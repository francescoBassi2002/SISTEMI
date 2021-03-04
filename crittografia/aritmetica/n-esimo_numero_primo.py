#dato un numero n trovare l'n-esimo numero primo

def numeroPrimo(n):
    ciao = False
    a = 2

    while(a < n-1):
        if (n % a == 0 ):
            break
        a = a + 1

    if(a == n-1):
        ciao = True
        print(f"{n}")  

    return ciao

n = int(input("Inserire un numero: "))
numero = 0
contatore = 0
while(contatore < n):
    numero = numero + 1
    if(numeroPrimo(numero)):
        contatore = contatore + 1

print(f"l'{n}-esimo numero primo è {numero}")