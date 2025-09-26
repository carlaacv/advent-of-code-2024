distance = []
list1 = []
list2 = []
result1 = 0
counter = 0
result2 = 0

with open('day1-input.txt') as f: 
    for each_line in f.readlines():
        x, y = (each_line.strip()).split("   ", 2)
        list1.append(int(x))
        list2.append(int(y))


list1.sort()
list2.sort()


for a, b in zip(list1, list2):
    if b >= a: 
        x = b-a
        distance.append(x)
    else:
        x = a-b
        distance.append(x)


for i in distance: 
    result += i

print(result)

## part 2 ##

for a in list1: 
    for b in list2:
        if a == b: 
            #print('a and be are the same', a, b)
            counter += 1
    if counter != 0: 
        result2 += (a*counter)
    counter = 0

print(result2)