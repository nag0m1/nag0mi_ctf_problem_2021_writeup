from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64

def encrypt(pt, key):
    aes_new = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    ct = aes_new.encrypt(pt)
    return ct

def read():
    with open("flag.txt", "r") as f:
        pt = f.read()
    return pt

def write(ct):
    out = base64.b64encode(ct).decode()
    with open("enc.txt", "w") as f:
        f.write(out)

def genkey(pt_enc):
    pt_enc_str = pt_enc.decode()
    key = 0
    for ch in range(128):
        if (ord(pt_enc_str[ch]) & 0b10000000):
            key = (key << 1) ^ 0b1
        else:
            key = key << 1
    return key


def main():
    pt = base64.b64encode(read().encode())
    key = genkey(pt)
    ct = encrypt(pt, key.to_bytes(16, byteorder="big"))
    write(ct)

if __name__ == "__main__":
    main()