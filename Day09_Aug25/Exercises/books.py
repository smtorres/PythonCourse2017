# book_table
# title					author_id		main_character				year
# "War and Peace"			1			"Pierre Bezukhov"			1869
# "Anna Karenina"			1			"Anna Karenina"				1877
# "Tale of Two Cities"      2			"Alexandre Manette"			1859
# "Crime and Punishment"	3			"Raskolnikov"				1866
 
# author_table
# author_id				author_name			country_id
# 1						Tolstoy				1
# 2						Dickens				2
# 3						Dostoevsky			1
# 4						Darwin				1
 
# country_table
# country_id				country_name			capital
# 1							Russia					Moscow
# 2							England					London

import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Some info about sqlalchemy
print sqlalchemy.__version__

#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/michelletorres/Desktop/books.db', echo=True)

Base = declarative_base() 

#Define some schemas
class Book(Base):
    __tablename__ = 'books'
#   __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    main_character = Column(String)
    year = Column(Integer)
    
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    def __init__(self, name, main_character=None, year=None):
      self.name = name
      self.main_character = main_character
      self.year = year
      
    def __repr__(self):
    	if self.author: return "<Book(%s by %s)>" % (self.name, self.author.name)
  	return "<Book(%s)>" %(self.name)

  class Author(Base):
    __tablename__ = 'authors'
  #   __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', backref='author')
    
    country_id = Column(Integer, ForeignKey('countries.id'))
    
    def __init__(self, name):
      self.name = name
    
    def __repr__(self):
      return "<Author('%s')>" % (self.name)

  class Country(Base):
    __tablename__ = 'countries'
  #   __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    
    authors = relationship('Author', backref='country')
      
    def __init__(self, name, capital=None):
      self.name = name
      self.capital = capital
    
    def __repr__(self):
      return "<Country('%s')>" % (self.name)

# First time create tables
    
Base.metadata.create_all(engine) 


book1=Book('war and peace')
author1=Author('tolstoy')
country1=Country('russia')

print book1
print author1
print country1

book1.author=author1
author1.country=country1

print book1
print author1
print author1.books
print country1.authors


#Create a session to actually store things in the db

Session = sessionmaker(bind=engine)
session = Session()

#Add data

session.add(book1)
session.add(author1)
session.add(country1)


#Persist all of this information
session.commit()

print list(session.query(Author))
# 
for author in session.query(Author).all():
    print author.name, author.country.name
# 
book2=Book('anna karenina')
book2.author=author1

session.add(book2)

book3=Book('tale of two cities')
session.add(book3)
# 
for book, author in session.query(Book, Author):
    print book.name, author.name
#  
for book, author in session.query(Book, Book.author):
 	  print book.name, author
# 
# 
for book, author in session.query(Book, Author).filter(Book.author != None):
   	print book.name, author.name
# 	
for book in session.query(Book).join(Author):
   	print book.name, book.author.name
# 
# 
session.commit()



