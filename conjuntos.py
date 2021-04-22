listaA = input("Insira os elementos de A: ").split()
listaB = input("Insira os elementos de B: ").split()
for x in listaA:
    x = int(x)
listaA = set(listaA)
for x in listaB:
    x = int(x)
listaB = set(listaB)

a = (listaA == listaB) #Se A = B
b = bool(listaA) #Se A é conjunto vazio
b = not b
c = (len(listaA) == 1) #Se A é conjunto unitário
d = bool(listaB) #Se B é conjunto vazio
d = not d
e = (len(listaB) == 1) #Se B é conjunto unitário
f = listaA.issubset(listaB) #Se A é subconjunto de B
g = listaB.issubset(listaA) #Se B é subconjunto de B
h = listaA.isdisjoint(listaB) #Se A e B são disjuntos
i = 2**(len(listaA)) #Número de subconjuntos de A
j = 2**(len(listaB)) #Número de subconjuntos de B
k = listaA.union(listaB) #União de A e B
l = listaA.intersection(listaB) #Intersecção de A e B
m = listaA.difference(listaB) #Diferença de A e B
n = listaB.difference(listaA) #Diferença de B e A
o = 2**(len(k)) #Número de subconjuntos de A união B
p = 2**(len(l)) #Número de subconjuntos de A intersecção B

print("A é igual B : %s" %a)
print("A é vazio: %s" %b)
print("A é unitário: %s" %c)
print("B é vazio: %s" %d)
print("B é unitário: %s" %e)
print("A é subconjunto de B: %s" %f)
print("B é subcojunto de A: %s" %g)
print("A e B são disjuntos: %s" %h)
print("Número de subconjuntos de A: %d" %i)
print("Número de subcojuntos de B: %d" %j)
print("União de A e B:", k)
print("Intersecção de A e B: ", l)
print("Diferença de A e B: ", m)
print("Diferença de B e A: ", n)
print("Número de subconjuntos de A união B: %d" %o)
print("Número de subconjuntos de A intersecção B: %d" %p)