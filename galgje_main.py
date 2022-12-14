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

#Menu wordt geladen uit bestand menu.txt en de tekst wordt geretourneerd
def laadmenu():
    bestandsnaam = 'menu.txt'
    f = open(bestandsnaam, encoding="UTF-8")
    #lees het hele bestand
    menuregels = f.read()
    f.close()
    return menuregels

#Toon statistieken. Gebruik de historie uit een bestand
def laat_stats_zien():
    bestandsnaam = "galgje_statistieken.json"
    #Als er geen bestand is met statistieken, zeg dat dan
    if not path.exists(bestandsnaam):
            print("Er zijn nog geen statistieken bekend")    
    else:
        with open(bestandsnaam, "r") as file:
            print('──────────────────────────────────────────────────────────────────────────────────────────')
            #Toon elke key value waarde in het bestand
            for k, v in json.load(file).items():
                print(f"{k}: {v}")
            print('──────────────────────────────────────────────────────────────────────────────────────────')

def wait():         # Druk een toets om door te gaan
    m.getch()

#Functie om keuze 'interactief' te doen.
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
        print ('Er is een fout opgetreden in de functie "gebruiker_speelt_spel"')

#Functie om keuze 'computer speelt spel' te doen
def computer_speelt_spel(puzzelwoorden:Puzzelwoorden):
    #statistieken worden hiervoor bijgehouden
    stats = GalgjeStatistics()
    aantal = int(input('  Hoeveel spelletjes wil je spelen? '))
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    #Een lus om het precieze aantal spelletjes uit te laten voeren door de computer
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
            print ('Er is een fout opgetreden in de functie "computer_speelt_spel"')

def clear():            # define our clear function
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#Dit is de functie om het menu daadwerkelijk te tonen en uit te voeren.
#parameters zijn: puzzelwoorden en een instantie van GalgjeVisualizer.
#De laatste zorgt voor het tonen van een galg
def menu(puzzelwoorden:Puzzelwoorden, visualizer:GalgjeVisualizer):   
    menu = laadmenu()
    #oneindige loop
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
            print(f'{Style.RESET_ALL}')
            #Stap uit de 'oneindige' loop
            break
        else:
            print('  Ongeldige keuze, probeer het nogmaals...')
            time.sleep(2)

#Maak instantie van Puzzelwoorden
puzzelwoorden = Puzzelwoorden('woorden.txt')
#Maak instantie van GalgjeVisualizer
visualizer = GalgjeVisualizer()

#Toon Splash-screen
Splash('galgje.png', 5000).splashscreen()
#Start het menu
menu(puzzelwoorden,visualizer)