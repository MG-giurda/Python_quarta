def main():
    file = open("./mac-vendors-export.csv", "r", encoding="utf-8")#encoding="utf-8" serve per risolvere gli errorei di windows
    righe = file.readlines()
    file.close()
    mac = "00:15:5D"
    #input("inserisci il mac adress -->")
    for riga in righe:
        if riga[0:8] == mac:
            print(riga)
        


if __name__ == "__main__":
    main()
