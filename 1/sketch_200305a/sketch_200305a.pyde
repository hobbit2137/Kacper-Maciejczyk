def setup():
    size(800,800)
    background(204,20,40)
def draw():
    line(mouseX,mouseY,width/2,height/2) # tam gdzie się da lepiej używać zmiennych zależnych
    print(mouseX,mouseY,mousePressed)
    rect(80,70,100,100)
    if mousePressed:
        rect(width/2,height/2,300,300)
        rect(width/8,height/16,width/8,height/8)
        line(width/2,height,width/2,height/2)
        circle(width/2,width/2,150)
    else:
        rect(550,width/2,100,100) # ten kwadrat jest przysłaniany po kliknięciu myszy więc nie ma sensu aby był rysowany w klatce gdzie następuje jej kliknięcie - optymalizacja poprzez mniej akcji dla programu, a ten sam efekt
    
# 1,75 pkt
