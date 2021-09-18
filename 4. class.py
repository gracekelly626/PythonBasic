
## class is like the blueprint. can tell people how to create instances
## instance aka object
class Person:
##__init__ a special method of class in Python - constructor is a general programming term for creating an instance of a class
  def __init__(self, name, age, address):
## self is usually the first parameter of a method
    self.m_name = name
    self.m_age = age
    self.m_address = address

  def getName(self):
## even the getName method doesn't have any specific parameters, should put 'self' as the first parameter. 
      return self.m_name

k = Person("Kuangdi", 3, "E14")
print(k.getName())
#function of a class aka method 
