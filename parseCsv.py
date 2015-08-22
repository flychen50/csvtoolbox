# coding=utf-8
f = open('hadp.txt', 'r')
x_info = set()
y_info = set()
i = 0
tb = {}
for line in f.readlines():
    line = line.strip()
    info = line.split(',')
    if i == 0:
        x, y, z = info
    else:
        xlabel = info[0]
        ylable = info[1]
        value = info[2]
        x_info.add(xlabel)
        y_info.add(ylable)
        if xlabel not in tb:
            tb[xlabel] = {}
        tb[xlabel][ylable] = value
    i = i + 1


x_info = sorted(x_info)
y_info = sorted(y_info)
res = str(x) + "/" + str(y) + "," + ",".join(y_info) + "\n"
for x in x_info:
    res += str(x)
    for y in y_info:
        if y not in tb[x]:
            res += "," + str(0)
        else:
            res += "," + str(tb[x][y])
    res += "\n"

print res
