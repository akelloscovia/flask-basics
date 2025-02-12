#company class
class Company:
    #Contructor
    def _init_(self,name,email,contact):
        self.name = name
        self.email = email
        self.contact = contact
        
        #new instance
        company_one = Company('scovia','akelloscovia907@gmail.com',7807407490)
        print(company_one)
        
        #ass
        #complete author and book classes
        #atleast 5 properties  and functions.
        
class Author:
    def __init__(self, name, birth_year, Age, contact, nationality):
        self.name = name
        self.birth_year = birth_year
        self.Age = Age
        self.contact = contact
        self.nationality = nationality
        self.books = []

    def __str__(self):
        return f"{self.name} ({self.birth_year}, {self.Age}, {self.contact} ,{self.nationality})"
author_details = Author("Chinua Achebe", 1925,"100","achebe101@gmail.com","Naigerian")
print(author_details)
class Book:
    def __init__(self, title, publication_year, author, language, edition):
        self.title = title
        self.publication_year = publication_year
        self.author = author
        self.language = language
        self.edition = edition
    

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year} ,{self.language},{self.edition})"
book_details= Book("Things fall apart","Chinua Achebe","1990","English","8th edition")
print(book_details)