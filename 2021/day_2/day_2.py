with open("input.txt") as file: data = file.readlines()
processed_data = list(map(lambda x: int(x[-3:]), data))

def part1(data):
    horizontal, depth = 0, 0
    for movement in range(len(data)):
        if "forward" in data[movement]: horizontal += processed_data[movement]
        elif "up" in data[movement]: depth -= processed_data[movement]
        else: depth += processed_data[movement]
    
    return horizontal * depth

def part2(data):
    horizontal, depth, aim = 0, 0, 0
    for movement in range(len(data)):
        if "forward" in data[movement]: 
            horizontal += processed_data[movement]
            depth += aim * processed_data[movement]
        elif "up" in data[movement]:
            aim -= processed_data[movement]
        else:
            aim += processed_data[movement]
    
    return horizontal * depth

### PRINTS ###
print(part1(data))
print(part2(data))
