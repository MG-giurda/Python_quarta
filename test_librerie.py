import funzioni
import random

def main ():
    voti = [random.randint(2,10)for i in range (10)] # una lista ripetuta casuale 10 volte 
    print(f"voti:{voti}")
    m,n = funzioni.media(voti)
    print(m)
if __name__ == "__main__":
    main()
