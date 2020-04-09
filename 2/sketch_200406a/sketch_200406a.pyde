def setup():
    size(600, 600)
    global natezenie, index, szerokosc, wysokosc # można też w jednej linii
    natezenie = 0
    index = 0
    frameRate(8) # nie za wolno?
    szerokosc = 0
    wysokosc = 250
def draw():
    global natezenie
    natezenie = natezenie + 1
    if natezenie == 255:
        natezenie = 0
    fill(0, 0, natezenie, 120)
    rect(wysokosc, szerokosc, 100, 100)
    fill(0, natezenie, 0, 120)
    global wysokosc
    wysokosc = wysokosc + 1
    global szerokosc
    szerokosc = szerokosc + 1
    # poniższej zakomentowanej części kodu nie użyłeś, a nic wizualnie ona nie zmienia
    #slownik = {"czerwony":(255, 0, 0), "niebieski":(0, 0, 255), "zielony":(0, 255, 0)}
    #print(slownik["zielony"])
    #fill(*slownik["zielony"])
    #lista = []
    #global index
    #for nazwa, wartosc in slownik.items():
    #    lista.append(wartosc)
    #index += 1
    #if index==3:
    #    index = 0
def mousePressed():
    exit()
    
# 1,25p
