# nag0m1CTF

https://nag0mictf.tk

## malware

### Baes64

> The message is encrypted by base64 and AES-CTR. Can you decrypt this message? I think that the key to the problem is the characteristic of an encrypted message and an encrypted method.

base64とAES(-CTR)の複合問題です．（問題文がBase64ではなくB**aes**64になったの気づいていましたかね？）

この問題の特徴としては，鍵が見つからないという点ですね．

鍵については問題文から作成されていることがプログラムから分かります．

問題文をbase64で暗号化したあと，前から順番に0b10000000とANDを取って，"0"か否かで`key`の値を決めています．

base64で暗号化した後のデータはどうなっているかというと，ASCII文字となっています．

ASCII文字というのは，7bitで構成されている文字です．

したがって，8bit目をAND取ったところで0です．`key`は0です．

<br>

これを考慮して逆順で解いたら復号することができます．

気になる方は実際に復号して確認してみてくださいね．
