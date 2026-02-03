f1 = open("mo.wav", "rb")
f2 = open("SICKOMODE.wav", "rb")
fw = open("combined.wav", "wb")

header1 = f1.read(100)
header2 = f2.read(100)

header1 = bytearray(header1)
header2 = bytearray(header2)
data_pos1 = header1.find(b"data")
data_pos2 = header2.find(b"data")
overlapsize = 3
#gets the file size
datasize1 = int.from_bytes(header1[data_pos1+4:data_pos1+8], "little")
datasize2 = int.from_bytes(header2[data_pos2+4:data_pos2+8], "little")

newdatasize = datasize1+datasize2
new_file_size = newdatasize + 36


header1[4:8] = new_file_size.to_bytes(4, "little")
header1[data_pos1+4:data_pos1+8] = newdatasize.to_bytes(4, "little")

fw.write(header1)

fade_samples = 44100 * 4 * 2
i=0
while True:
    sample_bytes = f1.read(2)
    if datasize1 - 88000:
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


#combiner
for i in range(88000):
    #write both f1 and f2 at same time for that 10 seconds from the datasize1 - 10 thing

while True:
    b = f2.read(2)
    if not b:
        break
    fw.write(b)

f2.close()

fw.close()

print("Hello World")
