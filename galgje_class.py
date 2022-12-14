# Importeer de benodigde functies uit de diverse classes
from galgje_api_class import APIresponse, GalgjeApi #Class die de communicatie met de webserver doet
from puzzelwoorden_class import Puzzelwoorden #Classe voor het aanmaken van de puzzelwoorden
from galgje_visualizer_class import GalgjeVisualizer #Class voor het visueel weergeven van het Galgje mannetje
import timeit #module om verstreken tijd te meten tijdens het spelen van Galgje
import re #Module om reguliere expressies toe te passen

class Galgje:

    pincode = 0 # Initieer de variable met 0
    api:GalgjeApi = None # wordt geinitieerd later
    verbose = True #Zet op False om geen verbose logging op het scherm te zien (zie __printregel)
    puzzelwoorden:Puzzelwoorden = None # Aanmaken van een lege variable
    letterhistorie='' # Aanmaken van een lege variable
    teradenwoord = '' # Aanmaken van een lege variable
    resultaat = '' # Aanmaken van een lege variable
    totaltime_run = 0.0 # Aanmaken van een lege variable
    totaltime_requests = 0.0 # Aanmaken van een lege variable
    aantalpogingen = -1 # We beginnen met -1; het aantal pogingen om het woord te raden

    def __init__(self, puzzelwoorden):  #initialisatie van de API
            self.api = GalgjeApi()
            self.pincode = self.api.pincode
            self.teradenwoord = self.api.teradenwoord
            self.puzzelwoorden = puzzelwoorden

    def __printregel(self,str): #Functie die de regels tekst op het scherm tonen aan gebruiker.
        if self.verbose: # Alleen regels op het scherm wanneer verbose = True gezet is.
            print(str)
    
    def run(self):  # functie voor het automatisch oplossen door computer
        starttime = timeit.default_timer()  #start de timer op de "starttijd"
        self.__printregel("NIEUW SPEL\nTe raden woord is: " + self.teradenwoord + ' met een lengte van ' + str(len(self.teradenwoord)) + ' karakters')
        geraden = False
        while True:
            teradenletter = self.puzzelwoorden.meest_voorkomende_letter(self.teradenwoord, self.letterhistorie) #op basis van o.a. de meest voorkomende letter en de reeds gekozen letter, kiezen we de te raden letter
            self.letterhistorie = self.letterhistorie + teradenletter # update van de variable met de gekozen letter
            self.__printregel('Ik kies letter: "' + teradenletter + '"')  # op het scherm de gekozen letter tonen

            response = self.api.raadletter(teradenletter)  #antwoord van de API
            self.teradenwoord = response.geradenletters
            self.aantalpogingen = response.pogingen
            self.__printregel(response.spelstatus + ' ' + self.teradenwoord + ' #pogingen over: ' + str(response.pogingen)) #scherm toont de pogingen die nog over zijn

            if response.pogingen == 0: # Op het moment dat er geen mogelijkheden meer zijn, stopt het spel
                self.__printregel("HELAAS, het woord is niet geraden")
                self.resultaat = 'NIET GERADEN: ' + self.teradenwoord
                self.__printregel(f"Woord dat geraden moest worden: {response.resultaat['woord dat geraden moest worden']}\n\n")
                break

            if self.teradenwoord.find('_') == -1:  # wanneer er nog een _ is maar het woord geraden is door computer.
                self.__printregel("YES! Geraden. Het woord was: " + self.teradenwoord)
                self.resultaat = 'GERADEN: ' + self.teradenwoord
                break
        self.totaltime_run = timeit.default_timer()-starttime #Nog wat informatie over oplostijd (totaal tijd)
        self.totaltime_requests = self.api.total_duration #nog wat extra informatie over de totaaltijd API calls
   
    def __vraag_letter(self):  #Functie om de gebruiker een letter te vragen
        while True:
            letter = input("Welke letter kies je? ") # gebruiker kiest een letter
            if len(letter)>0 and re.match(r'^[A-Za-z]+$', letter):  # Wanneer de ingevoerde waarde leeg is EN een alfanummeriek karakter bevat...
                return letter[0].lower()     # wordt het karater omgezet naar lowercase in de variabele letter.
            else:
                print('Ongeldige invoer...')    # bij ongeldige invoer verschijnt een foutmelding


    def interactief(self, galgjevisualizer:GalgjeVisualizer):
        starttime = timeit.default_timer()
        self.__printregel("NIEUW SPEL\nTe raden woord is: " + self.teradenwoord + ' met een lengte van ' + str(len(self.teradenwoord)) + ' karakters')
        geraden = False
        while True:

            teradenletter = self.__vraag_letter()  #Hier wordt naar de functie vraag_letter verwezen

            self.letterhistorie = self.letterhistorie + teradenletter # Bijhouden van de reeds gekozen letters op basis van te raden letter en historie
            response = self.api.raadletter(teradenletter) # letter doorsturen naar de API
            self.teradenwoord = response.geradenletters
            self.aantalpogingen = response.pogingen

            self.__printregel(galgjevisualizer.PrintGalgje(response.pogingen))
            self.__printregel(response.spelstatus + ' ' + self.teradenwoord + ' #pogingen over: ' + str(response.pogingen)) # Toon aan gebruiker de resterende pogingen

            if response.pogingen == 0:  #Wanneer het aantal pogingen 0 is is het woord niet geraden
                self.__printregel("HELAAS, het woord is niet geraden")
                self.resultaat = 'NIET GERADEN: ' + self.teradenwoord
                self.__printregel(f"Woord dat geraden moest worden: {response.resultaat['woord dat geraden moest worden']}\n\n")
                break

            if self.teradenwoord.find('_') == -1: # wanneer de gebruiker het woord raad terwijl er nog niet geraden letters over waren
                self.__printregel("YES! Geraden. Het woord was: " + self.teradenwoord)
                self.resultaat = 'GERADEN: ' + self.teradenwoord
                break
        self.totaltime_run = timeit.default_timer()-starttime #Nog wat informatie over oplostijd (totaal tijd)
        self.totaltime_requests = self.api.total_duration #nog wat extra informatie over de totaaltijd API calls