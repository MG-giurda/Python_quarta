#in Python possiamo delimitare con "" oppure con ''
stringa = "Ciao mondo !"
print(stringa )
#Esempio di indicizzazione  della stringa 
print(f"l'unico carattere delle stringa è {stringa[-1]}")

# esempio di slicing delle stringhe 
# è un modo di tagliare le stringhe 
print(f"la sottostringa 2-5 è {stringa[2:5]}.")# il primo carattere è incluso il secondo è escluso 
# prende tutti i caratteri dalla posizione 2 include e 5 esculo 

#assegnazione multipla
nome, cognome = "Mario" , "Rossi"
# concatenazione tra stringhe (vale per ogni tipo di dato )
x = nome + " "+ cognome
print(x)

# concatenazione multipla
y = nome*5 
print(y)