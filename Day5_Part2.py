import numpy as np

with open('input5.txt') as f:
    lines = f.readlines()
    
stacks = []
for line in lines:
    list1 = []
    if line.strip():
        line = line.replace('\n','').replace('    ',' 0 ').replace('[','').replace(']','').replace(' ','')
        for x in line:
            list1.append(x)  
        stacks.append(list1)               
    else:
        break
stacks = np.array(stacks).T
stacks = np.flip(stacks, axis=1).tolist()
stacks = {row[0]: row[1:] for row in stacks}
for key in stacks:
    while '0' in stacks[key]:
        stacks[key].pop()
        
count=0
with open('input5.txt') as f:
    lines = f.readlines()
    
for line in lines:

    temp_stack=[]
    if count <= len(stacks):
        count+=1
    else:
        number = line.strip().split(' ')[1]
        source = line.strip().split(' ')[3]
        dest = line.strip().split(' ')[5]

        if int(number)==1:
            move_crate = stacks[source].pop()
            stacks[dest].append(move_crate)
        else:
            for crates in range(1,int(number)+1):
                temp_stack.append(stacks[source].pop())
            for i in range(0,len(temp_stack)):
                stacks[dest].append(temp_stack.pop())

            
output = ''           
for key in stacks:
    output = output + stacks[key].pop()
print(output)
