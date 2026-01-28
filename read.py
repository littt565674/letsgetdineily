# Euan-readData1.py
# Exploration: reading text and binary data

FILENAME = "data/homework1.txt"

# -------------------------
# Step 1: Reading in text
# -------------------------
print("STEP 1: Reading file as text\n")

line_count = 0

file = open(FILENAME, "r")

for line in file:
    print(line.strip())   # strip to avoid extra blank lines
    line_count += 1

file.close()

print(f"\nTotal number of lines: {line_count}\n")


# ----------------------------------
# Step 2: Reading in binary (1 byte)
# ----------------------------------
print("STEP 2: Reading file as binary (1 byte at a time)\n")

byte_count = 0

file = open(FILENAME, "rb")

while True:
    byte = file.read(1)   # read one byte
    if not byte:
        break
    print(byte)
    byte_count += 1

file.close()

print(f"\nTotal number of bytes: {byte_count}\n")


# -------------------------------------------------
# Step 3: Reading in binary (? bytes at a time)
# -------------------------------------------------
print("STEP 3: Reading file line-by-line in binary\n")

file = open(FILENAME, "rb")

while True:
    # Read the UTF-8 character (4 bytes)
    char_bytes = file.read(4)
    if not char_bytes:
        break

    # Read the newline character (1 byte)
    newline = file.read(1)

    # Decode and print the character
    print(char_bytes.decode("utf8"))

file.close()

