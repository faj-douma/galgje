import unittest
from puzzelwoorden_class import Puzzelwoorden
from galgje_api_class import GalgjeApi
from galgje_class import Galgje

#Unit test voor class Puzzelwoorden
class TestPuzzelwoorden(unittest.TestCase):

    #Test of het maken van het object Puzzelwoorden lukt
    def test_aanmaken(self):
        pw = Puzzelwoorden('woorden.txt')
        self.assertIsNotNone(pw)

    #Test of het masker en de letterhistorie een lijst met items oplevert
    def test_lijstvoldoetaanmasker(self):
        pw = Puzzelwoorden('woorden.txt')
        lijst = pw.lijst_voldoet_aan_masker('ri___en','enri')
        #check of lijst is gevuld 
        self.assertTrue(len(lijst)>0)

    #Test of bij de huidige woordenlijst de meest voorkomende letter een t is bij het gegeven masker en de gegeven letterhistorie
    def test_meest_voorkomende_letter(self):
        pw = Puzzelwoorden('woorden.txt')
        letter = pw.meest_voorkomende_letter('__a____ee_', 'ae')
        #Met bovenstaand masker en letterhistorie moet de letter t naar voren komen
        self.assertTrue(letter=='t')

#Unittest voor de class GalgjeApi
class TestGalgjeApi(unittest.TestCase):

    #Test het creëren van het object
    def test_aanroepAPI(self):
        api = GalgjeApi()
        #Bij een succesvolle creatie van het object met class GalgjeApi is moet er een pincode >= 0 zijn
        self.assertTrue(api.pincode >= 0)

    #Test de functie raadletter in object
    def test_raadletter(self):
        api = GalgjeApi()
        response = api.raadletter('e')
        self.assertTrue(response.status == 'succes')

    #Test de functie raadwoord in object
    def test_raadwoord(self):
        api = GalgjeApi()
        #Kies een niet bestaand woord. Ook deze aanroep moet succesvol zijn
        response = api.raadwoord('xxxxxxxx')
        self.assertTrue(response.status == 'succes')       

#Unittest voor class Galgje 
class TestGalgje(unittest.TestCase):

    #Test het aanmaken van object Galgje en de functie run
    def test_galgje(self):
        pw = Puzzelwoorden('woorden.txt')
        galgje = Galgje(pw)
        galgje.verbose = False
        self.assertIsNotNone(galgje)
        galgje.run()
        self.assertTrue(len(galgje.resultaat)>0)        



if __name__ == '__main__':
    unittest.main()