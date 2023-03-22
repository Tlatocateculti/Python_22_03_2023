dni_tygodnia = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
slownik = {"imie": "Mariola", "nazwisko" : "Kowalska", "wiek": 34}
print(dni_tygodnia[3])
dni=list(dni_tygodnia)
dni_tygodnia = None
dni[3] = "Nie wiem"
print(dni)
#slownik.update({"telefon": "666777888"})
s_klucze = slownik.keys()
print(slownik['nazwisko'])
print(s_klucze)
slownik['wiek']=24+3
slownik.update({"telefon": ["666777888", "778883344", "123456789"]})
print(s_klucze)
for klucz in s_klucze:
    print(klucz, ":", slownik[klucz])

"""
tab = []

while True:
    tab.append(int(input("Podaj liczbę, 0 kończy wprowadzanie: ")))
    if tab[-1] == 0:
        break

print(tab)
#del tab[3]
#del tab[3:]
del tab[:3]
print(tab)
    
#print(tab)
#print('::',tab[::])
#print(':3',tab[:3])
#print('::-1',tab[::-1])
#print(':-1',tab[:-1])
#print('3:',tab[3:])

tekst = input("Podaj dowolny tekst: ")
print("Tekst:",tekst,"posiada",len(tekst),"znaków")

#for z in range(0, 128):
#    print(z, chr(z))
"""

"""
print("Hej "*50)

a = 10
b = int(input("Podaj b: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)


#a,b = float(input("Podaj a: ")), float(input("Podaj b: "))
#print(a+b)
"""


"""
imie = input("Podaj swoje imię: ")
#print("Witaj,",imie,"!")
print(f"Witaj, {imie}!")
"""
