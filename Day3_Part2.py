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
with open('input3.txt') as f:
    while True:
        set1 = set(f.readline().strip())
        set2 = set(f.readline().strip())
        set3 = set(f.readline().strip())
        if not set1:
            break
        alpha = (set1 & set2 & set3).pop()
        score = score + alpha_dict[alpha]
        
        if not set1:
            break
print(score)
