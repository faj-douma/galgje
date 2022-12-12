import unittest
from puzzelwoorden_class import Puzzelwoorden
from galgje_api_class import GalgjeApi
from galgje_class import Galgje

class TestPuzzelwoorden(unittest.TestCase):

    #Test of het maken van het object Puzzelwoorden lukt
    def test_aanmaken(self):
        pw = Puzzelwoorden('woorden.txt')
        self.assertIsNotNone(pw)

    #Test of het masker en de letterhistorie een lijst met items oplevert
    def test_lijstvoldoetaanmasker(self):
        pw = Puzzelwoorden('woorden.txt')
        lijst = pw.lijst_voldoet_aan_masker('ri___en','enri') 
        self.assertTrue(len(lijst)>0)

    #Test of bij de huidige woordenlijst de meest voorkomende letter een t is bij het gegeven masker en de gegeven letterhistorie
    def test_meest_voorkomende_letter(self):
        pw = Puzzelwoorden('woorden.txt')
        letter = pw.meest_voorkomende_letter('__a____ee_', 'ae')
        self.assertTrue(letter=='t')

class TestGalgjeApi(unittest.TestCase):

    def test_aanroepAPI(self):
        api = GalgjeApi()
        self.assertTrue(api.pincode > 0)


    def test_raadletter(self):
        api = GalgjeApi()
        response = api.raadletter('e')
        self.assertTrue(response.status == 'succes')

    def test_raadwoord(self):
        api = GalgjeApi()
        response = api.raadwoord('xxxxxxxx')
        self.assertTrue(response.status == 'succes')       

class TestGalgje(unittest.TestCase):

    def test_galgje(self):
        pw = Puzzelwoorden('woorden.txt')
        galgje = Galgje(pw)
        galgje.verbose = False
        self.assertIsNotNone(galgje)
        galgje.run()
        self.assertTrue(len(galgje.resultaat)>0)        



if __name__ == '__main__':
    unittest.main()