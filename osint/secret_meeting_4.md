# secret meeting 4
## 問題
The long chase is finally coming to an end.<br>
We've finally found their main hideout.<br>
The building in the image is their base.<br>
Please identify the coordinates of their hiding place!!

Please round to the nearest fourth decimal place.<br>
note: flag format is nag0m1{latitude,longitude}<br>
e.g. (12.3456,123.4567) -> nag0m1{12.346,123.457}

[place.png](./chall/place.png)

## 解答
最後は画像から得られる情報をもとに推測を立てて建造物の場所を特定する．

画像から分かる情報として，<br>
1.看板のeinbahnstraßeを検索するとドイツ語ということからドイツで取られた写真と推測<br>
2.写真の中に日本とスイスの国旗が見える

「ドイツ　日本」などで検索するとサジェストに大使館，総領事館などが出てきてある程度建物の推測が立つ．<br>
[ドイツにある日本大使館・総領事館](https://www.de.emb-japan.go.jp/itpr_ja/konsular_index.html)は在ドイツ日本国大使館，在デュッセルドルフ日本国総領事館，在ハンブルク日本国総領事館，在フランクフルト日本国総領事館，在ミュンヘン日本国総領事館がある．<br>
順に調べていくと[在ハンブルク日本国総領事館](https://www.google.co.jp/maps/@53.5510638,9.9937065,3a,75y,353.11h,93.93t/data=!3m6!1e1!3m4!1sKxH9QJYF9xMa_Ro__av0jA!2e0!7i13312!8i6656?hl=ja)で画像通りの場所が見つかる．

flagは建物の場所なので，建物の経緯度を求めると(53.5514174,9.9929029)より

<details>
  <summary>flag</summary>

  > nag0m1{53.551,9.993}

</details>
