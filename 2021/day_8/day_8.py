def treat_data(txt):
    with open(txt) as file: data = file.readlines()

    data = list(map(lambda x: x[:len(x) - 1].split(' | '), data)) 
    for item in range(len(data)):
        for i in range(2):
            data[item][i] = data[item][i].split(' ')

    return data


def find_numbers(data):
    numbers = 0
    for output in data:
        for j in range(len(output[1])): 
            if len(output[1][j]) in [2, 4, 3, 7]: numbers += 1
    
    return numbers


def find_numbers(data):
    for output in data:
        numbers = ['', '', '', '', '', '', '', '', '', '']
        current_line = output[0].copy()
        for j in range(len(current_line)):
            if len(current_line[j]) == 2: 
                numbers[1] += current_line[j]
                current_line[j] = 1
            elif len(current_line[j]) == 4: 
                numbers[4] += current_line[j]
                current_line[j] = 4
            elif len(current_line[j]) == 3: 
                numbers[7] += current_line[j]
                current_line[j] = 7
            elif len(current_line[j]) == 7: 
                numbers[8] += current_line[j]
                current_line[j] = 8
            
            elif 'e' not in current_line[j]: 
                numbers[2] += current_line[j]
                current_line[j] = 2
            elif (('e' and 'b' in current_line[j]) 
                    and (len(current_line[j]) == 5)):
                numbers[3] += current_line[j]
                current_line[j] = 3
            elif len(current_line[j]) == 5:
                numbers[5] += current_line[j]
                current_line[j] = 5       
        print(numbers)

    return numbers

txt = "test.txt"
data = treat_data(txt)
print(find_numbers(data))
