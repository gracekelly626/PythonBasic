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
  
## 3. advanced class
class Employee:
  def __init__(self, name, id, years_of_experience, base_salary):
    self.m_name = name 
    self.m_id = id
    self.m_years = years_of_experience
    self.m_base_salary = base_salary

  def getName(self):
    return self.m_name

  def getID(self):
    return self.m_id
  
  def getBaseSalary(self):
    return self.m_base_salary

  def getSalary(self):
    return self.m_base_salary

# QuantDev class inherits from Employee class
# aka QuantDev class is a derived class of Employee - Employee is a base class of QuantDev
class Quant(Employee): 
    def __init__(self, name, id, years_of_experience, base_salary, bonus):
# super() 调用base class的methods, member variables
        super().__init__(name, id, years_of_experience, base_salary)
        self.m_bonus = bonus
        
    def getSalary(self):
        return self.m_bonus+super().getBaseSalary()
        #self.m_base_salary也可以work， 但是不推荐， 在class中尽量用公开的东西

class QuantTrader(Quant):
  def __init__(self, name, id, years_of_experience, base_salary, bonus, commission):
    super().__init__(name, id, years_of_experience, base_salary, bonus)
    self.m_commision = commission
  
  def getSalary(self):
    return self.m_commision + super().getSalary()
    # 如果写super(Quant, self).getSalary() 就是employee class里面的salary, ie, super(Parent, self).my_method()
    

k = Employee("Kuangdi", "G01222298", 2, 50)
#print(k.getName())
#print(k.getID())

m = Quant("MC", "C222222", 10,100, 50)
#print(m.getName())
#print(m.getID())

w = Employee("Wuyang", "F3333333", 10,150)

p = QuantTrader(name="Pangpang", id="M6666666", years_of_experience=3, base_salary=50,bonus=50, commission=20)

employee_list = [k,m]
employee_list.append(w)
employee_list.append(p)

for i in employee_list:
  print(i.getName(), ":", i.getSalary())
  
homework - design a similar frame
class Customer:
  def __init__(self, name, age, account_no):
    self.m_name = name
    self.m_age = age
    self.m_account_no = account_no
  
  def getName(self):
    return self.m_name
  
  def getSaving(self):
    return None

class SavingCustomer(Customer):
  def __init__(self, name, age, account_no, saving_amount):
    super().__init__(name, age, account_no)
    self.m_saving_amount = saving_amount
  
  def getSaving(self):
    return self.m_saving_amount

class EverydaySavingCustomer(SavingCustomer):
  def __init__(self, name, age, account_no, saving_amount, everyday_saving):
    super().__init__(name, age, account_no, saving_amount)
    self.m_everyday_saving = everyday_saving

  def getSaving(self):
    return self.m_everyday_saving + super().getSaving()

k = EverydaySavingCustomer(name = "Kuangdi", age=25, account_no=3366, saving_amount = 6000, everyday_saving = 600)
m = SavingCustomer(name = "MC", age=31, account_no=2266, saving_amount = 60000)
p = Customer(name = "Pangpang", age=30, account_no=1166)
w = EverydaySavingCustomer(name = "lwy", age=31, account_no=4466, saving_amount = 7000, everyday_saving = 700)

customer_list = [k,m,p,w]

for i in customer_list:
  print(i.getName(), ":", i.getSaving())
