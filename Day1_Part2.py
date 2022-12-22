temp = 0
elf_cal = []
with open('input1.txt') as f:
    for line in f:
        if  line.strip():
            temp = temp + int(line.strip())
        else:
            elf_cal.append(temp)
            temp = 0
elf_cal.sort(reverse=True)
top3 = elf_cal[0] + elf_cal[1] + elf_cal[2]
print(top3)
