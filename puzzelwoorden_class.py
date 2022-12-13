import re, collections

class Puzzelwoorden:

    #Deze string bevat alle letters uit het alfabet op volgorde van hoe frequent deze voorkomen in alle woorden
    #van de Nederlandse taal. Taal is in ontwikkeling, dus is dit wel een benadering.
    gesorteerde_frequentiestring = "earnotilsdkgupmbhvcwfjzyxq"

    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam
        self.woordenlijst = self.__lees_bestand()
        self.woordentekst = '\n'.join(self.woordenlijst)

    def __lees_bestand(self):
        woordenlijst = []
        with open(self.bestandsnaam, 'r') as file:
            woordenlijst = file.readlines()
        return self.__opschonen_puzzelwoordenlijst(woordenlijst)

    def __opschonen_puzzelwoordenlijst(self, woordenlijst):
        restwoorden = []
        for woord in woordenlijst:
            woord = woord.strip().lower()
            if self.__voldoet_aan_alle_criteria(woord):
                restwoorden.append(woord)
        return restwoorden


    def __is_romeins_getal(self, woord):
        roman = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000,'iv':4,'ix':9,'xl':40,'xc':90,'cd':400,'cm':900}
        i = 0
        num = 0
        try:
            while i < len(woord):
                if i + 1 < len(woord) and woord[i:i + 2] in roman:
                    num += roman[woord[i:i + 2]] 
                    i += 2 
                else:
                    #print(i)
                    num += roman[woord[i]]
                    i += 1
            if num > 0:
                return True
            else:
                return False
        except:
            return False
    
    def __voldoet_aan_alle_criteria(self, woord = ''):
        voldoet = True
        if len(woord) < 4:
            voldoet = False
        elif len(woord) > 13:
            voldoet = False
        elif not woord.isascii():
            voldoet = False
        elif not woord.isalpha():
            voldoet = False
        elif self.__is_romeins_getal(woord):
            voldoet = False
        return voldoet


    #Haal alle woorden uit de totale woordenlijst die voldoen aan het masker, rekening houdend met de letterhistorie
    def lijst_voldoet_aan_masker(self, mask='', letterhistorie=''):
        retval = []
        regex_karakterselectie = '.'  # Dit karakter staat voor een willekeurig karakter in een string.

        if len(letterhistorie) > 0:
            # Als er een letterhistorie is, verandert het willekeurige karakter naar een willekeurig karakter met
            # uitzondering van de karakters in de letterhistorie
            regex_karakterselectie = '[^' + letterhistorie + ']' 

        # Het woordmasker wordt gebruikt om een reguliere expressie te maken om te zien of een woord voldoet aan het masker.
        mask = "^" + mask.replace("_",regex_karakterselectie) + "$"

        # re.findall doorzoekt de grote string met alle woorden om die woorden eruit te halen die voldoen aan het masker
        retval = re.findall(mask, self.woordentekst, flags=re.MULTILINE)
        return retval

    #Kies de meest voorkomende letter in de Nederlandse taal die niet in de letterhistorie voorkomt.
    def __letter_uit_frequentiestring(self, letterhistorie):

        for letter in self.gesorteerde_frequentiestring:
            if letterhistorie.find(letter) == -1:
                break

        return letter

    #zoek meest voorkomende letter in de woordenlijst waarbij de woorden geselecteerd
    #worden door een masker en waarbij de letterhistorie meegerekend wordt.
    def meest_voorkomende_letter(self, mask='', letterhistorie=''):
 
        retval = ''
        alleletters = []

        # Zet alle letters van woorden die voldoen aan het masker en de letters die niet voorkomen in de letterhistorie
        # in de lijst 'alleletters'
        for woord in self.lijst_voldoet_aan_masker(mask, letterhistorie):
            for letter in woord:
                if not letter in letterhistorie:
                    alleletters.append(letter)

        # maak een frequentietabel van alle voorkomende letters in alle gevonden woorden
        alleletters = collections.Counter(alleletters).most_common()
        
        # Kies de eerste letter uit de frequentietabel. Dat is de letter met de hoogste frequentie.
        # Mocht er een woord geraden moeten worden die NIET in de woordenlijst staat en er zijn geen letters meer over
        # om te kiezen, kies dan een gewone letter die het meest voorkomt. Rekening houdend met de letterhistorie.
        if len(alleletters) > 0:
            retval = alleletters[0][0]
        else:
            retval = self.__letter_uit_frequentiestring(letterhistorie)

        return retval



