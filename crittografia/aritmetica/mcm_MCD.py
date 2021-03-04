def eDivisibile(num1, num2):
    ciao = False
    if(num1 % num2 == 0):
        ciao = True
    return ciao


def mcm(num1,num2):
    return num1*num2/MCD(num1,num2)

def MCD(num1,num2):
    
    vettore = []
    if(num2>num1):
        #inverte in modo tale che num1 sia maggiore di num2
        num1,num2 = num2,num1    
    while(1):
        n = num1 % num2 
        if(n==0):
            break
        vettore.append(n)
        num1 = n
    return vettore[-1]


n1 = int(input("inserire un numero: "))
n2 = int(input("inserire un altro numero: "))
print(f"il minimo comune multiplo è {mcm(n1,n2)}")
print(f"il minimo comune multiplo è {MCD(n1,n2)}")