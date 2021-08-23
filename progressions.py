#progressao aritmetica

#PA de 1a ordem
def soma_pa(x, y, z): #a1, an, r
	soma=0
	for i in range(x, y+1, z):
		soma+=1
	return soma

#PG
def soma_pg(x, y, z): #a1, an, r
    soma, an = 0, x
    while an<=y:
        soma, an = soma+an, an*z
    return soma

#PA de 2a ordem
def soma_pa_2(x, y, z, k): #a1, an, r, b1
    soma, an, bn = 0, x, k
    while an <= y:
        soma, an, bn = soma+an, an+bn, bn+z
    return soma

#PA de 3a ordem
def soma_pa_3(x, y, z, k, w): #a1, an, r, b1, c1
    soma, an, bn, cn = 0, x, k, w
    while an <= y:
        soma, an, bn, cn = soma+an, an+bn, bn+cn, cn+z
    return soma