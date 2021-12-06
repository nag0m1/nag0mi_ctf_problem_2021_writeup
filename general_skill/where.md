# where
## 問題
where is the flag.txt?

note: flag format is nag0m1{flag}

[where.zip](./chall/where.zip)

## 解答
大量にあるフォルダからflagを探し出す問題

flag formatをたよりに"nag0m1"が書かれているファイルを再帰的に探し出すようにコマンドを打つ．<br>

> grep nag0m1 -r ./

grep: ファイル中の文字列を検索<br>
-r : 再帰的に検索するオプション<br>
./ : 現在のディレクトリ以下から探索

<details>
  <summary>flag</summary>

  > nag0m1{f1ag_i5_h3r3}

</details>
