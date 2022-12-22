with open('input21.txt') as f:
    lines = f.readlines()
    
monkey_names = {}
for line in lines:
    line = line.strip().split(': ')
    if line[1].isnumeric():
        monkey_names[line[0]] = line[1]

unsolved = True
while(unsolved):
    unsolved = False
    for index in range(0, len(lines)):
        line = lines[index]
        monkey_name = line.strip().split(': ')[0]
        monkey_message = line.strip().split(': ')[1]

        if not monkey_message.isnumeric():
            monkey_1 = monkey_message.split(' ')[0]
            monkey_2 = monkey_message.split(' ')[2]
            modifier = monkey_message.split(' ')[1]

            if (monkey_1 in monkey_names) and (monkey_2 in monkey_names):
                monkey_names[monkey_name] = eval(str(monkey_names[monkey_1]) + modifier + str(monkey_names[monkey_2]))
                monkey_names[monkey_name] = eval(str(monkey_names[monkey_1]) + modifier + str(monkey_names[monkey_2]))
            else:
                unsolved = True
        if 'root' in monkey_names:
            print(monkey_names['root'])
            break
