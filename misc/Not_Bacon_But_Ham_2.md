# Not Bacon But Ham 2
## 問題
This ham looks better than that before.

note: flag format is nag0m1{flag}

[ham2.txt](./chall/ham2.txt)
[ham2.py](./chall/ham2.py)

## 解答
n=7, k=4の拡張ハミング符号のデコードプログラムを作成する問題<br>

(7,4)ハミング符号は7 bit毎に1 bitまでのエラー訂正を保証するものであったが，2 bitエラーが起きた場合にはエラーが起きてないものとして処理される．<br>
対して拡張(7,4)ハミング符号は1 bitまでのエラー訂正と2 bitまでのエラー検出を保証する．<br>

拡張(7,4)ハミング符号のエンコードは(7,4)ハミング符号と同様のエンコードを行った後，偶パリティビットとしてさらに1 bit付加する（8 bit中1になっているビット箇所が偶数になるように調整すること）<br>
プログラムを見ると，エンコードの式はNot Bacon But Ham 1をベースにしているので，生成行列<img src="https://latex.codecogs.com/gif.latex?G">は前問の生成行列にパリティ部分を付けた以下のように表される．
<br><br>
<img src="https://latex.codecogs.com/gif.latex?G=&space;\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;0&space;&&space;1&space;&&space;1\\&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;1\\&space;0&space;&&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;1\\&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;0&space;&1&space;\end{bmatrix}">
<br><br>
検査行列<img src="https://latex.codecogs.com/gif.latex?H">は少し特殊でパリティ計算のため4行目がall 1になる．
<br><br>
<img src="https://latex.codecogs.com/gif.latex?H=&space;\begin{bmatrix}&space;1&space;&&space;1&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;0&space;&&space;1&space;&&space;0&space;&&space;0\\&space;1&space;&&space;1&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;0\\&space;1&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;1&space;\end{bmatrix}">
<br><br>
となる．

8 bitの符号語 c = [ c0, c1, c2, c3, c4, c5, c6, c7 ] と<img src="https://latex.codecogs.com/gif.latex?H^T">の乗算結果 r = [r0, r1, r2, r3 ] とエラー検出の対応は以下の通り
- [0 0 0 0] => エラーなし
- <img src="https://latex.codecogs.com/gif.latex?H">の列に対応したビット列 => 1 bitエラー，列番号と同じ番号にエラーが入っているため訂正可能
- [0 0 0 0]でもなく<img src="https://latex.codecogs.com/gif.latex?H">の列に対応したビット列でもない => 2 bitエラー，検出のみで訂正不可

今回の問題はflagをascii 2進数表記にしたビット列に対して8 bit毎に1 bitまたは2 bitのエラーが起きている．<br>
2 bitエラーが起きた箇所は訂正できないため，正しいflagを伝えるにはflagのビット列をノイズチャネルに通した結果を複数回行う必要があり，今回は10回行った．<br>
よって，ham2.txtのi番目の出力のうち，2 bitエラーが起きた箇所は1 bitエラーで訂正可能な他のj番目の出力を参照するように元のflagを求める．

<details>
  <summary>解答ソース</summary>

  ~~~
  import numpy as np

  with open("ham2.txt", mode="r") as f:
      data = [s.strip() for s in f.readlines()]

  ht = np.array([[1,1,0,1,1,0,0,0], [0,1,1,1,0,1,0,0], [1,1,1,0,0,0,1,0], [1,1,1,1,1,1,1,1]]).T
  err2 = [9,9,9,9,9,9,9,9]
  N = 10

  t = []
  for i in range(N):
      s = np.array([int(data[i][j]) for j in range(len(data[i]))]).reshape((len(data[i])//8, 8))
      s_ht = np.dot(s, ht) % 2
      t0 = []
      for j in range(len(s_ht)):
          if list(s_ht[j]) in ht.tolist():    # 1 bit error
              for k in range(len(ht)):
                  if list(s_ht[j]) == ht.tolist()[k]:
                      break
              s[j][k] = s[j][k] ^ 1
              t0.append(s[j].tolist())
          elif list(s_ht[j]) not in ht.tolist():  # 2 bit error
              t0.append(err2)
      t.append(t0)

  ans = [0]*(len(s_ht))
  for i in range(N):
      for j in range(len(s_ht)):
          if t[i][j] != err2:
              ans[j] = t[i][j]
          elif (t[i][j] == err2) and (ans[j] == 0):
              pass

  s1 = ""
  for i in range(len(ans)):
      s1 += "".join([str(n) for n in ans[i][:4]])
  flag = "".join([chr(int(s1[i:i+8], 2)) for i in range(0, len(s1), 8)])
  print(flag)
  ~~~

</details>

<details>
  <summary>flag</summary>

  > nag0m1{city_country_shank-end_boneless_etc}

</details>
