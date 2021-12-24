data = open("input.txt").read().splitlines() 
x_data = []
for i in range(len(data)):
    x_data.append(int(data[i].replace(' ', ',').split(",")[0]))
    x_data.append(int(data[i].replace(' ', ',').split(",")[1]))
y_data = []
for i in range(len(data)):
    y_data.append(int(data[i].replace(' ', ',').split(",")[1]))
    y_data.append(int(data[i].replace(' ', ',').split(",")[4]))
nx = max(x_data)
ny = max(y_data)

"""
Part1 : At how many points do at least two lines overlap?
"""
print("====PART1====")
import numpy as np

diagram = np.zeros((nx+1, ny+1), dtype=np.int) # empty diagram

for i in range(len(data)):
    x1 = int(data[i].replace(' ', ',').split(",")[0])
    y1 = int(data[i].replace(' ', ',').split(",")[1])
    x2 = int(data[i].replace(' ', ',').split(",")[3])
    y2 = int(data[i].replace(' ', ',').split(",")[4])
    if x1==x2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        y = y1-y2
        if y>1 : 
            for i in range(1,abs(y)):
                diagram[y1-i][x1]+=1
        else:
            for i in range(1,abs(y)):
                diagram[y1+i][x1]+=1
    if y1==y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        if x>0 : 
            for i in range(1,abs(x)):
                diagram[y2][x2+i]+=1
        else:
            for i in range(1,abs(x)):
                diagram[y2][x2-i]+=1 

print("number of points where at least two lines overlap :",len(np.where(diagram >= 2)[0]))
