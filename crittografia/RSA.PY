import funzioni_varie

def cifra(messaggio , c , n):
    print(f"({messaggio}^{c}) mod {n}")
    return (messaggio**c) % n

def decifra(messaggio_cifrato , d , n):
    return (messaggio_cifrato**d) % n


messaggio_da_cifrare = int(input("Inserisci il messaggio da cifrare: "))


chiave_privata_p = int(input("Inserire numero primo: "))
chiave_privata_q = int(input("Inserire un altro numero primo: "))

chiave_pubblica_n = chiave_privata_p * chiave_privata_q

chiave_privata_m = int(funzioni_varie.mcm(chiave_privata_p - 1, chiave_privata_q - 1))

chiave_pubblica_c = funzioni_varie.rsa_calcolo_c(chiave_privata_m)

chiave_privata_d = funzioni_varie.rsa_calcolo_d(chiave_pubblica_c, chiave_privata_m)

print(f"le chiavi private sono: p {chiave_privata_p} , q {chiave_privata_q} , m {chiave_privata_m} , d {chiave_privata_d}")
print(f"le chiavi pubbliche sono: c {chiave_pubblica_c} , n {chiave_pubblica_n}")

messaggio_cifrato = cifra(messaggio_da_cifrare, chiave_pubblica_c, chiave_pubblica_n)

print(f"messaggio cifrato inviato: {messaggio_cifrato}")
print(f"messaggio decifrato ricevuto: {decifra(messaggio_cifrato, chiave_privata_d, chiave_pubblica_n)}")