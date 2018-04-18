cislo = int(input('Zadej číslo:'))
faktorial = 1

if cislo < 0:
    print ('Faktoriál záporného čísla neexistuje')
if cislo == 0:
    print ('Faktoriál nuly je 1')
else:
    for cislo in range (1,cislo+1):
        faktorial = faktorial * cislo
        cislo = cislo + 1
    print (faktorial)
