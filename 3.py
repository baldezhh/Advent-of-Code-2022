import string

def intersection(arr1, arr2):
    arr3 = [value for value in arr1 if value in arr2]
    return arr3

with open('3_input.txt', 'r') as f:
    lines = f.read().splitlines()

priority = string.ascii_letters
sum_1, sum_2 = 0, 0

for i in lines:
    x = intersection(i[len(i)//2:], i[:len(i)//2])
    sum_1 = sum_1 + priority.index(x[0]) + 1

for i in range(0, len(lines), 3):
    x = set(lines[i]).intersection(set(lines[i+1]).intersection(set(lines[i+2])))
    sum_2 = sum_2 + priority.index(x.pop()) + 1

print(sum_1)
print(sum_2)
