import pandas as pd

df = pd.read_csv('input2.txt', delimiter=" ", header=None)
df = df.replace(['A', 'B', 'C'], [1, 2, 3])

score=0
for index, row in df.iterrows():
    if row[1]=='X':
        score += 0
    elif row[1]=='Y':
        score += 3
    else:
        score+=6
    if row[1]=='Y':
        score += row[0]
    if row[0]==1 and row[1]=='X':
        score+=3
    if row[0]==1 and row[1]=='Z':
        score+=2
    if row[0]==2 and row[1]=='X':
        score+=1
    if row[0]==2 and row[1]=='Z':
        score+=3
    if row[0]==3 and row[1]=='X':
        score+=2
    if row[0]==3 and row[1]=='Z':
        score+=1
print(score)
