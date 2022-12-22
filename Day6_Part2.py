with open('input6.txt') as f:
    line = f.readline().strip()

for i in range(4,len(line),1):
    if len(set(line[i-4:i]))==4: 
        break
for j in range(i, len(line),1):
    if len(set(line[j:j+14]))==14:
        print(line[j:j+14])
        print(j+14)
        break
