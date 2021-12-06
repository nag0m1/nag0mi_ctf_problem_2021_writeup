from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import *
import base64

def decrypt(ct, key):
    aes_new = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    pt = aes_new.decrypt(ct)
    return pt

def read():
    with open("enc.txt", "r") as f:
        ct = f.read()
    return ct

def write(pt):
    with open("dec.txt", "w") as f:
        f.write(base64.b64decode(pt).decode())

def base64_decode(text):
    return base64.b64decode(text.encode())

def main():
    ct = base64.b64decode(read().encode())
    pt = decrypt(ct, (0).to_bytes(16,  byteorder="big"))
    write(pt)

if __name__ == "__main__":
    main()