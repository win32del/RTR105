f = open("zedd.txt")
for line in f:
    if line.startswith("hello"):
        print(line)
