def setup():

    global img
    size(1200/2, 1600/2) 

def draw():
 
    global img
    img = loadImage("pionkidart.jpg")
    

    image(img, 50,100, 500,500) 

    try:
 
        f = open("pionkidart.jpg")
        if f.name == 'pionkidart.jpg':
            raise Exception


    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print ("Error!")
        rect(20, 75,555,555)
        fill (255,0,0,90)
    
    else:
        rect(20, 75,555,555)
        fill (0,0,255,90)

               

    

    
