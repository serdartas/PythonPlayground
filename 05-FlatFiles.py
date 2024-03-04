# Create a flat file
myFile = open("./myTestFile.txt", mode="+w")
# some modes
# r: open for reading
# r+: read and write
# w: write
# a: appending
# +: create
# +w: create file and open it for writing

# Write text to the file
myFile.write("10 Hello World!")
myFile.close()

# Append text to file
myFile = open("./myTestFile.txt", mode="a")
myFile.write("\n20 New text")
myFile.write("\n30 Newer text")
myFile.close()

# Read file
with open("./myTestFile.txt", mode="r") as myFile:
    for line in myFile.readlines():
        print(line)
