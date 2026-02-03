f1 = open("mo.wav", "rb")
f2 = open("SICKOMODE.wav", "rb")
fw = open("combined.wav", "wb")

header1 = f1.read(44)
header2 = f2.read(44)

header1 = bytearray(header1)
header2 = bytearray(header2)
#gets the file size
size1 = int.from_bytes(header1[4:8], "little")
size2 = int.from_bytes(header2[4:8], "little")

datasize1 = int.from_bytes(header1[40:44],"little")
datasize2 = int.from_bytes(header2[40:44],"little")
newdatasize = datasize1+datasize2
new_file_size = newdatasize + 36


header1[4:8] = new_file_size.to_bytes(4, "little")
header1[40:44] = newdatasize.to_bytes(4, "little")

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
        sample_faded = int(sample_int * factor)
        fw.write(sample_faded.to_bytes(2, "little", signed=True))
    else:
        fw.write(sample_bytes)  # Just write original bytes
    
    i += 1

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
