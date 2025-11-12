def main_0():
    lista = ["Luca","alessandro","robert","gabriele"]
    nomemax = None 
    lenmax = 0
    for nome in lista:
        if(len(nome)>lenmax):
            nomemax = nome
            lenmax = len(nome)
    print(nomemax)

def main():
    lista = ["Luca","alessandro","robert","gabriele"]
    nomemax = None 
    lenmax = 0
    for i,nome in enumerate(lista):
        print(f"{i}-{nome}")
if __name__== "__main__": #dunder
    print(__name__)
    main()