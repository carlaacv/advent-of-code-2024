counter = 0
safe_counter = 0

with open('day2/input.txt') as f: 
    lines = f.readlines()
    for each_line in lines:
        new_line = each_line.strip().split(" ")
        for i in range(len(new_line)-1): 
            if int(new_line[i]) > int(new_line[i+1]) and (int(new_line[i])-int(new_line[i+1]) in [1,2,3]): 
                counter = counter + 1
            elif int(new_line[i]) < int(new_line[i+1]) and (int(new_line[i+1])-int(new_line[i]) in [1,2,3]): 
                counter = counter - 1
            elif int(new_line[i+1]) == int(new_line[i]): 
                continue
            else: 
                continue
        if abs(counter) == len(new_line)-1: 
            counter = 0
            safe_counter += 1
        else: 
            counter = 0

print(safe_counter)