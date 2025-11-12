def main():
    lista_nomi = ["Luca","alessandro","robert","gabriele"]
    lista_voti = [[9,2,6],
                  [6,7],
                  [10,9,9],
                  [4,5]]
    #stampare la meda di ognunostampare n voti per ognuno stampare il voto massimo e minimo
    for nome,voti in zip(lista_nomi,lista_voti):
        print(f"{nome}: {voti}")
if __name__== "__main__": #dunder
    print(__name__)
    main()