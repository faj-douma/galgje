# pip install Pillow

from tkinter import *
from PIL import ImageTk,Image

class Splash:                 # Lees plaatje in en toon dit in het midden van het scherm

    def __init__(self, bestand, timer):
        self.bestand = bestand
        self.timer = timer
    
    def splashscreen(self):
        root = Tk()
        plaatje = ImageTk.PhotoImage(Image.open(self.bestand))
        plaatje_width = plaatje.width()
        plaatje_height = plaatje.height()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width/2) - (plaatje_width/2))
        y = int((screen_height/2) - (plaatje_height/2) - 50) # iets boven midden plaatsen
        root.title('Galg_e')
        root.overrideredirect(True)     # Geen titelbalk
        root.geometry(f"{plaatje_width}x{plaatje_height}+{x}+{y}")
        label = Label(image=plaatje)
        label.pack()    
        root.after(self.timer, root.destroy)
        mainloop()

#Splash('c:/apps/python/galgje/sprint/galgje.png', 3000).splashscreen()