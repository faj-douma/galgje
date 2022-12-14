import os.path 
from os import path
from datetime import datetime
import json

class GalgjeStatistics:
     #Statistieken berekenen en als dictionary teruggeven
     def __calc__stats(self, dict, resultaat):
        totaalGespeeld = int(dict["totaalGespeeld"])
        aantalGewonnen = int(dict["aantalGewonnen"])
        aantalVerloren = int(dict["aantalVerloren"])
        if resultaat.split(":")[0] == "GERADEN" : 
            aantalGewonnen += 1
        else:
            aantalVerloren += 1
        totaalGespeeld += 1
        if totaalGespeeld > 0:
            winRatio = (aantalGewonnen/totaalGespeeld) * 100
        statsDict = { "totaalGespeeld" : totaalGespeeld, "aantalGewonnen": aantalGewonnen, "aantalVerloren" : aantalVerloren, "winratio" : winRatio, "LaatsteSpel" : str(datetime.now()) }
        return statsDict
    
     def Log_Statistics(self, resultaat):
        #initieel 
        bestandsnaam = "galgje_statistieken.json"
         #File laden in dictionary, indien niet bestaand de dictionary aanmaken
        if not path.exists(bestandsnaam):
            statsDict = { "totaalGespeeld" : 0, "aantalGewonnen": 0, "aantalVerloren" : 0, "winratio" : 0, "LaatsteSpel" : "" }    
        else:
            with open(bestandsnaam, "r") as file:
                statsDict = json.load(file)

        #Schrijf de logging naar json bestand
        with open(bestandsnaam, "w") as file:
            json.dump(self.__calc__stats(statsDict, resultaat), file)
        return None