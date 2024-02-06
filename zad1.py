with open('zadania maturalne marzec 2021\galeria-przykład.txt', 'r') as f: txt = [x.rstrip() for x in f]
#print(txt)
kod = [(x.split(' ')[0], x.split(' ')[1]) for x in txt]
lst = []
for i in kod:
    licz = 0
    for x in kod:
        if i[0] == x[0]:
            licz += 1
    if not (i[0], licz) in lst:
        lst.append((i[0], licz))
for k,l in lst:
    print(k,l)
