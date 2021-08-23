#next and previous

def next(lista, x):
    ind = lista.index(x)
    return lista[ind+1]

def previous(lista, x):
    ind = lista.index(x)
    return lista[ind-1]