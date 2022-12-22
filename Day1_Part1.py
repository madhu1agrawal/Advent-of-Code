temp = 0
elf_cal = []
with open('input1.txt') as f:
    for line in f:
        if  line.strip():
            temp = temp + int(line.strip())
        else:
            elf_cal.append(temp)
            temp = 0
print(max(elf_cal))
