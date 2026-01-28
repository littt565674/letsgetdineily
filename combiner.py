f1 = open("mo.wav", "rb")
f2 = open("SICKOMODE.wav", "rb")
fw = open("combined.wav", "wb")

header1 = f1.read(44)
data_pos = header1.find(b"data")
header2 = f2.read(44)


header1 = bytearray(header1)
header2 = bytearray(header2)
#gets the file size
size1 = int.from_bytes(header1[4:8], "little")
size2 = int.from_bytes(header2[4:8], "little")

new_size = size1 + size2

new_riff_size = (size1 - 8) + (size2 - 8) + 8 #riff causing errors 
header1[4:8] = new_riff_size.to_bytes(4, "little")

new_data_size = (size1 - 44) + (size2 - 44)  
header1[data_pos + 4 : data_pos + 8] = new_data_size.to_bytes(4, "little")

fw.write(header1)

fade_samples = 44100 * 4 * 2
i=0
while True:
    sample_bytes = f1.read(2)
    if not sample_bytes:
        break

    sample_int = int.from_bytes(sample_bytes, "little", signed=True)

    if i < fade_samples:
        factor = i / fade_samples
    else:
        factor = 1

    sample_faded = int(sample_int * factor)

    fw.write(sample_faded.to_bytes(2, "little", signed=True))
    i += 1


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
