from random import randrange

pole = '--------------------'
policko = ''
znak = ''
vyhra = '-'

while vyhra == '-':
    def tah_hrace(pole, policko, znak):
    #Zažádá hráče o číslo políčka, vyhodnotí správnost čísla a zda políčko není plné
    #Pokud je, požádá o input znovu
    #pokud není, zaznamená tah
        policko=int(input('Na které políčko chceš hrát? Zadej číslo od 0 do ' + str(len(pole)-1) + '\n' ))
        znak='x'
        while policko not in range(0,len(pole)):
            print('Neplatné číslo políčka. Zadej číslo od 0 do '+str(len(pole)-1))
            policko=int(input('Na které políčko chceš hrát?'))

        while pole[policko] != '-':
            print('Políčko uz je zabrané. Zkus jiné!')
            policko=int(input('Na které políčko chceš hrát? Zadej číslo od 0 do ' + str(len(pole)-1) + '\n' ))

        pole1 = pole[0:policko]
        pole2 = pole[policko+1:]
        pole = pole1 + znak + pole2
        return pole

    pole=tah_hrace(pole, policko, znak)

    print(pole)

    def vyhodnot_stav(pole):
    #Vyhodnocuje, kdo vyhrál po každém kole a je zároveň podmínkou pro WHILE
        if '-' not in pole:
            vyhra = '!'
        elif 'ooo' in pole:
            vyhra = 'o'
        elif 'xxx' in pole:
            vyhra = 'x'
        else:
            vyhra = '-'
        return vyhra

    vyhra = vyhodnot_stav(pole)
    if vyhra == '-':
        print('Teď hraje počítač')

        def tah_pocitace(pole):
        #Vygeneruje náhodné políčko, zkontoluje obsazenost a hraje
        #Kontroluje, zda nehraje na obsazené pole a pro info tiskne hlášku (lze ve finální verzi odstranit)
        #Strategicky se snaží o tři 'o' vedle sebe
            znak='o'
            policko=randrange(0,len(pole))
            while pole[policko] != '-':
                print('Počítač zahrál na plné pole, hraje znova')
                policko=randrange(0,len(pole))
            pole1 = pole[0:policko]
            pole2 = pole[policko+1:]
            pole = pole1 + znak + pole2
            return pole

        pole=tah_pocitace(pole)
        print (pole)

    vyhra = vyhodnot_stav(pole)

vyhra = vyhodnot_stav(pole)
#Tiskne hlášky o vítězství/prohře/remíze na konci hry
if vyhra == '!':
    print ('Remíza')
elif vyhra == 'x':
    print ('Vyhrál jsi!')
elif vyhra == 'o':
    print ('Vyhrál počítač!')
else:
    print ('Máš kód na houby a koukej si tam najít chybu') # kontrolní řádka :) neměla by správně nastat
