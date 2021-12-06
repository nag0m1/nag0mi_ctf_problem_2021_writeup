# tweet
## 問題
Do you know the twitter account @okayama_uni? Please look for a past tweet using tweet capture. Certainly, that tweet was posted at 2017/8/18 and introduce a article.

note: flag is after the last slash in the article URL.

e.g. article URL: https://www.okayama-u.ac.jp/tp/profile/message_j.html,
flag: nag0m1{message_j.html}

[tweet.png](./chall/tweet.png)

## 解答
岡大公式twitterアカウントのツイートを投稿時間から探す．<br>
ツイートしているサイトページのurl中のファイル名部分がflagになる．

twitterの高度検索機能を使うとツイートを遡らなくても検索できる．<br>

> @okayama_uni since:2017-08-18_13:30:00_JST until:2017-08-18_14:00:00_JST

と検索すると画像と同じ時刻に投稿されたツイートが出てくる．<br>
urlは https://www.okayama-u.ac.jp/tp/release/release_id486.html なのでflagは以下の通り

<details>
  <summary>flag</summary>

  > nag0m1{release_id486.html}

</details>
