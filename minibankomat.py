#zadatak s ispita

rjecnik1={"ime":"nezir","sifra":18006,"pocetnaSnovca":50}
lista1=["polaganje novca","podizanje novca", "pregled stanja racuna", "izmjena sifre"]
print(rjecnik1,lista1)

def polaganjenovca():
    pocetnaSnovca=rjecnik1["pocetnaSnovca"]
    sumanovca=int(input("unesite koliko novca zelite upaltit na vas racun"))
    sumanovaca=pocetnaSnovca+sumanovca
    print("uplata je uspjesna, suma novca na vasem racunu inosi",sumanovaca)
    rjecnik1["pocetnaSnovca"]=sumanovaca

def podizanjenovca():
    novac=int(input("uensite koliko novca zelite podic"))
    pocetnaSnovca = int(input("unesite pocetnu sumu novca"))
    if novac>pocetnaSnovca:
        print("nemate dovoljno sredstava na racunu")
        pitanje=input("zelite li ponovno unijetu manju kolicinu novca")
        if pitanje=="DA" or pitanje=="da":
            novac = int(input("uensite koliko novca zelite podic"))
        else:
            print("zahvaljujemo sto ste koristili nase usluge")
    elif novac<pocetnaSnovca:
        print("vasa transakcija e uspjesno obavljena")
        pocetnasnovca=pocetnaSnovca-novac
        print("preostala sredstva na vasem racunu su", pocetnasnovca,"preuzmite vasu karticu")
        pitanje2=("zelite li drugu transakciju")
        if pitanje2=="DA" or pitanje2=="da":
            novac = int(input("uensite koliko novca zelite podic"))
        else:
            print("hvala sto ste koristili nase usluge")
        rjecnik1["pocetnaSnovca"]=pocetnasnovca
def izmjenasifre(sifra,novasifra):
    sifra=rjecnik1["sifra"]
    novasifra=input("uensite nouv sifru ponovno")
    print("Vaša nova sifra je", novasifra)
    rjecnik1["sifra"]=novasifra
sifra=input("unesite vasu sifru")
if sifra=="18006":
    print("unijeli ste tacnu sofru, odaberite jednu od sljedencih opcija")
else:
    print("sifra nije tocna")
    piitanje=input("zelite li unijeti sifru ponovno")
    if piitanje == "DA" or piitanje == "da":
        sifra = int(input("ponovno unesite sifru"))
    else:
        print("zahvaljujemo sto ste koristili nase usluge")

print("ponudjene opcije su: podizanje novca polaganje novca  provjera stanja racuna, promjena sifre")
opcija=input("unesite zeljenu opciju ")

if opcija=="podizanje novca":
    podizanjenovca()
    novac=int(input("uensirte koliko novca zelite podic"))
    print(rjecnik1)
elif opcija=="polaganje novca":
    polaganjenovca()
    print(rjecnik1)
elif opcija=="promjena sifre":
    novasifra=input("unesite novu sifru")
    izmjenasifre(sifra,novasifra)
    print(rjecnik1)
