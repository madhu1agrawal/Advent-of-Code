with open('input6.txt') as f:
    line = f.readline().strip()

for i in range(4,len(line),1):
    if len(set(line[i-4:i]))==4: 
        print(line[i-4:i])
        print(i)
        break
