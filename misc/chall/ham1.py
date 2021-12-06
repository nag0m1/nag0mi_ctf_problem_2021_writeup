import random

def encode(s):
    c = []
    x = [0] * 4
    for i in range(len(s)//4):
        for j in range(4):
            x[j] = int(s[i*4:i*4+4][j])
        c.append(s[i*4:i*4+4] + str(x[0]^x[1]^x[3]) + str(x[1]^x[2]^x[3]) + str(x[0]^x[1]^x[2]))
    return c

def noisy_channel(c):
    noisy_data = []
    for ci in c:
        r = random.randint(0,6)
        noisy_data.append(ci[:r] + str(int(ci[r])^1) + ci[r+1:])
    return "".join(noisy_data)

if __name__ == "__main__":
    with open("flag.txt", mode="r") as f:
        s = f.readline()
        
    s = "".join(list(map(lambda x:bin(ord(x))[2:].zfill(8), s)))

    c = encode(s)

    noisy_data = noisy_channel(c)

    with open("ham1.txt", mode="w") as f:
        f.write(noisy_data)
