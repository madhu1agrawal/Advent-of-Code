import pandas as pd

df = pd.read_csv('input2.txt', delimiter=" ", header=None)
df = df.replace(['A', 'B', 'C'], ['X', 'Y', 'Z'])

score=0
for index, row in df.iterrows():
    if row[1]=='X':
        score += 1
    elif row[1]=='Y':
        score += 2
    else:
        score+=3
    if row[0]==row[1]:
        score += 3
    if row[0]=='X' and row[1]=='Y':
        score+=6
    if row[0]=='X' and row[1]=='Z':
        score+=0
    if row[0]=='Y' and row[1]=='X':
        score+=0
    if row[0]=='Y' and row[1]=='Z':
        score+=6
    if row[0]=='Z' and row[1]=='X':
        score+=6
    if row[0]=='Z' and row[1]=='Y':
        score+=0
print(score)
