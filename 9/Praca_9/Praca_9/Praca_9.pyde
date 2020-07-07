def setup():

    global img
    size(1200/2, 1600/2)
    noFill()
    strokeWeight(10)

def draw():
 
    global img
    img = loadImage("pionkidart.jpg")
    
    try:
        image(img, 50,100, 500,500)
    except:
        print ("Error!")
        stroke (255,0,0,90)
    
    else:
        stroke (0,0,255,90)
    finally:
        rect(20, 75,555,555)    

#1,25pkt

    
