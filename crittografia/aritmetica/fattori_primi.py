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
        




num = int(input("inserire un nmero: "))

print(fattori_primi(num))