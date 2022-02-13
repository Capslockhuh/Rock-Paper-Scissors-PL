import random, sys

print('PAPIER, KAMIEŃ, NOŻYCE')

#te zmienne będą liczyć wygrane, przegrane i remisy
wygrane = 0
przegrane = 0
remisy = 0

#główna pętla
while True:
    print('%s Wygrane, %s Przegrane, %s Remisy' % (wygrane, przegrane, remisy))
    while True: 
        print('Wybierz swój ruch: p - papier, k - kamień n - nożyce, z - zakończ')
        ruchGracza = input()
        if ruchGracza == 'z':
            print('Do zobaczenia!')
            sys.exit() #zakończ program jeśli gracz wybierze "z"
        if ruchGracza == 'p' or ruchGracza == 'k' or ruchGracza == 'n':
            break #wyjdź z pętli jeśli gracz wybierze swój ruch
        print('Wybierz: p, k, n lub z')
            
#wyświetl wybór gracza
    if ruchGracza == 'p':
        print('PAPIER kontra...')
    elif ruchGracza == 'k' :
        print('KAMIEŃ kontra...')
    elif ruchGracza == 'n':
        print('NOŻYCE kontra...')

#wyświetl wybór komputera
    losowyNumer = random.randint(1, 3)
    if losowyNumer == 1:
        ruchKomputera = 'k'
        print('KAMIEŃ')
    elif losowyNumer == 2:
          ruchKomputera = 'p'
          print('PAPIER')
    elif losowyNumer == 3:
          ruchKomputera = 'n'
          print('NOŻYCE')

#sprawdź kto wygrał
    if ruchGracza == ruchKomputera:
        print('REMIS!')
        remisy = remisy + 1
    elif ruchGracza == 'k' and ruchKomputera == 'n':
        print('Wygrałeś!')
        wygrane = wygrane + 1
    elif ruchGracza == 'p' and ruchKomputera == 'k':
        print('Wygrałeś!')
        wygrane = wygrane + 1
    elif ruchGracza == 'n' and ruchKomputera == 'p':
        print('Wygrałeś!')
        wygrane = wygrane + 1
    elif ruchGracza == 'k' and ruchKomputera == 'p':
        print('Przegrałeś!')
        przegrane = przegrane + 1
    elif ruchGracza == 'p' and ruchKomputera == 'n':
        print('Przegrałeś!')
        przegrane = przegrane + 1
    elif ruchGracza == 'n' and ruchKomputera == 'k':
        print('Przegrałeś!')
        przegrane = przegrane + 1
    



    
    
                        
            
