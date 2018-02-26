class Book(object):

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        print "a book has been created"

#special method comes into play when a atribute needs to assign
#for example __str__ is a special method
    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s" %(self.title,self.author,self.pages)

#another special method is __len__ to chech the leangth of the given Book

    def __len__(self):
        return self.pages
b = Book("python", "jay", 100)
print(len(b))
