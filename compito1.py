#s = input("scrivi un stringa ")
#sl = s.lower()
#if sl == sl[::-1]:
#   print("la stringa è uguale")
#else :
#    print("la stringa non è uguale")

#s = int(input("scrivi un numero"))
#for i in range(1,s+1,1):  # primo numero è il numero da cui parte il ciclo il secondo arrivo il terzo è il salto
#   print(i*i)
import math #serve per fare le rice quadrate
s = int(input("scrivi un numero"))
somma = 0
for i in range(1,s*2+2,2):  # primo numero è il numero che parte il secondo arrivo il terzo è il salto
   print(i)
   somma += i
radice_intera = math.isqrt(somma) # radice quadrate ma prende solo il numero intero
print(f"la somma è : {somma} , quadrato perfetto {radice_intera**2 == somma}") #con == mi restituisce un bool

