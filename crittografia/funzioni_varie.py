def MCD(num1,num2):
    c = 0
    vettore = []
    if(num2>num1):
        #inverte in modo tale che num1 sia maggiore di num2
        num3 = num1
        num1 = num2
        num2 = num3
    print(f"MCD tra {num1} e {num2}")
       
    while(1):
        n = num1 % num2 
        if(n==0):
            if(c==0):
                vettore.append(num2)
            break
        vettore.append(n)
        num1 = num2
        num2 = n
        c = c + 1
    return vettore[-1]

def mcm(num1,num2):
    return (num1*num2)/MCD(num1,num2)

def fattori_primi(n):
    f_p = []
    c = 2

    while(n!=1):
        
        if(n % c == 0):
            f_p.append(c)
            n = n / c
            c = 1
        
        c = c + 1

    return f_p
        

def rsa_calcolo_d(c , m):
    contatore = 1  
    while((c * contatore) % m != 1):
        contatore = contatore + 1
    return contatore

def rsa_calcolo_c(m):
    print(m)
    for c in range(2 , m):
        if(MCD(c,m) == 1):
            break
    return c
    

def main():
    print(MCD(27,18))


if __name__ == "__main__":
    main()