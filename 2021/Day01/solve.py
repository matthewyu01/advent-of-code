with open ('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
for i in range(1,len(lines)):
    if int(lines[i-1][:-1]) < int(lines[i][:-1]):
        count += 1
print(f"Part 1: Increased Count: {count}")

count = 0
for i in range(len(lines)-3):
    if int(lines[i][:-1]) < int(lines[i+3][:-1]):
        count += 1
print(f"Part 2: Increased Count: {count}")

    
