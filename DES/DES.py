
from funzioni import *


def DES (messaggio,chiave):

    def generaChiave(chiave, shift):
        def Convert(string): 
            list1=[] 
            list1[:0]=string 
            return list1 

        chiave = Convert(chiave)
        for a in range(0,8):
            chiave.pop((7+8*a)-a)
        
        vett = dividi_parti_uguali(chiave,len(chiave)/2)
        SX = vett[0]
        DX = vett[1]
        rotate(SX,shift)
        rotate(DX,shift)
        











    mess_permutato, dizionario = permuta_mess(messaggio)
    vett=dividi_parti_uguali(mess_permutato,32)
    SX = vett[0]
    DX = vett[1]
    for a in range(0,16):
        if(a+1 == 1 or a+1 == 2 or a+1 == 9 or a+1 == 16):
            shift_l = 1
        elif(a+1 == 3 or a+1 == 4 or a+1 == 5 or a+1 == 6 or a+1 == 7 or a+1 == 8 or a+1 == 10 or a+1 == 11 or a+1 == 12 or a+1 == 13 or a+1 == 14 or a+1 == 15):
            shift_l = 2
        sottochiave = generaChiave(chiave, shift_l)
        new_sx = DX
        new_dx = operazione_destra()
        


    

vettore,zero_agg=mess64bit("ciaocomestai")




