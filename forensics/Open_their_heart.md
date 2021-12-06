# Open their heart

## 問題
Hear their mind when they exit!!

note: flag format is nag0m1{flag}

[conversation.txt](./chall/conversation.txt)

## 解答
難読プログラミング言語の1つ，シェイクスピア言語で書かれたプログラム

ファイルの登場人物がシェイクスピアの4大悲劇ハムレット，オセロ，リア王，マクベスのヒロインであることから「シェイクスピア　プログラム」等で検索して推測する．

シェイクスピア言語では最初の行から最初のピリオドまではコメントと見なされる．<br>
2行目以降からAct Iまでの間に変数の宣言が行われ，変数名にはシェイクスピアの作中に出てくる人物しか使えない制約がある．<br>

プログラムは舞台の台本のように書かれているが，Actなどの幕と場は今回の問題では無視してよい．<br>
変数への値の格納は以下の手順で行われる．
1.  [Enter]で舞台に上がる人物（扱う変数）を決める．（最初は必ず2人以上を登場させる）
2.  人物：セリフ によって値の代入が行われるが，この際のセリフは相手に言っているので，自分以外の変数にセリフによって決まった値が格納される．（連続して同じ人物がセリフを言うときは「人物：」は省略可能）
~~~
[Enter A and B]
A: You are a flower.
~~~
とするとBに値が格納される．

3.  格納された値を表示するための文は，Open your heart.とSpeak your mind.の2つがあり，それぞれ話しかけられた相手の値とascii文字を表示する．
4.  使い終わった変数は[Exit]を使って退場させる．
5.  1.に戻る．

配布されたプログラムは値を格納しているだけになっているので，[Exit]や[Exeunt]で退場させられる前にSpeak your mind.によってasciiを出力させてみるとflagが出てくる．

ブラウザで実行してくれる[サイト](https://tio.run/#spl)を使用すると良い．

<details>
  <summary>値に関する説明</summary>

  - 名詞を１または-1として扱い，そこに形容詞がついた分だけ2がかけられる．1になる名詞はflowerなどのきれいとされる名詞，-1になるのはpigなどの汚れているとされる名詞，また，中性名詞は1として扱う．<br>
  (the noble beautiful flower は形容詞が2つついているので，1×2×2で4となる．)
  - 2乗と3乗はsquare of，cube ofで表すことができる．
  - yourselfやthyselfは話しかけられた人物自身の値を表す．
  - as 形容詞 as は代入記号と同じ
  - sum A and B や difference A from B でA+B，A-Bが計算される．

  これらを用いて値を設定する．<br>
  例）
  ~~~
  [Enter A and B]
  A:
  You are the noble beautiful flower.
  You are as good as sum of the square of yourself and the dirty pig.
  ~~~
  とすると，最初のセリフでBに4が格納される．<br>
  2つ目のセリフでは<img src="https://latex.codecogs.com/gif.latex?B=B^2&plus;(-1)\times2">が実行され，B=14となる．

</details>

<details>
  <summary>flag</summary>

  > nag0m1{to_be_or_not_to_be}

</details>
