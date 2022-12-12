from galgje_class import Galgje
from puzzelwoorden_class import Puzzelwoorden


pw = Puzzelwoorden('woorden.txt')

for i in range(100):
    try:
        g = Galgje(pw)
        g.verbose = False
        g.run()
        print ('#'+str(i)+': ' + g.resultaat)
        print (f'Oplosduur: {g.totaltime_run}, API-calls-duur: {g.totaltime_requests}')
    except:
        a = 1
    