## 1. basic class
## class is like the blueprint. can tell people how to create instances
## instance aka object
class Person:
##__init__ a special method of class in Python - constructor is a general programming term for creating an instance of a class
  def __init__(self, name, age, address):
## self is usually the first parameter of a method
    self.m_name = name
## usually self.XX is a member variable of a class. it is carried by self/instance. usually cannot be touched by other instance/object 
    self.m_age = age
    self.m_address = address

  def getName(self):
## even the getName method doesn't have any specific parameters, should put 'self' as the first parameter. 
    return self.m_name

  def getAddress(self):
    return self.m_address

  def changeAddress(self, new_address):
    self.m_address = new_address

k = Person("Kuangdi", 3, "E14") ## self is k 

print(k.getName())
## print(k.m_name) in general cases, it is not allowed although in python it works.
#function of a class aka method 
print(k.getAddress())
k.changeAddress("E1")
print(k.getAddress())

## home assisgnment 
## 创建一个新的Person的object, 然后用一个loop把它年龄从0改到100岁, 并且print出来
class young_lady:
  def __init__(self,name, age, beauty, IQ):
    self.m_name = name
    self.m_age = age
    self.m_beauty = beauty

  def getAge(self):
    return self.m_age
  
  def changeAge(self,new_age):
    self.m_age = new_age

k = young_lady('Kuangdi', 3, 'super pretty', 'super intellegent')

for i in range(1,101):
  k.changeAge(i)
  print(k.getAge())
  
 ######################################
## 2. advanced class
class Employee:
  def __init__(self, name, id, years_of_experience):
    self.m_name = name 
    self.m_id = id
    self.m_years = years_of_experience

  def getName(self):
    return self.m_name

  def getID(self):
    return self.m_id

k = Employee("Kuangdi", "G01222298", 2)
#print(k.getName())
#print(k.getID())

m = Employee("MC", "C222222", 10)
#print(m.getName())
#print(m.getID())

w = Employee("Wuyang", "F3333333", 10)

employee_list = [k,m]
employee_list.append(w)

for i in employee_list:
  print(i.getName())
