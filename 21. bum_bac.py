for cislo in range (1,101):
    delitel3 = cislo % 3
    delitel5 = cislo % 5
    if delitel3 == 0 and delitel5 == 0:
        print ('bum-bác', ', ', sep='', end='')
    elif delitel5 == 0:
        print ('bác', ', ', sep='', end='')
    elif delitel3 == 0:
        print ('bum', ', ', sep='', end='')
    else:
        print (cislo,', ', sep='', end='')
    cislo=cislo+1

print('konec.')
