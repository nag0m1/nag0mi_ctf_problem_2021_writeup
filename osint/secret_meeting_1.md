# secret meeting 1
## 問題
Wataru, a competent detective, got information that the camarilla he is pursuing will hold a secret meeting at a certain location in Japan. Do you know the coordinates of this gate where they're going to meet?

Please round to the nearest fourth decimal place.<br>
note: flag format is nag0m1{latitude,longitude}<br>
e.g. (12.3456,123.4567) -> nag0m1{12.346,123.457}

[gate.jpg](./chall/gate.jpg)

## 解答
画像の場所を特定する問題<br>
secret meeting 1~4の共通として小数点以下第4位を四捨五入，flagはnag0m1{緯度,経度}となることに注意する．

google画像検索にかけると金沢駅前の門がヒット．<br>
google mapで探すと，[ココ](https://www.google.com/maps/place/%E9%BC%93%E9%96%80/@36.5778248,136.6492212,346m/data=!3m1!1e3!4m5!3m4!1s0x5ff8336a1d830563:0xb98e78ac002f627d!8m2!3d36.5778025!4d136.6491445)が出てくる．<br>
経緯度は(36.5778248,136.6492212)なので，

<details>
  <summary>flag</summary>

  > nag0m1{36.578,136.649}

</details>
