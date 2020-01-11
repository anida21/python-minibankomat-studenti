class Student:
    def __init__(self, ime, pismeni=0, usmeni=0, prosjek=0):
        self.ime = ime

    def PostaviPis(self, b):
        self.pismeni = b

    def PostaviUsmeni(self, b):
        self.usmeni = b

    def Dajime(self):
        return self.ime

    def DajProsjek(self):
        return self.prosjek

    def PostaviProsjek(self, b):
        self.prosjek = b;


lista = [Student("Marko"), Student("Ahmed"), Student("Merisa")]
print("U listi se nalaze slijedeci studenti:")
for x in lista:
    c = x.Dajime()
    if x != lista[-1]:
        print("'" + x.Dajime() + "',", end=' ');
    else:
        print("'" + x.Dajime() + "'", end=' ');

print("\nDa li zelite unijeti jos nekog studenta? da/ne: ")

a = input()
while a == "da":
    print("Unesite ime studenta:")
    b = input()
    lista.append(Student(b));
    print("Da li zelite unijeti jos nekog studenta? da/ne: ")
    a = input()

print("Nova lista studenta je sada:")

for x in lista:
    c = x.Dajime()
    if x != lista[-1]:
        print("'" + x.Dajime() + "',", end=' ');
    else:
        print("'" + x.Dajime() + "'", end=' ');

print();
dict = {
    "pismeni": int(0),
    "usmeni": int(0),
    "konacni": float(0)
}
for x in lista:
    print("Unesite ocjene koju je student " + x.Dajime() + " ostvario na pismenom ispitu:", end='')
    b = int(input())
    while b < 5 or b > 10:
        print("Morate unijeti broj od 5-10 za vrijednost ocjene")
        print("Unesite ocjene koju je student " + x.Dajime() + " ostvario na pismenom ispitu:", end='')
        b = int(input())

    dict["pismeni"] = b;

    print("Unesite ocjenu koju je student " + x.Dajime() + " ostvario na usmenom ispitu:", end='')
    b = int(input())
    while b < 5 or b > 10:
        print("Morate unijeti broj od 5-10 za vrijednost ocjene")
        print("Unesite ocjene koju je student " + x.Dajime() + " ostvario na pismenom ispitu:", end='')
        b = int(input())

    dict["usmeni"] = b;

    if dict["pismeni"] > 5 and dict["usmeni"] > 5:
        dict["konacni"] = float((dict["pismeni"] + dict["usmeni"]) / 2)
    else:
        dict["konacni"] = 5

    x.PostaviPis(dict["pismeni"])
    x.PostaviUsmeni(dict["usmeni"])
    x.PostaviProsjek(dict["konacni"])

for x in lista:
    print(x.Dajime() + " : " + str(x.DajProsjek()))