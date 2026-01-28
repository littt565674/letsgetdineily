f1 = open("mo.wav", "rb")
f2 = open("mo2.wav", "rb")
fw = open("combined.wav", "wb")

# Read the first 44 bytes of the first file (WAV header)
header1 = f1.read(44)
header2 = f2.read(44)

header1 = bytearray(header1)
header2 = bytearray(header2)
#gets the file size
size1 = int.from_bytes(header1[4:8], "little")
size2 = int.from_bytes(header2[4:8], "little")

new_size = size1 + size2
header1[4:8] = new_size.to_bytes(4, "little")



while True:
    b = f1.read(1)
    if not b:
        break
    fw.write(b)

f1.close()

#Make it so that the data size info and stuff is carried over into the first header
for i in range(44):
    f2.read(1)


while True:
    b = f2.read(1)
    if not b:
        break
    fw.write(b)

f2.close()
fw.close()

print("Hello World")
