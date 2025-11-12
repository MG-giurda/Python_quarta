#in python abbiamo le collezioni , tra le condizioni abbiamo:
#liste,tuple,dizionari,set.

#lista:
l = [3,4,5,6,"ciao",True]
#per accedere agli elementi vivono le stesse regole 
#di INDICIZZAZIONE e SLICING delle stringhe 

print (f"L'ultimo della lista è {l[-1]}")
print (f"tutta la lista senza il proma elemento e l'ultimo elemento {l[1:-1]}")

#aggiunta di un elemento 
l.append("NUOVO") # non aggiunge nulla ma modifica l 

l.pop()#toglie l'ultimo elemento della lista 