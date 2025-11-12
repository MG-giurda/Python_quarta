ip = input("inserisci un ip -> ")
ottetti_str= ip.split(".") 
# metodo stringhe che suddivide una stringa 
# cercando il carattere separtore
print(ottetti_str) 
ottetti = []
for s in ottetti_str:
    ottetti.append(int(s))
print(bin(ottetti[0]))
#chiede all'utente un numero binario se la lunghezza è minore del numero del bit gli aggiungo a sinistra tanti zeri quanti il numero di bit 
