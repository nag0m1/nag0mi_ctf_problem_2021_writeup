# anonymous

by kanon

## 問題
Let's do something a little more advanced.

Simple but difficult,can you solve it?

note: flag format is nag0m1{flag}


## 解答

RSA暗号の(RSA暗号の問題がないのは普通に誤算でした)上位互換のECC(Elliptic-curve cryptography)です。
簡単に解説しますと楕円曲線暗号はECDLPと呼ばれ、RSA暗号を解くよりも難しいです。ただ今回の曲線はorder=primeなのでanomalous曲線と呼ばれる曲線になります。<br>
anomalous曲線はorder=primeの性質によりSSSA攻撃という攻撃方法が成立しRSA暗号と同じDLP問題になります。
これによって簡単に解くことができます。

ECCは他にもいろいろな攻撃手段(どれも特殊なもの)があるので興味ある人は調べてもいいかもしれません。

補足として、今回はsagemathというものを使用しました。これを用いれば群・体の計算を簡単に用いることができます。

<details>
  <summary>flag</summary>

  > nag0m1{4n0m4l0u5_curv3}

</details>
