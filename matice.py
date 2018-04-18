pismeno = 'X'
mezera = ' '

for cislo_radku in range(0,6):
    if cislo_radku == 0:
        for opakovani in range(0,6):
            print(pismeno, mezera, end='')
        print('\n')
    elif cislo_radku == 5:
        for opakovani in range(0,6):
            print(pismeno, mezera, end='')
        print('\n')
    else:
        for opakovani in range(0,6):
            if opakovani == 0:
                print(pismeno, mezera, end='')
            elif opakovani == 5:
                print(pismeno, mezera, end='')
            else:
                print(mezera, mezera, end='')
        print('\n')
    cislo_radku = cislo_radku+1
