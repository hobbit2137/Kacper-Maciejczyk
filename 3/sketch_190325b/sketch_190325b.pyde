def setup():
    size(500, 500)
    background(100, 20, 20)
    fill(255)
    textSize(120)
    textAlign(CENTER)
    text("K", width/2-80, height/2)
    text("M", width/2+80, height/2)
    s = createShape()
    s.beginShape()
    s.fill(200, 202, 40)
    s.stroke(0)
    s.vertex(width/2-100, height/3*2)
    s.vertex(width/2-30, height/3*2-50)
    s.vertex(width/2, height/3*2)
    s.vertex(width/2+30, height/3*2+50)
    s.vertex(width/2-100, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, -240)
def draw():
    if (mousePressed == True): # nie miało być na kliknięcie, a zaznaczenie - najechanie myszą
        text("K", width/2-80, height/2)
        text("M", width/2+80, height/2)
        fill(24, 200, 200)
    else:
        fill(0)
    if keyPressed:
        if (keyCode == LEFT):
            fill(125)
            text("K", width/2-80, height/2)
            fill(255)
            text("M", width/2+80, height/2)
        if (keyCode == RIGHT):
            fill(125)
            text("M", width/2+80, height/2)
            fill(255)
            text("K", width/2-80, height/2)
        fill(0) # warunki obowiązują dopóki wytabowane, nie ma potrzeby ich powielania
        if key == 'k' or key == 'K':
            text("K", width/2-80, height/2)
        if key == 'm' or key == 'M':
            text("M", width/2+80, height/2)
            
# 1,5pkt
