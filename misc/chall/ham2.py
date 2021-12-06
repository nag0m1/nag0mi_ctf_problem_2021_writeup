import random

def encode(s):
    c = []
    x = [0] * 4
    for i in range(len(s)//4):
        for j in range(4):
            x[j] = int(s[i*4:i*4+4][j])
        t = s[i*4:i*4+4] + str(x[0]^x[1]^x[3]) + str(x[1]^x[2]^x[3]) + str(x[0]^x[1]^x[2])
        t = t + str((t.count("1") % 2))
        c.append(t)
    return c

def very_noisy_channel(c):
    ret = []
    err_bit = [i for i in range(8)]
    for ci in c:
        err_count = random.randint(1,2)
        r = sorted(random.sample(err_bit, err_count))
        if len(r) == 0:
            ret.append(ci)
        elif len(r) == 1:
            ret.append(ci[:r[0]] + str(int(ci[r[0]])^1) + ci[r[0]+1:])
        elif len(r) == 2:
            ret.append(ci[:r[0]] + str(int(ci[r[0]])^1) + ci[r[0]+1:r[1]] + str(int(ci[r[1]])^1) + ci[r[1]+1:])
        else:
            print("too many noise")
            exit(1)
    return "".join(ret)

if __name__ == "__main__":
    with open("flag.txt", mode="r") as f:
        s = f.readline()

    s = "".join(list(map(lambda x:bin(ord(x))[2:].zfill(8), s)))

    c = encode(s)

    with open("ham2.txt", mode="w") as f:
        for i in range(10):
            data = very_noisy_channel(c)
            f.write(data+"\n")
