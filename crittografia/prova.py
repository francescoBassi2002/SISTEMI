def numeroPrimo(n):
    ciao = False
    a = 2
    print("inizio a verificare")
    while(a < n-1):
        if (n % a == 0 ):
            break
        a = a + 1   

    if(a == n-1):
        ciao = True
        print(f"{n} è un numero primo")
    else:
        print(f"{n} non è un numero primo")    

    return ciao

numeroPrimo(int(input("")))