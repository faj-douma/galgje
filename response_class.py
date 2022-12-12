# Opbouw response van Galgje website
# {'status': 'succes', 'versie': 'alpha', 'resultaat': 
#   {'galgje pin': 24673, 'resterend pogingen': 8, 'spel status': 'Woord is gekozen en je hebt nog 8 pogingen', 'geraden letters': '_____'}
# }

import json

class APIresponse:
    #def __init__(self, status='', versie='', resultaat='', pin=0, pogingen=0, spelstatus='', geradenletters='', lengtewoord=0):

    status = ''
    versie = ''
    resultaat = ''
    pin = 0
    pogingen = 0
    spelstatus =  ''
    geradenletters = ''
    lengtewoord = 0

    def __init__(self, jsonresponse):
        self.status = jsonresponse.json()['status']
        self.versie = jsonresponse.json()['versie']
        self.resultaat = jsonresponse.json()['resultaat']
        self.pin = self.resultaat['galgje pin']
        self.pogingen = self.resultaat['resterend pogingen']
        self.spelstatus = self.resultaat['spel status']
        self.geradenletters = self.resultaat['geraden letters']
        self.lengtewoord = len(self.resultaat['geraden letters'])


    def __str__(self):
        print('Status = ' + self.status)
        print('Versie = ' + self.versie)
        print('Galgje pin: {}'.format(self.pin))
        print('Resterende pogingen: {}'.format(self.pogingen))
        print('Spel status: {}'.format(self.spelstatus))
        print('Geraden letters: {}'.format(self.geradenletters))
        print('Lengte van het woord: {} letters.'.format(self.lengtewoord))
        return



        