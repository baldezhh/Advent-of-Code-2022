#     rock  paper  lesbians
me = {'X':1, 'Y':2, 'Z':3}
elf = {'A':1, 'B':2, 'C':3}
my_total = 0

def win(i): return me[i]+6
def lose(i): return me[i]+0
def draw(i): return me[i]+3

with open('2_input.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        if me[i[2]] == elf[i[0]]:
            my_total += draw(i[2]) 
        elif me[i[2]] == 1 and elf[i[0]] == 2:
            my_total += lose(i[2])
        elif me[i[2]] == 1 and elf[i[0]] == 3:
            my_total += win(i[2])
        elif me[i[2]] == 2 and elf[i[0]] == 1:
            my_total += win(i[2])
        elif me[i[2]] == 2 and elf[i[0]] == 3:
            my_total += lose(i[2])
        elif me[i[2]] == 3 and elf[i[0]] == 1:
            my_total += lose(i[2])
        elif me[i[2]] == 3 and elf[i[0]] == 2:
            my_total += win(i[2])

print(my_total)
