#creare un programma in python che chiede all'utente un numero 
# e lo stampa se il numero è divisibile per 2 ,3,5 
#usare operatore % per il resto della divisione 
print("inserisci un numero")
num = int(input("-> "))
if num % 2 == 0:
    print("numero divisibile per 2")
elif num % 3 == 0:
    print("numero divisibile per 3")
elif num % 5 == 0:
    print("numero divisibile per 5")
else :
    print("numero non divisible")