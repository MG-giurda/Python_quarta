#l'utente inserisce in input la password 
# il programma stampa la password con gli asterischi
password = input("inserisci una password --> ")
#len serve per prendere la lunghezza della parola faccio (len (password)-2) pk per me serveno tenere la prima e
#l'ultima quindi tevo tenerle solo 2 ù
password_blanked = password[0] + "*" * (len(password)-2) + password[-1]    
print(f"hai inserito la password --> {password_blanked}")