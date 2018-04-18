pocet_radku = int(input('Zadej počt řádků:'))
pismeno = 'X'
mezera = ' '
jednotka = pismeno + mezera

for cislo_radku in range(0,pocet_radku+1):
    if cislo_radku == 0 or cislo_radku == pocet_radku:
        for opakovani in range(0,pocet_radku+1):
            print(jednotka, end = '')
        print('\n')
    else:
        for opakovani in range(0,pocet_radku+1):
            if opakovani == 0 or opakovani == pocet_radku:
                print(jednotka, end='')
            else:
                print(mezera*2, end='')
        print('\n')
    cislo_radku = cislo_radku+1
