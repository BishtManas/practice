class book :
    def __init__(self):
        self.name = input ("what is your book name : ")
        self.author = input ("what's the author name : ")
        self.pages = input ("how many pages in this book : ")
        
    def books(self):
        print (f"book details -->\nBook name : {self.name}\nAuthor name :{self.author}\nPages : {self.pages}")
obj = book ()
obj.books()
        
        