class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
        
def setup():
    size(220,100)
    global library, Anna, Kacper
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Koralina"]
    library = Library(books) 
    Anna = Customer()
    Kacper = Customer() # klasy są po to, żeby łatwo i szybko tworzyć wiele obiektów o rozbudowanej funkcjonalności
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Anna.requestBook("Naocznosc"))
            library.lendBook(Kacper.requestBook("Koralina")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Anna.returnBook())
            library.addBook(Kacper.returnBook()) # powielanie tych samych warunków to również zła praktyka

#0,25/0,5pkt za tę część        
