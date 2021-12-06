# What color does it look like?

## 問題
Looking for what you need

note: flag format is nag0m1{flag}

[black.png](./chall/black.png)

## 解答
一見すると真っ黒な画像だが，[RGB抽出](https://www.peko-step.com/tool/getcolor.html)を用いるとRGBが0x000000と0x010101の2つで作られていることが分かる．

RGB抽出ツールである[青空白猫](https://digitaltravesia.jp/usamimihurricane/webhelp/_RESOURCE/MenuItem/another/anotherAoZoraSiroNeko.html)を用いるか片方のRGB値を白に変更して違いを見やすくするプログラムを作る．<br>
出力としてはQRコードが表示され，読み取るとflagが見える．

<details>
  <summary>解答ソース</summary>

  ~~~
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt

  img = cv2.imread("black.png")
  img_array = np.asarray(img)

  for i in range(len(img_array)):
      for j in range(len(img_array[i])):
          if all(img_array[i][j] == np.array([1,1,1])):
              img_array[i][j] = np.array([0xff,0xff,0xff])

  cv2.imwrite("extract.jpg", img_array)
  ~~~
</details>

<details>
  <summary>flag</summary>

  > nag0m1{can_y0u_r3ad_qr}

</details>
