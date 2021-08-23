#sequencias
import nextandprevious as np

lista = list(map(int, input().split()))
def find_ratio(x, n=1):
    difs, found = [], False
    for i in x:
        if i != x[-1]:
            difs.append(np.next(x, i)-i)
    if difs[0] == difs[1]:
        found = True
        print("A P.A. tem ordem {} e razão {}".format(n, difs[0]))
    else:
        n+=1
        find_ratio(difs, n)
find_ratio(lista)