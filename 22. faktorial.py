cislo = int(input('Zadej číslo:'))
faktorial = 1

for cislo in range (1,cislo+1):
    faktorial = faktorial * cislo
    cislo = cislo + 1
    print (faktorial)
