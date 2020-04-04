def setup():
    size(600, 600)
    global natezenie
    natezenie = 0
    global index
    index = 0
    frameRate(8)
    global szerokosc
    szerokosc = 0
    global wysokosc
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
    slownik = {"czerwony":(255, 0, 0), "niebieski":(0, 0, 255), "zielony":(0, 255, 0)}
    print(slownik["zielony"])
    fill(*slownik["zielony"])
    lista = []
    global index
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    index += 1
    if index==3:
        index = 0
def mousePressed():
    exit()
