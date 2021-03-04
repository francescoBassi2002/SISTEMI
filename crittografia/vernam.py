lista_alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def cifraMessaggio(messaggio):
    
    
    messaggio_cifrato = ""
    carattere_separatore=""
    a=0
    z=0

    for c in range(0, len(messaggio)):
        for n in lista_alfabeto:
            if(n==messaggio[a]):
                if(c!=len(messaggio)-1):
                    carattere_separatore="_"
                else:
                    carattere_separatore=""

                messaggio_cifrato=messaggio_cifrato+str(z)+carattere_separatore

                a=a+1
                z=0
                break
            z=z+1

    return messaggio_cifrato




contenuto = input("Inserire il contenuto: ")

chiave = input("Inserire la chiave (più lunga del contenuto): ")

#da lettere a numeri
contenuto_cifrato= cifraMessaggio(contenuto)
print(f"{contenuto} = {contenuto_cifrato}")

chiave_cifrata = cifraMessaggio(chiave)
print(f"{chiave} = {chiave_cifrata}")

chiave_cifrata_int = chiave_cifrata.split("_")
contenuto_cifrato_int = contenuto_cifrato.split("_")

#trasformazione in interi
for a in range (0, len(chiave_cifrata_int)):
    chiave_cifrata_int[a]= int(chiave_cifrata_int[a])

for a in range(0, len(contenuto_cifrato_int)):
    contenuto_cifrato_int[a]=int(contenuto_cifrato_int[a])

#messaggio codificato finale
messaggioIntero = []
for x in range (0, len(contenuto)):
    messaggioIntero.append((chiave_cifrata_int[x] + contenuto_cifrato_int[x])%26)

print(f"Messaggio intero numeri interi con mod 26 applicato: {messaggioIntero}")

messaggio_finale = []

for x in range (0, len(messaggioIntero)):
    messaggio_finale.append(lista_alfabeto[messaggioIntero[x]])


print(f"messaggio finale codificato: {messaggio_finale}")