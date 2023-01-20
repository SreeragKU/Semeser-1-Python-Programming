class publisher:
    def getpublisher(self):
        self.name=input("Enter the name of the publisher: ")
class book(publisher):
    def getbook(self):
        self.title=input("Enter the title of the book: ")
        self.author=input("Enter the name of the author: ")
class python(book):
    def getpython(self):
        self.price=input("Enter the price of the book: ")
        self.pages=int(input("Enter the number of pages: "))

    def printdetails(self):
        print("\nPublisher name: ",self.name,"\nBook title: ",self.title,"\nBook's author",self.author,"\nBook's price: ",self.price,"\mNo: of pages: ",self.pages)

b=python()
b.getpublisher()
b.getbook()
b.getpython()

