#l'utente inserisce in input la password 
# il programma stampa la password con gli asterischi
password = input("inserisci una password --> ")
password_blanked = "*"*len(password)     #len serve per prendere la lunghezza della parola 
print(f"hai inserito la password --> {password_blanked}")