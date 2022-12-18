#     rock  paper  scisors
me = {'X':1, 'Y':2, 'Z':3}
elf = {'A':1, 'B':2, 'C':3}
my_total = 0

def win(e):
    if elf[e] == 1: 
        return 3+6
    elif elf[e] == 2:
        return 1+6
    elif elf[e] == 3:
        return 2+6

def lose(e): 
    if elf[e] == 1: 
        return 2+0
    elif elf[e] == 2:
        return 3+0
    elif elf[e] == 3:
        return 1+0

def draw(e):
    if elf[e] == 1: 
        return 1+3
    elif elf[e] == 2:
        return 2+3
    elif elf[e] == 3:
        return 3+3


with open('2_input.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        if i[2] == 'X': 
            my_total+=lose(i[0])    
        elif i[2] == 'Y':
            my_total+=draw(i[0])
        elif i[2] == 'Z':
            my_total+=win(i[0])

print(my_total)
