f = open("image.bmp","rb")
fw = open("image.bmp", "wb")


file_type = f.read(2)
print(file_type)

file_size = f.read(4)
print(int.from_bytes(file_size,"little"))

start_pos = f.read(4)

print(int.from_bytes(start_pos,"little"))



image_header_size = f.read(4)
print(int.from_bytes(image_header_size, "little"))

image_height = f.read(4)
print(int.from_bytes(image_height, "little"))

image_width = f.read(4)
print(int.from_bytes(image_width, "little"))

num_planes = f.read(2)
print(int.from_bytes(num_planes,"little"))

bits_per_pix = f.read(2)
print(int.from_bytes(bits_per_pix,"little"))
temp = f.read(24)
print(int.from_bytes(temp,"little"))

for i in range(124):
    for j in range(124):
        pixel_color = f.read(3)
        
        if not pixel_color: 
                break
            
        if pixel_color == b"\xf8\x00\x00":
                print("R", end="")
                fw.write(b"\x00\x00\xf8")  
        elif pixel_color == b"\xf8\x00\xf8":
                print("M", end="")
                fw.write(pixel_color)  
        elif pixel_color == b"\xf8\xf8\x00":
                print("Y", end="")
                fw.write(pixel_color)
        elif pixel_color == b"\x00\x00\xf8":
                print("B", end="")
                fw.write(b"\xf8\x00\x00")  
        elif pixel_color == b"\x00\xf8\x00":
                print("G", end="")
                fw.write(pixel_color)  
        elif pixel_color == b"\x00\x00\x00":
                print("K", end="")
                fw.write(pixel_color) 
        elif pixel_color == b"\x00\xf8\xf8":
                print("C", end="")
                fw.write(pixel_color)  
print()
f.close()
fw.close()