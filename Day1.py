lines = open('input1.txt').read().splitlines()

erglist = []
erg = 0
for i in lines:
    if i == '':
        erglist.append(erg)
        erg = 0
    else:
        erg += int(i)

print(max(erglist))
erglist.sort(reverse=True)
print(erglist[0]+ erglist[1]+ erglist[2])