add_library("pdf")

def setup():
    global img
    global i
    size(198, 255)#, PDF, "eksportdoPDF.pdf") # skoda, że skalowanie nie zostało zastosowane
    beginRecord(PDF, "eksportdoPDF.pdf")
    img=loadImage("zdjecie1.jpg")
    imageMode(CENTER)
    image(img, width/2, height/2)
    
def draw():
    global img
    global i
    if (mousePressed == True):
        i = loadImage("okularki.png") # brakuje wyboru
        image(i, width/2, 117, 140, 70)
        endRecord()
        
#1,5p
