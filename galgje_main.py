from galgje_class import Galgje
from puzzelwoorden_class import Puzzelwoorden
from galgje_visualizer_class import GalgjeVisualizer
import time
from splash import Splash
from os import system, name
import msvcrt as m
from colorama import Fore, Style

def laadmenu():
    bestandsnaam = 'menu.txt'
    f = open(bestandsnaam, encoding="UTF-8")
    menuregels = f.read()
    f.close()
    return menuregels

def wait():         # Druk een toets om door te gaan
    m.getch()

def gebruiker_speelt_spel(puzzelwoorden:Puzzelwoorden, visualizer:GalgjeVisualizer):
    try:
        g = Galgje(puzzelwoorden)
        g.verbose = True
        g.interactief(visualizer)
        print ('SAMENVATTING:')
        print (f'Pin: {g.pincode}  {g.resultaat}')
        print (f'Oplosduur: {g.totaltime_run}, API-calls-duur: {g.totaltime_requests}, Aantal pogingen over: {g.aantalpogingen}')
        print ('──────────────────────────────────────────────────────────────────────────────────────────')
    except:
        print ('Kon geen instantie van Galgje maken...')

def computer_speelt_spel(puzzelwoorden:Puzzelwoorden):
    aantal = int(input('  Hoeveel spelletjes wil je spelen? '))
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    for i in range(aantal):
        try:
            g = Galgje(puzzelwoorden)
            g.verbose = False
            g.run()
            print (f'#{str(i)}: Pin: {g.pincode}  {g.resultaat}')
            print (f'Oplosduur: {g.totaltime_run}, API-calls-duur: {g.totaltime_requests}, Aantal pogingen over: {g.aantalpogingen}')
            print ('──────────────────────────────────────────────────────────────────────────────────────────')
            
        except:
            print ('Kon geen instantie van Galgje maken...')

def clear():            # define our clear function
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def menu(puzzelwoorden:Puzzelwoorden, visualizer:GalgjeVisualizer):   
    menu = laadmenu()
    while True:
        clear()
        print(f'\n{Fore.GREEN}{menu}')
        keuze = input('                      ')
        if keuze == '1':
            gebruiker_speelt_spel(puzzelwoorden,visualizer)
            print('  druk een willekeurige toets om terug te keren naar het menu')
            wait()
        elif keuze == '2':
            computer_speelt_spel(puzzelwoorden)
            print('  druk een willekeurige toets om terug te keren naar het menu')
            wait()
        elif keuze == '3':
            stop = True
            print(f'{Style.RESET_ALL}')
            break
        else:
            print('  Ongeldige keuze, probeer het nogmaals...')
            time.sleep(2)

puzzelwoorden = Puzzelwoorden('woorden.txt')
visualizer = GalgjeVisualizer()

#Splash('galgje.png', 5000).splashscreen()
menu(puzzelwoorden,visualizer)