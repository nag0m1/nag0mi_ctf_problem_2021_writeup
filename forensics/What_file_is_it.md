# What file is it?

## 問題
I found a broken flag.

note: flag format is nag0m1{flag}

[broken](./chall/broken)

## 解答
一部が破損したファイルの復元を行う問題

拡張子が消されているが，バイナリエディタやstringsコマンドを用いるとIHBR(一部破損), sRGBなどが見えpngファイルと推測できる．<br>
IHBRは本来だとIHDRであり，他にも数ヵ所書き換えられているので，[PNG ファイルフォーマット解説サイト](https://www.setsuki.com/hsp/ext/png.htm)などを見つつ
[ブラウザで処理できるバイナリエディタ](https://www.oh-benri-tools.com/tools/programming/hex-editor)やHeD Hex Editor等を用いて修正する．

修正箇所は
- 1行目
  - FNG => PNG
  - IHBR => IHDR
- ラスト1行目
  - IEMD => IEND

の3箇所<br>
修正したファイルに拡張子.pngを付けると正しくファイルが開かれてflagが見える．

<details>
  <summary>flag</summary>

  > nag0m1{png_png_png}

</details>
