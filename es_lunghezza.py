lista = ["Luca","alessandro","robert","gabriele"]
nmax = 0
nomemax = ""
nomeup = ""
for nome in lista:
    nomeup = nome.upper()
    print(nomeup)
    n=len(nome)
    if(n>nmax):
        nmax= n
        nomemax = nome
        
print(nomemax)

