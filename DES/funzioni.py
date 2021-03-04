import socket as sck
N_chiavePubblica_passaggioChiavi = 9973
g_chiavePubblica_passaggioChiavi = 9949


def passaggio_key_invia(N,g):
    ip = '127.0.0.1'
    port = 8080

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect((ip,port))
    
    while(1):
        a = int(input(f'inserisci a (minore di {N}): '))
        if a<N:
            break
    
    A = (g**a) % N

    s.sendall(str(A).encode()) 
    B = int(s.recv(4096).decode())

    chiave = (B ** a) % N
    s.close()
    print(chiave)
    print(f"chiave in binario : {bin(chiave)[2:57]}")
    return bin(chiave)[:57]

def passaggio_key_ricevi(N,g):
    ip = '127.0.0.1'
    port = 8080
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind((ip,port))
    s.listen()
    
    conn,tupla = s.accept()
    while(1):
        b = int(input(f'inserisci b (minore di {N}): '))
        if b<N:
            break
    
    
    A = int(conn.recv(4096).decode())
    
    B = (g**b) % N

    conn.sendall(str(B).encode())

    chiave = (A ** b) % N
    s.close()
    print(chiave)
    print(f"chiave in binario : {bin(chiave)[2:57]}")
    return bin(chiave)[:57]


def mess64bit(string): #ritorna il messaggio diviso in parti da 64 bit ed il numero di zeri aggiunti all'ultimo pezzo
    stringa =""
    vett = []
    num_zeri_aggiunti = 0
    for a in string:
        stringa += bin(ord(a))[2:]
    
    while 1: 
        if len(stringa) % 64 == 0:
            break 
        stringa += "0"
        num_zeri_aggiunti += 1
        
    print(len(stringa)/64)
    print(stringa)
    for a in range(0,int(len(stringa)/64)):
        buffer =""
        for i in range (0,64):
            buffer += stringa[i+64*a]
        vett.append(buffer)

    return vett, num_zeri_aggiunti

def dividi_parti_uguali(stringa,num_per_parte):
    vett = []
    for a in range(0,int(len(stringa)/num_per_parte)):
        
        buffer =""
        for i in range (0,num_per_parte):
            buffer += stringa[i+num_per_parte*a]
        vett.append(buffer)
    return vett

def permuta_mess(messaggio):
    def Convert(string): 
        list1=[] 
        list1[:0]=string 
        return list1 
    def trovato(valore,lista):
        ciao = False
        for a in range(0,len(lista)):
            if (lista[a] == valore):
                ciao = True
                break
        return ciao

    import random

    messaggio = "ciao"
    list_messaggio = Convert(messaggio)
    print(list_messaggio)
    lista_poss_val = []
    mess_permutato = []
    dizionario = {} #chiave = vecchia posizion, valore = posizione permutata
    for a in range(0,len(messaggio)):
        lista_poss_val.append(a)


    for a in range(0,len(messaggio)):
        rand = random.randint(0,len(list_messaggio)-1)

        while(1):
            if trovato(list_messaggio[rand],mess_permutato):
                rand = random.randint(0,len(list_messaggio)-1)
            else: 
                break

        dizionario.update({a:rand})
        valore = list_messaggio[rand]
        
        mess_permutato.append(valore)
    return mess_permutato,dizionario

def rotate(l, n):
    return l[n:] + l[:n]