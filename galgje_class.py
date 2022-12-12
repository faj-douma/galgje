from galgje_api_class import APIresponse, GalgjeApi
from puzzelwoorden_class import Puzzelwoorden
import timeit

class Galgje:

    pincode = 0
    api:GalgjeApi = None
    verbose = True
    puzzelwoorden:Puzzelwoorden = None
    letterhistorie=''
    teradenwoord = ''
    resultaat = ''
    totaltime_run = 0.0
    totaltime_requests = 0.0

    def __init__(self, puzzelwoorden):
            self.api = GalgjeApi()
            self.teradenwoord = self.api.teradenwoord
            self.puzzelwoorden = puzzelwoorden

    def __printregel(self,str):
        if self.verbose:
            print(str)
    
    def run(self):
        starttime = timeit.default_timer()
        self.__printregel("NIEUW SPEL\nTe raden woord is: " + self.teradenwoord + ' met een lengte van ' + str(len(self.teradenwoord)) + ' karakters')
        geraden = False
        while True:
            teradenletter = self.puzzelwoorden.meest_voorkomende_letter(self.teradenwoord, self.letterhistorie)
            self.letterhistorie = self.letterhistorie + teradenletter
            self.__printregel('Ik kies letter: "' + teradenletter + '"')

            response = self.api.raadletter(teradenletter)
            self.teradenwoord = response.geradenletters

            self.__printregel(response.spelstatus + ' ' + self.teradenwoord + ' #pogingen over: ' + str(response.pogingen))

            if response.pogingen == 0:
                self.__printregel("HELAAS, het woord is niet geraden")
                self.resultaat = 'NIET GERADEN: ' + self.teradenwoord
                break

            if self.teradenwoord.find('_') == -1:
                self.__printregel("YES! Geraden. Het woord was: " + self.teradenwoord)
                self.resultaat = 'GERADEN: ' + self.teradenwoord
                break
        self.totaltime_run = timeit.default_timer()-starttime
        self.totaltime_requests = self.api.total_duration
   
      


