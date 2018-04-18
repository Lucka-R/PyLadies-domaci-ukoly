pismeno = 'X'
mezera = ' '
jednotka = pismeno + mezera


for cislo_radku in range(0,6):
    if cislo_radku == 0:
        for opakovani in range(0,6):
            print(jednotka, end = '')
        print('\n')
    elif cislo_radku == 5:
        for opakovani in range(0,6):
            print(jednotka, end='')
        print('\n')
    else:
        for opakovani in range(0,6):
            if opakovani == 0:
                print(jednotka, end='')
            elif opakovani == 5:
                print(jednotka, end='')
            else:
                print(mezera*2, end='')
        print('\n')
    cislo_radku = cislo_radku+1

