f = open("zedd.txt")
for line in f:
    line = line.rstrip()
    if not "is" in line:
        continue
    print(line)
