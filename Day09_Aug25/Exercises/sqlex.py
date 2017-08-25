# install sqlite from sqlite.org
# pip install sqlalchemy
# pip install pysqlite
# Check: http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Some info about sqlalchemy
print sqlalchemy.__version__

#Connect to the local database, can use :memory: to just try it out in memory
# The return value of create_engine() is an instance of Engine, and it represents the core 
# interface to the database, adapted through a dialect that handles the details of the database 
# and DBAPI in use. In this case the SQLite dialect will interpret instructions to the Python 
# built-in sqlite3 module.
engine = sqlalchemy.create_engine('sqlite:////Users/michelletorres/Desktop/players.db', echo=True)

# When using the ORM, the configurational process starts by describing the database tables we’ll be
# dealing with, and then by defining our own classes which will be mapped to those tables. 
# In modern SQLAlchemy, these two tasks are usually performed together, using a system known as 
# Declarative, which allows us to create classes that include directives to describe the actual 
# database table they will be mapped to.
# Classes mapped using the Declarative system are defined in terms of a base class which maintains 
# a catalog of classes and tables relative to that base - this is known as the declarative 
# base class. 
Base = declarative_base() 

#Define some schemas
class Player(Base):
  __tablename__ = 'players'
  
  #Have an ID column because player attributes (name, etc) are not unique
  id = Column(Integer, primary_key=True)
  name = Column(String)
  number = Column(Integer)
  
  team_id = Column(Integer, ForeignKey("teams.id"))
  
  def __init__(self, name, number, team=None):
    self.name = name
    self.number = number
    self.team = team
    
  def __repr__(self):
    return "<Player('%s', '%s')>" % (self.name, self.number)


class Team(Base):
  __tablename__ = "teams"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  players = relationship("Player", backref="team")
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "<team('%s')>" % (self.name)
    
# First time create tables
# The MetaData is a registry which includes the ability to emit a limited set of schema 
# generation commands to the database. As our SQLite database does not actually have 
# a users table present, we can use MetaData to issue CREATE TABLE statements to the database
#  for all tables that don’t yet exist. Below, we call the MetaData.create_all() method,
#  passing in our Engine as a source of database connectivity. We will see that special
#  commands are first emitted to check for the presence of the users table, and following
# that the actual CREATE TABLE statement:

Base.metadata.create_all(engine) 

# With our User class constructed via the Declarative system, we have defined information 
# about our table, known as table metadata. The object used by SQLAlchemy to represent this
#  information for a specific table is called the Table object, and here Declarative has made
#  one for us. We can see this object by inspecting the __table__ attribute:
#See structure of players table:
Player.__table__  

#Create a player
mason = Player("Mason Plumlee", 5)
print str(mason.id)
# Oops... nothing. Even though we didn’t specify it in the constructor, the id attribute still produces a value
#  of None when we access it (as opposed to Python’s usual behavior of raising AttributeError 
# for an undefined attribute). SQLAlchemy’s instrumentation normally produces this default value
# for column-mapped attributes when first accessed. For those attributes where we’ve actually 
# assigned a value, the instrumentation system is tracking those assignments for use within an 
# eventual INSERT statement to be emitted to the database.

#Create a session to actually store things in the db
# We’re now ready to start talking to the database. The ORM’s “handle” to the database is the Session.
#  When we first set up the application, at the same level as our create_engine() statement, 
# we define a Session class which will serve as a factory for new Session objects
Session = sessionmaker(bind=engine)
session = Session()
# The above Session is associated with our SQLite-enabled Engine, but it hasn’t opened any 
# connections yet. When it’s first used, it retrieves a connection from a pool of connections 
# maintained by the Engine, and holds onto it until we commit all changes and/or close the 
# session object.

session.add(mason)
# 
# #Create some more players
session.add_all([Player("Miles Plumlee", 40),
  Player("Seth Curry", 30), Player("Austin Rivers", 0),
  Player("The other Plumlee", 100)])

session.new 
# #Persist all of this information
# We tell the Session that we’d like to issue all remaining changes to the database and commit the transaction.
# 
session.commit()


# Test again... (it keeps the count in the order they entered the database)
print str(mason.id)

# Some querying
# order the results
for player in session.query(Player).order_by(Player.number):
  print player.number, player.name, player.id
  
#limit the results with offset, might use this for pagination
for player in session.query(Player).order_by(Player.number)[1:3]:
  print player.number, player.name

#Some filters
for player in session.query(Player).filter(Player.name == "Mason Plumlee").order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(Player.name != "Mason Plumlee").order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(or_(Player.name == "Mason Plumlee", Player.name == "Miles Plumlee")).order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(Player.name.like("%Plumlee%")).order_by(Player.number):
  print player.number, player.name

for player in session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number):
  print player.number, player.name

#Results are just lists  
results = session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number)
results.first()
results[0]
results[1]

#count is faster than loading all of the objects
session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number).count()

#how to work with relations
duke = Team('Duke')

players = session.query(Player).all()
mason.team = duke
players[1].team = duke
mason.team.players



#Lets load the two things together
for player, team in session.query(Player, Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, team.name

#equivalently  
for player in session.query(Player).join(Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, player.team.name

#Now some deletion (see SQLAlchemy Cascades for some fun data sanitation)
players
session.query(Player).filter(Player.number == 30).count()
seth = session.query(Player).filter(Player.number == 30).first()
session.delete(seth)
session.query(Player).filter(Player.number == 30).count()
session.query(Player).filter(Player.name.like("%Seth%")).count()
players
players = session.query(Player).all()
players 

#Updating
other_plumlee = players[3]
other_plumlee.name = "Marshall Plumlee"
# The Session is paying attention. It knows, for example, that Ed Jones has been modified:
session.dirty
session.commit()
# 
# How to convert data to csv
players = session.query(Player).all()
for player in players:
  print player.name, player.number, player.team

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.