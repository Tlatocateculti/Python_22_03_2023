def znajdzliczbe(parametr, start=0):
    wyjscie = ''
# tablica  - 10 znaków
#len(tablica) - 10
#tablica[0], tablica[1], tablica[2]...tablica[9]
    for ltmp in range(start,len(parametr)):
    #for litera in parametr:
        # jeżeli ilość znaków w wyjscie będzie większa od zera
        #ORAZ
        # ZANEGOWANE DZIAŁANIE!
        # litera będzie w przedziale 0..9
        # LUB litera będzie toższama z , lub .
        # LUB litera będzie znakiem -
        
        litera = parametr[ltmp]
        if len(wyjscie) > 0 and (litera >= '0' and
         litera <= '9' or
         (litera==',' or litera=='.') or 
         litera=='-')==False:
            break
        start+=1
        if litera >= '0' and litera <= '9':
            wyjscie+=litera
        if litera == '-' and len(wyjscie)==0:
            wyjscie+=litera
        if (litera == ',' or litera =='.') and len(wyjscie) > 0:
            wyjscie+='.'
    if len(wyjscie)==0:
         wyjscie='0'
    if (wyjscie.find('.')==-1):
         wyjscie=int(wyjscie)
    else:
         wyjscie=float(wyjscie)
    return (start if wyjscie!=0 else -1, wyjscie)        
    #print("Jestem w funkcji",wyjscie)


#ciag = input("Podaj dowolny ciąg znakowy: ")
ciag = 'To -8.5 jest 24 tekst w tym 11 tygodniu przy temperaturzr -7,2 ff'
wynik = []
s = 0
while True:
    #print(s,ciag)
    tmp = znajdzliczbe(ciag,s)
    #print(tmp)
    if (tmp[0]!=-1):
        wynik.append(tmp)
        s=tmp[0]
        continue
    break
    #s=tmp[0]
print(wynik)
#To jest 24 tekst w tym 11 tygodniu przy temperaturzr -7,2
