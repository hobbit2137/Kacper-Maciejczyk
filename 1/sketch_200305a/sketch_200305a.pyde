def setup():
    size(800,800)
    background(204,20,40)
def draw():
    line(mouseX,mouseY,400,400)
    print(mouseX,mouseY,mousePressed)
    rect(80,70,100,100)
    rect(550,400,100,100)
    if mousePressed:
        rect(width/2,height/2,300,300)
        rect(100,50,100,100)
        line(400,800,400,400)
        circle(400,400,150)
    
    
