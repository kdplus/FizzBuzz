di = {}
m = None
with open("./input.txt", "r") as f:
    ret = None
    while ret is None or len(ret) == 2:
        s = f.readline()
        ret = s.split(':')
        if len(ret) == 2:
            di[int(ret[0])] = ret[1][:-1]
        else:
            m = int(ret[0])

sorted_di = sorted(di.items(), key=lambda i : int(i[0]))
flag = True
for k, v in sorted_di:
    if m % int(k):
        continue
    else:
        print(v, end="")
        flag = False

if flag:
    print(m)