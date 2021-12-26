def treat_data(txt):
    with open(txt) as file: data = file.readlines()
    for line in range(len(data)):
        data[line] = list(data[line][:len(data[line]) - 1])
        data[line] = list(map(int, data[line]))

    return data


def find_low_pp(data):
    LD, LL, risk_lev = len(data), len(data[0]), 0
    for line in range(LD):
        for pp in range(LL):
            back, front, top, bottom = False, False, False, False
            if data[line][pp] == 9: continue

            if (((pp - 1 >= 0) 
                and (data[line][pp - 1] > data[line][pp]))
                or pp - 1 < 0):
                back = True

            if (((pp + 1 < len(data[line])) 
                and (data[line][pp + 1] > data[line][pp]))
                or pp + 1 >= len(data[line])):
                front = True

            if (((line - 1 >= 0) 
                and (data[line - 1][pp] > data[line][pp]))
                or line - 1 < 0):
                top = True

            if (((line + 1 < len(data)) 
                and (data[line + 1][pp] > data[line][pp]))
                or line + 1 >= len(data)):
                bottom = True

            if back and front and top and bottom:
                risk_lev = risk_lev + data[line][pp] + 1
    
    return risk_lev


### PART 2 ###
#from collections import deque

def get_point_value(map, point):
    return map[point[1]][point[0]]


def find_surround_points(map, coord):
    points = [(coord[0], coord[1] - 1), 
              (coord[0] + 1, coord[1]), 
              (coord[0], coord[1] + 1), 
              (coord[0] - 1, coord[1])]
              
    points = list(filter(lambda x: 0<=x[0]<len(map[0]) 
                        and 0<=x[1]<len(map), points))

    return points


def check_points(map, point, blacklist): 
    size, waiting = 0, [point]
    while len(waiting) != 0:
        size += 1
        blacklist.append(waiting[0])
        points = find_surround_points(map, waiting[0])
        waiting.remove(waiting[0])
        for point in points:
            if point in blacklist or get_point_value(map, point) == 9:
                continue
            else:
                blacklist.append(point)
                waiting.append(point)

    return size


def check_basin_size(map):
    LL, CC, sizes, blacklist = len(map), len(map[0]), [], []
    for line in range(LL):
        for col in range(CC):
            if map[line][col] == 9: 
                points = find_surround_points(map, (col, line)) 
                num_point, two_points = 0, [0, 0]
                for pp in points:
                    if num_point == 2: break
                    if (get_point_value(map, pp) != 9  
                        and pp not in blacklist):
                        two_points[num_point] = pp
                        num_point += 1
                try: sizes += [check_points(map, two_points[0], blacklist)]
                except: pass 
                try: sizes += [check_points(map, two_points[1], blacklist)]
                except: pass
    sizes.sort()
     
    return sizes[-1] * sizes[-2] * sizes[-3]
