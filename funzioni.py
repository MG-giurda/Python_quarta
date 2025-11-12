# il codice deve essere diviso in funzioni --> MODULARITÀ
#COSTANTE è UNA VARIABILE GLOBALE
#ATTENZIONE : accessibile da tutte le funzioni ma soltante in lettura 
COSTANTE = 3.14
def prima_lettera_maiuscola(stringa):
    '''
    DOCSTRING
    la funzione restituisce il nome con la lettera iniziale maiuscola
    '''
    #stringa è un una variabile locale
    s = stringa[0].upper()+ stringa[1:].lower()
    return s
def media(lista):
    '''
    restituisce la media dei valori presenti in lista 
    e il numero di elementi di lista 
    '''
    somma = 0.
    n_lista = len(lista)
    for val in lista :
        somma = somma + val 
    return somma /n_lista,n_lista

def main():
# print(help(prima_lettera_maiuscola))
   #nome = input("inserisci una parola ")
   # print(prima_lettera_maiuscola(nome))
   voti = [4.5,5.6,6.7,7.8]
   m,n = media(voti)
   print(f"la media è {m}, il numero di voti {n}")
   pass
if __name__ == "__main__":
    main()