# Can you find it?
## 問題
Find the flag in this directory.

note: flag format is nag0m1{flag}

[seven.zip](./chall/seven.zip)

## 解答
解凍すると7つのファイルが出てくる．

それぞれが他のファイルと1行異なるものになっており，異なっている箇所をつなげるとflagが出てくる．<br>
ファイルの差を出力するdiffコマンドと，複数のコマンドの標準出力をまとめて扱う(&)を使う.

~~~
> (diff 1.txt 2.txt & diff 3.txt 4.txt & diff 5.txt 6.txt & diff 6.txt 7.txt ) > ans.txt
~~~
ansの中身を見ると，


```
1001c1001
< {sp
---
> 0t_
1001c1001
< the
---
> _d1
1001c1001
< ff3
---
> r3n
1001c1001
< r3n
---
> c3}
```

となっており，これらをつなげるとflagになる

<details>
  <summary>flag</summary>

  > nag0m1{sp0t_the_d1ff3r3nc3}

</details>
