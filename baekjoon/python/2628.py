import sys

sys.stdin = open('input.txt', 'r')

temp = sys.stdin.read().splitlines()

total = list(map(int, temp[0].split()))

wid = [0, total[0]]
leng = [0, total[1]]

for a in range(2, len(temp)) :

    temp_int = list(map(int, temp[a].split()))
    
    if int(temp_int[0]) == 0 :
        leng.append(temp_int[1])

    else :
        wid.append(temp_int[1])

wid_int = list(map(int, wid))
leng_int = list(map(int, leng))

wid_int_sor = sorted(wid_int)
leng_int_sor = sorted(leng_int)

var_wid = []
var_leng = []

for i in range(len(wid_int_sor)-1) :
    ele_w = wid_int_sor[i+1] - wid_int_sor[i]
    var_wid.append(ele_w)

for j in range(len(leng_int_sor)-1) :
    ele_l = leng_int_sor[j+1] - leng_int_sor[j]
    var_leng.append(ele_l)

print(max(var_wid) * max(var_leng))