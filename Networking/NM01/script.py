from pwn import *

host = args.HOST or 'cfta-nm01.allyourbases.co'
port = int(args.PORT or 8017)
io = connect(host, port)

hex_code = io.recvline()
hex_str = "".join(hex_code.split("\\x")).strip()
decoded_str = bytearray.fromhex(hex_str).decode()
print("Decoded String: " + decoded_str)

io.sendline(decoded_str)
io.interactive()
