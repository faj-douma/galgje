import json
from galgje_class import Galgje
from galgje_statistics_class import GalgjeStatistics
from puzzelwoorden_class import Puzzelwoorden
from galgje_visualizer_class import GalgjeVisualizer
import time
from splash_class import Splash
from os import path, system, name
import msvcrt as m
from colorama import Fore, Style

def laadmenu():
    bestandsnaam = 'menu.txt'
    f = open(bestandsnaam, encoding="UTF-8")
    menuregels = f.read()
    f.close()
    return menuregels

def laat_stats_zien():
    bestandsnaam = "galgje_statistieken.json"
    if not path.exists(bestandsnaam):
            print("Er zijn nog geen statistieken bekend")    
    else:
        with open(bestandsnaam, "r") as file:
            print('──────────────────────────────────────────────────────────────────────────────────────────')
            for k, v in json.load(file).items():
                print(f"{k}: {v}")
            print('──────────────────────────────────────────────────────────────────────────────────────────')

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
    stats = GalgjeStatistics()
    aantal = int(input('  Hoeveel spelletjes wil je spelen? '))
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    for i in range(aantal):
        try:
            g = Galgje(puzzelwoorden)
            g.verbose = False
            g.run()
            stats.Log_Statistics(g.resultaat)
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
            laat_stats_zien()
            print('  druk een willekeurige toets om terug te keren naar het menu')
            wait()
        elif keuze == '4':
            stop = True
            print(f'{Style.RESET_ALL}')
            break
        else:
            print('  Ongeldige keuze, probeer het nogmaals...')
            time.sleep(2)

puzzelwoorden = Puzzelwoorden('woorden.txt')
visualizer = GalgjeVisualizer()

Splash('galgje.png', 5000).splashscreen()
menu(puzzelwoorden,visualizer)