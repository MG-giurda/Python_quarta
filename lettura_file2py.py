def main():
    file = open("./mac-vendors-export.csv", "r", encoding="utf-8")#encoding="utf-8" serve per risolvere gli errorei di windows
    righe = file.readlines()
    file.close()
    mac_adress = []
    vendor = []

    #input("inserisci il mac adress -->")
    for riga in righe[1:]:
        print(riga)
        campi = riga.split(",")
        mac_adress.append(campi[0])
        vendor.append(campi[1])
        print(campi)
    print(mac_adress)
   
    mac = input("Inserisci il MAC adress --> ").upper()

    for m,v in zip(mac_adress,vendor):
        if m[0:8] == mac[0:8]:
            print(f" il produttore è : {v}")
        


if __name__ == "__main__":
    main()
