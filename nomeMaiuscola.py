# creare un programma in python e chiede all'utente il suo nome 
# e lo stampa sempre con l'iniziale maiuscola 
print("inserisci il tuo nome ")
nome = input("-> ")
m = nome[0] 
m= m.upper()
# quando metto [1:] vuol dire che prendo dal sacondo carattere fino alla fine della parola 
mnuovo = m + nome[1:].lower() 
print(f"{mnuovo}")


