def treat_data(txt):
    with open(txt) as file: data = file.readlines()
    for line in range(len(data)):
        data[line] = data[line][:len(data[line]) - 1]

    return data


def get_point_value(map, point):
    return int(map[point[1]][point[0]])


def find_surround_points(map, coord):
    points = [(coord[0], coord[1] - 1), 
              (coord[0] + 1, coord[1]), 
              (coord[0], coord[1] + 1), 
              (coord[0] - 1, coord[1])]
              
    points = list(filter(lambda x: 0<=x[0]<len(map[0]) 
                        and 0<=x[1]<len(map), points))

    return points


### PART 1 ###

def find_low_pp(data):
    LD, LL, risk_lev = len(data), len(data[0]), 0
    for line in range(LD):
        for col in range(LL):
            pp = (col, line)
            points = find_surround_points(data, pp)
            bigger_points = list(filter(lambda x: get_point_value(data, x) 
                                > get_point_value(data, pp), points))
            
            if len(bigger_points) == len(points):
                risk_lev = risk_lev + get_point_value(data, pp) + 1
   
    return risk_lev


### PART 2 ###

def check_points(map, point, blacklist): 
    size, waiting = 0, [point]
    blacklist.append(waiting[0])
    while len(waiting) != 0:
        size += 1
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
            if get_point_value(map, (col, line)) == 9: 
                points = find_surround_points(map, (col, line))
                for pp in points:
                    if (get_point_value(map, pp) != 9  
                        and pp not in blacklist):
                        point = pp
                try: sizes += [check_points(map, point, blacklist)]
                except: pass 
    sizes.sort()
     
    return sizes[-1] * sizes[-2] * sizes[-3]
