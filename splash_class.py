# pip install Pillow

from tkinter import *
from PIL import ImageTk,Image

class Splash:                 # Lees plaatje in en toon dit in het midden van het scherm

    #Het object wordt geconstrueerd met een bestandsnaam en een tijd.
    def __init__(self, bestand, timer):
        self.bestand = bestand
        self.timer = timer

    #Deze functie toont het plaatje uit de bestandsnaam    
    def splashscreen(self):
        #root wordt een instantie van de class Tk. Dat is het tekenbord
        root = Tk()
        plaatje = ImageTk.PhotoImage(Image.open(self.bestand))
        plaatje_width = plaatje.width()
        plaatje_height = plaatje.height()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        #Bepaal de coördinaten van het plaatje op het scherm door de dimensies van het scherm te gebruiken
        x = int((screen_width/2) - (plaatje_width/2))
        y = int((screen_height/2) - (plaatje_height/2) - 50) # iets boven midden plaatsen
        root.title('Galg_e')
        root.overrideredirect(True)     # Geen titelbalk
        root.geometry(f"{plaatje_width}x{plaatje_height}+{x}+{y}")
        label = Label(image=plaatje)
        label.pack()    
        #Stel een functie in om uit te voeren na verloop van de tijd. In dit geval...gooi het tekenbord weg.
        root.after(self.timer, root.destroy)
        mainloop()
#Test
#Splash('rudi.png', 3000).splashscreen()
