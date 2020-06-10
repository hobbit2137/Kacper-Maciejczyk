from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'

class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('miau miau', random(50, width-70), random(50, height-50))
        return 'miau miau'
    def gimmePaw(self):
        image(loadImage("tygrys.jpeg"), random(-250, width-10), random(-250, height-10))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass

class Fox(Pet):
     def __init__(self, name):
        self.name = name
     def speak(self):
        text('miska pusta', random(50, width-70), random(50, height-50))
        return 'miska pusta'
  
def setup():
    size(900,900)
    textSize(20)
    Puszek = Cat('Puszek')
    Rudy = Fox('Rudy')
    global list_of_pets
    list_of_pets = [Puszek, Rudy] 
    print(isinstance(Puszek, Pet))
    print(Puszek+Rudy)
   
def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Cat): 
            pet.gimmePaw()
