# -*- coding: utf-8 -*-
from datetime import datetime,timedelta

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        
class Member(User):
    
    books_collected={}
    fine=0
    
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,catalog,name,isbn,days=10):
        flag=catalog.searchByName(name)
        if (flag.searchBookItem(isbn) ):
            catalog.removeBookItem(name,isbn)
            self.issue_date = datetime.now()
            self.due_date = datetime.now()+timedelta(days)
            self.books_collected[name] = [self.issue_date,self.due_date]
            print("Issued Date: ",self.issue_date.strftime("%d-%m-%y @ %H:%M"))
            print("Due date: ",self.due_date.strftime('%d-%m-%y '))
        
        else:
            print('item not in stock')
            
    #assume name is unique
    def returnBook(self,catalog,name,isbn):
        book=catalog.searchByName(name)
        rack=input("Enter Rack No.:")
        catalog.addBookItem(book,isbn,rack)
        return_date=datetime.now().date()
        due= self.books_collected[name][1].date()
        self.days_elapsed = return_date - due
        
        
        if return_date > due:
            self.fine+=(self.days_elapsed.days)*2.0
        if self.fine > 0:        
            print("fine to be paid:",self.fine)
            inp= input('is the amount paid(Y/N):') 
            if inp=="Y":
                    self.fine=0
        print("fine to be paid:",self.fine)        
        del self.books_collected[name]
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name +' ' + self.location +' ' + self.emp_id
    
    def addBook(self,catalog,name,author,publish_date,pages):
        b=catalog.addBook(name,author,publish_date,pages)
        return(b)
        
        
    def removeBook(self,catalog,name):
        book=catalog.searchByName(name)
        if book in catalog.books:
            catalog.different_book_count -= 1
            catalog.books.remove(book)
            
    
    def removeBookItemFromCatalog(self,catalog,book,isbn):
        for b in catalog.books:
            if book.strip()==b.__repr__():
                catalog.removeBookItem(b.name,isbn)
            
            
        
    
    
        