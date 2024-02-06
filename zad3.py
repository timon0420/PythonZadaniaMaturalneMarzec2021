with open('zadania maturalne marzec 2021\galeria-przykład.txt', 'r') as f: txt = [x.rstrip() for x in f]
lst = []
for z in range(len(txt)):
    x = txt[z].split(' ')
    i = 0
    wynik = []
    while (4+i) <= len(x):
        if x[(2+i)] != '0' and x[3+i] != '0':
            wynik.append((int(x[2+i])*int(x[3+i])))
        i += 2
    lst.append((x[1], len([wynik.count(x) for x in set(wynik)])))
print(f'MAX: {max(lst, key=lambda x: x[1])}, MIN: {min(lst, key=lambda x: x[1])}')
