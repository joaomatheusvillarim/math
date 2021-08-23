import progressoes
n=1
x = progressoes.soma_pa_3(1, n**3, 6, 7, 12) == ((n*(n+1))/2)**2
y = progressoes.soma_pa_3(1, (n+1)**3, 6, 7, 12)  - (progressoes.soma_pa_3(1, n**3, 6, 7, 12) ) ==  (((n+1)*((n+1)+1))/2)**2 - ( ((n*(n+1))/2)**2)
print(x and y)