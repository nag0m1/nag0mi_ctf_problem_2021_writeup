# how many primes
## 問題
How many primes are existing less than or equal to 5000?

note: flag format is nag0m1{count}
e.g. If the number of primes is 10, the flag becomes nag0m1{10}.

## 解答
5000以下の素数の値を答える問題

「5000 素数」等で調べると[数の性質](https://ja.numberempire.com/5000)が出てくるのでそこから前の素数に飛べば何番目の素数か分かる．

判定プログラムの例は以下の通り

<details>
  <summary>解答ソース</summary>

  ~~~
  #!/usr/bin/env python
  import math

  UPPER = 5000

  if __name__ == "__main__":
      primes = [2]

      for i in range(3,UPPER):
          for j in range(len(primes)):
              if math.sqrt(i) < primes[j]:
                  primes.append(i)
                  break
              elif i%primes[j] == 0:
                  break

      print("the number of primes is ",len(primes))
  ~~~

</details>

<details>
  <summary>flag</summary>

  > nag0m1{669}

</details>
