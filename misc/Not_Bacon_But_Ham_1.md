# Not Bacon But Ham 1
## 問題
Do you like ham?

note: flag format is nag0m1{flag}

[ham1.txt](./chall/ham1.txt)
[ham1.py](./chall/ham1.py)

## 解答
(7,4)ハミング符号のデコードプログラムを作成する問題<br>

プログラムの流れは以下の通り，<br>
1.flag.txtに書かれたテキストをasciiで読み取り8 bitに拡張したものを2進数表記でsに格納<br>
2.sがハミング符号によってエンコードされ，リストcにはc=[c0,c1,...]と符号語ci (i=0,1,...) が格納<br>
3.各ciごとに1 bitエラーを引き起こすノイズチャネルを通過

(n,k)ハミング符号はk bitの情報ビットに対して(n-k) bitの符号ビットを付加することでn bitに拡張し，n bitごとにn, kから決まるある程度までのエラー訂正を保証する．<br>
n, kはプログラムから読み取ると n=7, k=4 となる．
よって，(7,4)ハミング符号であることが分かり，次は符号化で用いる生成行列<img src="https://latex.codecogs.com/gif.latex?G">を考える．
また，(7,4)ハミング符号の特徴として，1符号語につき1 bitエラーまで訂正できることが挙げられる．

(7,4)ハミング符号における符号化は4 bitのビット列 s = [s0, s1, s2, s3]を1行の行列と見なし，そこに生成行列<img src="https://latex.codecogs.com/gif.latex?G">をかけることで7 bitのビット列<img src="https://latex.codecogs.com/gif.latex?sG">が得られる処理となっている．<br>
その際の生成行列<img src="https://latex.codecogs.com/gif.latex?G">は <img src="https://latex.codecogs.com/gif.latex?G=[I_4|A]">，( <img src="https://latex.codecogs.com/gif.latex?I_4"> は4×4の単位行列)で表されるので，<img src="https://latex.codecogs.com/gif.latex?A">をソースコードから求める．

~~~
c.append(s[i*4:i*4+4] + str(x[0]^x[1]^x[3]) + str(x[1]^x[2]^x[3]) + str(x[0]^x[1]^x[2]))
~~~

のうち，<br>
s[i\*4:i*4+4] は単位行列をかけていることを表しており，<br>
str(x[0]^x[1]^x[3]), str(x[1]^x[2]^x[3]), str(x[0]^x[1]^x[2]) が<img src="https://latex.codecogs.com/gif.latex?G">の5,6,7列目を表している．<br>
bitごとの加算は排他的論理和で表されることに注意すると，生成行列<img src="https://latex.codecogs.com/gif.latex?G">は以下のように表される．
<br><br>
<img src="https://latex.codecogs.com/gif.latex?G&space;=&space;\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;0&space;&&space;1\\&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;1\\&space;0&space;&&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;1\\&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;0&space;\end{bmatrix}">
<br><br>
また，復号と訂正に用いる検査行列<img src="https://latex.codecogs.com/gif.latex?H">は<img src="https://latex.codecogs.com/gif.latex?G">をもとに得ることができ，<img src="https://latex.codecogs.com/gif.latex?H=[A^T&space;|&space;I]">で求められる.<br>
（<img src="https://latex.codecogs.com/gif.latex?A">は<img src="https://latex.codecogs.com/gif.latex?G">で用いた行列<img src="https://latex.codecogs.com/gif.latex?A">の転置行列，<img src="https://latex.codecogs.com/gif.latex?I">は単位行列）
よって，検査行列<img src="https://latex.codecogs.com/gif.latex?H">は
<br><br>
<img src="https://latex.codecogs.com/gif.latex?H&space;=&space;\begin{bmatrix}&space;1&space;&&space;1&space;&&space;0&space;&&space;1&space;&&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;1&space;&&space;1&space;&&space;0&space;&&space;1&space;&&space;0\\&space;1&space;&&space;1&space;&&space;1&space;&&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}">

となる．
<br><br>
後の流れは[wiki](https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%9F%E3%83%B3%E3%82%B0%E7%AC%A6%E5%8F%B7)に従う．<br>
7 bitのビット列に<img src="https://latex.codecogs.com/gif.latex?H^T">をかけると，エラーが起きてない場合は[0 0 0]が出力され，1 bitエラーが起きていた場合はHの列に対応したビット列が出てきて，その列番号がエラーが起きたビット番号を表している．<br>
（例：[1 1 1 1 1 1 1]<img src="https://latex.codecogs.com/gif.latex?H^T">=[0 1 1]が出てきた場合，<img src="https://latex.codecogs.com/gif.latex?H">の3列目に対応しているため，3 bit目にエラーが起きていたことが分かる．よって，正しいビット列は[1 1 0 1 1 1 1]となる）<br>

ham1.txtに書かれたビット列を7 bitで区切り，上記の処理を行った後，訂正のために付加した符号ビットである後半3 bitを取り除いたものを結合することで本来のflagのasciiコードが得られる．

<details>
  <summary>解答ソース</summary>

  ~~~
  import numpy as np

  with open("ham1.txt", mode="r") as f:
      data = f.readline()

  s = np.array([int(data[i]) for i in range(len(data))]).reshape((len(data)//7, 7))

  ht = np.array([[1,1,0,1,1,0,0], [0,1,1,1,0,1,0], [1,1,1,0,0,0,1]]).T
  sh = np.dot(s, ht) % 2

  for i in range(len(sh)):
      for j in range(len(ht)):
          if list(sh[i]) == list(ht[j]):
              s[i][j] = s[i][j] ^ 1

  s1 = "".join(list(map(str, s[:, :4].reshape(1,4*len(s)).tolist()[0])))
  flag = "".join([chr(int(s1[i:i+8], 2)) for i in range(0, len(s1), 8)])
  print(flag)

  ~~~

</details>

<details>
  <summary>flag</summary>

  > nag0m1{h4m_15_s0_delicious!!}

</details>
