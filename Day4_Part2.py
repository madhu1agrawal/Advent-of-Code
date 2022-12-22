count = 0
with open('input4.txt') as f:
    while True:
        line = f.readline().strip()

        if not line:
            break
        l1 = int(line.split(',')[0].split('-')[0])
        u1 = int(line.split(',')[0].split('-')[1])

        l2 = int(line.split(',')[1].split('-')[0])
        u2 = int(line.split(',')[1].split('-')[1])

        set1 = set(range(l1, u1+1))
        set2 = set(range(l2, u2+1))
        
        if set1.intersection(set2):
            count += 1
            
print(count)
