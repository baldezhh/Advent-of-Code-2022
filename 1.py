with open('1_input.txt', 'r') as f:
    lines = f.readlines()

max = 0
current = 0
top_list = []
for item in lines:
    if item == '''\n''':
        if current > max:
            max = current
            top_list.append(max)
            current = 0
        else:
            top_list.append(current)
            current = 0
            continue
    else:
        current = current + int((item.replace('''\n''', '')))
        
print(max)
top_list.sort(reverse=True)
print(top_list[0]+top_list[1]+top_list[2])
