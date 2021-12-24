### PART 1 ###


def treat_data(txt):
    with open(txt) as file: data = file.readlines()
    data = list(map(lambda x: eval(x.replace(" -> ", ",")), data))
    data = list(filter(lambda x: x[0] == x[2] or x[1] == x[3], data))
    
    for line in range(len(data)):
        x1, x2 = data[line][0], data[line][2] 
        y1, y2 = data[line][1], data[line][3]
        if ((x1 == x2 and y1 > y2) or (y1 == y2 and x1 > x2)):
            data[line] = (x2, y2, x1, y1)

    return data


def create_table(data):
    biggest_x, biggest_y, table = 0, 0, [[]]
    for line in range(len(data)):
        x1, x2 = data[line][0], data[line][2] 
        y1, y2 = data[line][1], data[line][3]
        
        if x1 > biggest_x: biggest_x = x1
        if x2 > biggest_x: biggest_x = x2
        
        if y1 > biggest_y: biggest_y = y1
        if y2 > biggest_y: biggest_y = y2
    
    for column in range(biggest_x + 1):
        table[0] += [0]
    for line in range(biggest_y):
        table += [table[0].copy()]
    
    return table


def insert_values(data, table):
    for insertion in range(len(data)):
        x1, x2 = data[insertion][0], data[insertion][2] 
        y1, y2 = data[insertion][1], data[insertion][3]
         
        if x1 == x2:
            for y in range(y1, y2 + 1):
                table[y][x1] += 1

        if y1 == y2:
            for x in range(x1, x2 + 1):
                table[y1][x] += 1
 
    return table


def check_overlap(table):
    count = 0
    for line in table:
        for value in line:
            if value > 1:
                count += 1

    return count


### PART 2 ###


def treat_data_part_2(txt):
    with open(txt) as file: data = file.readlines()
    data = list(map(lambda x: eval(x.replace(" -> ", ",")), data))
    data = list(filter(lambda x: x[0] == x[2] or x[1] == x[3] 
                        or abs((x[3] - x[1])/(x[2] - x[0])) == 1, data))
    
    for line in range(len(data)):
        x1, x2 = data[line][0], data[line][2] 
        y1, y2 = data[line][1], data[line][3]
        data[line] = sorted([[x1,y1],[x2,y2]], key=lambda k: [k[1], k[0]])
      
    return data


def create_table_part_2(data):
    biggest_x, biggest_y, table = 0, 0, [[]]
    for line in range(len(data)):
        x1, x2 = data[line][0][0], data[line][1][0] 
        y1, y2 = data[line][0][1], data[line][1][1]
        
        if x1 > biggest_x: biggest_x = x1
        if x2 > biggest_x: biggest_x = x2
        
        if y1 > biggest_y: biggest_y = y1
        if y2 > biggest_y: biggest_y = y2
    
    for column in range(biggest_x + 1):
        table[0] += [0]
    for line in range(biggest_y):
        table += [table[0].copy()]
    
    return table


def insert_values_part_2(data, table):
    for insertion in range(len(data)):
        x1, x2 = data[insertion][0][0], data[insertion][1][0]
        y1, y2 = data[insertion][0][1], data[insertion][1][1]
        if x1 > x2: our_range = range(x2, x1 + 1)
        else: our_range = range(x1, x2 + 1)
        
        if x1 == x2:
            for y in range(y1, y2 + 1):
                table[y][x1] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                table[y1][x] += 1
        elif abs((y2 - y1)/(x2 - x1)) == 1:  
            for x in our_range:
                y = int((y2 - y1)/(x2 - x1))*x + y2 - int((y2 - y1)/(x2 - x1))*x2
                table[y][x] += 1
                  
    return table
