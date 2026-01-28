f = open("binaryFile.bin", "wb")
for i in range(30):
    f.write(i.to_bytes(2, byteorder='little'))
f.close()
f = open("binaryFile.bin", "rb")
while True:
    bytes_read = f.read(2)
    if bytes_read == b'':
        break
    else:
        print(int.from_bytes(bytes_read, byteorder='little'))