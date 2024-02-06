with open('zadania maturalne marzec 2021\galeria-przykład.txt', 'r') as f: txt = [x.rstrip() for x in f]
lst = []
for z in range(len(txt)):
    x = txt[z].split(' ')
    i = 0
    wynik = 0
    while (4+i) <= len(x):
        if x[(2+i)] != '0' and x[3+i] != '0':
            wynik += (int(x[(2+i)])*int(x[3+i]))
        i += 2
    lst.append((x[1], wynik, int((len(list(filter(lambda x: x != '0',x)))-2)/2)))
for miasto, pow, ilość in lst:
    print(miasto, pow, ilość)
min = min(lst, key=lambda x: x[1])
max = max(lst, key=lambda x: x[1])
print('min: ', min[0], min[1], min[2])
print('max: ', max[0], max[1], max[2])
