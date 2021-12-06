# png has many message

## 問題
can you get flag in png??

note: flag format is nag0m1{flag}

[message.png](./chall/message.png)

## 解答

pngファイルにはコメントを付け足すことができる．<br>
コメントの開始はtEXTで始まることが決まっているため，バイナリエディタでファイルを開いて該当箇所を探すか，コマンドにて
~~~
> strings message.png | grep tEXT
~~~
とするとコメントが出てくる．<br>
コメントは bmFnMG0xe3RleHRfaW5fcG5nX2Ywcm1hdH0= となっており，あとはこれをbase64でデコードする．

<details>
  <summary>flag</summary>

  > nag0m1{text_in_png_f0rmat}

</details>
