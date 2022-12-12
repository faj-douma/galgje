from requests import request
from response_class import APIresponse
from datetime import datetime
import timeit

class GalgjeApi:

    __url = "http://beprek.nl/galgje"
    pincode = 0
    teradenwoord = ''
    total_duration = 0.0

    def __init__(self):
        response = self.__webvraag('?pin=nieuw')
        self.pincode = response.pin
        self.teradenwoord = response.geradenletters
        if response.pogingen != 10:
            raise Exception('Foutieve response')

    def __webvraag(self, parameters):                                   # Doe een http request met parameters
        starttime = timeit.default_timer()
        jsonresponse = request("GET", self.__url + parameters)
        self.total_duration += timeit.default_timer() - starttime
        return(APIresponse(jsonresponse))

    def raadletter (self,letter):
        response = self.__webvraag('?pin=' + str(self.pincode) + '&letter='+ letter)
        return(response)

    def raadwoord (self, woord):
        response = self.__webvraag('?pin=' + str(self.pincode) + '&woord='+ woord)
        return(response)
