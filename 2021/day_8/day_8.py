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
        for j in range(len(data[1][1])): 
            if len(output[1][j]) in [2, 4, 3, 7]: numbers += 1
    
    return numbers


txt = "input.txt"
data = treat_data(txt)
print(find_numbers(data))
