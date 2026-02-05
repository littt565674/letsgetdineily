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

# maybe we change to 128 later if to un noticable
overlap = 88000 * 64

header1[4:8] = new_file_size.to_bytes(4, "little")
header1[data_pos1+4:data_pos1+8] = newdatasize.to_bytes(4, "little")

fw.write(header1)

data1 = f1.read(datasize1)
data2 = f2.read(datasize2)

fw.write(data1[:-overlap])

for i in range(0, overlap, 2):  # Step by 2, not 1!
    sample1 = int.from_bytes(data1[-overlap + i: -overlap + i + 2], "little", signed=True)
    sample2 = int.from_bytes(data2[i:i + 2], "little", signed=True)
    combined = (sample1 + sample2) // 2
    fw.write(combined.to_bytes(2, "little", signed=True))

fw.write(data2[overlap:])

f1.close()
f2.close()
fw.close()
#Make it so that the data size info and stuff is carried over into the first header
#for i in range(44):
 #   f2.read(1)


#combiner
#while True:
 #   b = f2.read(2)
  #  if not b:
   #     break
    #fw.write(b)

#f2.close()

#fw.close()

print("Hello World")
