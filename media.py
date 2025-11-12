def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [
        [6, 7, 8, 5],
        [7, 6],
        [8, 10, 9, 9],
        [5, 8]
    ]

    for nome, voti in zip(lista_nomi, lista_voti):
        somma = 0
        n_voti = len(voti)

        voto_max = voti[0]
        voto_min = voti[0]

        for voto in voti:
            somma += voto
            if voto > voto_max:
                voto_max = voto
            if voto < voto_min:
                voto_min = voto

        media = somma / n_voti

        # stampa separata
        print(f"Studente: {nome.upper()}")
        print(f"  Media dei voti: {media}")
        print(f"  Voto massimo: {voto_max}")
        print(f"  Voto minimo: {voto_min}\n")
        


if __name__ == "__main__":
    main()
