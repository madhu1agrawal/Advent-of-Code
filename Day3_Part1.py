import string

alpha_dict = {}
value = 1
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
alphabates = lower + upper

for alphabate in alphabates:
    alpha_dict[alphabate] = value
    value += 1
    
score = 0
elf_cal = []
with open('input3.txt') as f:
    for line in f:
        line = line.strip()
        set1 = set(line[:len(line)//2])
        set2 = set(line[len(line)//2:])
        alpha = set1.intersection(set2).pop()
        score = score + alpha_dict[alpha]
print(score)
