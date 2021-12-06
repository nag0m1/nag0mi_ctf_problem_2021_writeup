# Bundle Of Outstanding Knowledge

## 問題文

◆◆◆◆◆◆◆◆5278◆

OMG, I unintentionally spilled coffee.<br>
Please mend this number. orz. <br>
I have some information about this number: it represents a book, it was published by SB Creative Crop and sold in Japan.

*Flag format is nag0m1{year_month_number} <br>
e.g. If the number is 0000000052780 and the book published in 2021/09, the flag becomes nag0m1{2021_09_0000000052780}.

## 解答

書籍の識別コードISBNに関する問題．

2007年以降に発行された書籍は13桁の数字(978-出版された地域-出版者番号-書籍番号-チェックディジット)が振られる．

[wiki](https://ja.wikipedia.org/wiki/ISBN)や[ISBN出版社コード一覧](http://kazemakase.wjg.jp/comics/pubcode2.php)を参照すると，日本：4，SB Creative Corp：7973である．<br>
また，チェックディジットは先頭の数字から1,3,1,3,...を掛けて和をとり，和を10で割った余りを10から引いた値となる．（ただし，結果が10の場合は0とする．）<br>
チェックディジット前までの数字は978479735278なので計算すると8になる．<br>
ISBN：9784797352788で検索すると「UNIXコマンドブック 第3版」がヒットし，発行年月は2009年07月ということがわかる．

> nag0m1{2009_07_9784797352788}
