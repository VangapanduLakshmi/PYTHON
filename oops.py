#!/usr/bin/env python
# coding: utf-8
OOPS:object oriented programmimg --> an approach/way/paradigm
the compleate task dividing in to objectswhy?
-->Complex Problems
--> organized
-->remove the redandence(duplicate)object
class
Encapsulation
Inheritance
polymorphism
AbstractionData science
--> compitation oriented -->going to build logic-->java,python,c,c++ etc
-->data centric--> AI,Data Science, DB-->pythonClass:Design/blue print/reference for task
             Class
               |
        --------------
        |             |
        Attributes/    methods/function/Actions
        variables/
        behaviour.everything in python is an "object"Object: the physical existence of class/the instance of the class/example of class
# **Creating Class**
class class_name:
    -->attributes
    -->create methods/functions
# In[1]:


class sample:
    pass


# **Bank Application**
Attributes:
    1.name
    2.Account no
    3.IFSc
    4.Branch
    5.balance
 Actions:
    1.Deposit
    2.withdraw
    3.Transfer
    4.Balance check
# In[30]:


class bank:
    def __init__(self,name,account_no,IFSC,Branch,Balance): #__init__ -->initialise the attributes/variables.
        #attributes,variables,behavoiur.
        self.name = name   #self store the current running object
        self.account_no = account_no
        self.IFSC = IFSC
        self.Branch = Branch
        self.Balance = Balance
    #action,functions, methods
    def deposit(self):
        amount=int(input("enter the amount to deposit:"))
        self.Balance=self.Balance+amount
        print("successfully deposited")
    def withdraw(self):
        amount=int(input("enter the amount to withdraw:"))
        if(self.Balance<amount):
            print("Insufficient fund in you account")
        else:
            self.Balance=self.Balance-amount
            print("successfully withdraw")
    def  checkbal(self):
        print(f'you habe{self.Balance} in your account')
    def customer_details(self):
        print(f'{self.name}\n{self.Balance}\n{self.Branch}\n')


# In[32]:


#Creating Object
customer=bank("Lakshmi","123445","IFSC123","India",200000)


# In[33]:


customer.deposit()


# In[34]:


customer.checkbal()


# In[35]:


customer.withdraw()


# In[36]:


customer.checkbal()


# In[37]:


customer.name


# In[1]:


customer.customer_details()


# # Inheritance

# def: access the variables and methods from parent class to child class (super class to sub class)

# # single inheritance
  parent
    |
  child
# In[6]:


#single inheritance.
class parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add():
        print(self.a + self.b)
    def mul():
        print(self.a *self.b)
class child:
    def wish(self):
        print("hello")


# In[7]:


child_class = child()


# In[8]:


child_class.wish()


# In[17]:


class parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a *self.b)
class child(parent):
    def wish(self):
        print("hello")


# In[18]:


child_class1 = child(2,4)


# In[19]:


child_class1.a


# In[20]:


child_class1.add()


# In[21]:


child_class1.mul()


# In[23]:


parent_class= parent(10,30)


# In[24]:


parent_class.add()


# # Multiple inheritance
   father    mother
     \         /
        child
# In[39]:


#multiple inheritance
class father:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a *self.b)
class mother:
    def __init__(self,a,b):
        self.a =a
        self.b=b
    def sub(self):
        print(self.a - self.b)
    def div(self):
        print(self.a / self.b)
class child(father,mother):
    def wish(self):
        print("hello")
  


# In[40]:


name= child(10,20)


# In[41]:


name.add()


# In[42]:


name.mul()


# In[43]:


name.sub()


# In[44]:


name.div()


# In[46]:


child.mro() #method resolution order.


# In[62]:


class father:
    def method1(self):
        print("i am father")
class mother:
    def method2(self):
        print(" i am mother")
class child(father,mother):
    def mothod(self):
        print("i am child")


# In[63]:


name = child()


# In[64]:


name.mothod()


# In[65]:


name.method1()


# In[66]:


name.method2()


# In[68]:


class father:
    def method1(self):
        print("i am father")
class mother:
    def method1(self):  
        print(" i am mother")
class child(father,mother):
    def mothod(self):
        print("i am child")


# In[69]:


name = child()


# In[70]:


name.mothod()


# In[71]:


name.method1()


# In[72]:


name.method1()


# **Multilevel inheritance**
multilevel inhertance

grand parent
    |
  parent
    |
  child
# In[82]:


class grand_parent:
    def method1(self):
        print("i am grand_parent")
class parent(grand_parent):
    def method2(self):  
        print(" i am parent")
class child (parent):
    def mothod(self):
        print("i am child")


# In[83]:


name2 = child()


# In[84]:


name2.mothod()


# In[85]:


name2.method1()


# In[86]:


name2.method2()


# In[87]:


name3= parent()


# In[88]:


name3.method1()


# In[89]:


name3.method2()


# In[90]:


name3.method()


# # Hierarchical inheritance
      parent
      /  |  \
   chi1 chi2 chi3
# In[103]:


class parent:
    def method1(self):
        print("i am parent")
class child1(parent):
    def method2(self):  
        print(" i am child1")
class child2(parent):
    def mothod3(self):
        print("i am child2")


# In[104]:


c1 = child1()


# In[105]:


c1.method2()


# In[106]:


c1.method1()


# # Hybrid Inheritance 

# In[108]:


class grand_parent:
    def method1(self):
        print("i am grand_parent")
class parent1(grand_parent):
    def method2(self):  
        print(" i am parent1")
class parent2:
    def method3(self):
        print("i am parent2")
class child (parent1,parent2):
    def mothod(self):
        print("i am child")


# In[109]:


p1= parent1()


# In[110]:


p1.method1()


# In[111]:


ch = child()


# In[112]:


ch.mothod()


# In[113]:


ch.method1()


# In[114]:


ch.method2()


# In[115]:


ch.method3()


# # To remove the duplicate methods

# In[ ]:





# In[52]:


class faculty:
    def __init__(self,desgn,salary):
        self.desgn = desgn
        self.salary = salary
    def salary(self):
        print(self.salary)
    def desgn1(self):
        print(self.desgn)  


# In[59]:


class duplicate:
    def __init__(self,name,branch,phone,address):
        self.name =name
        self.branch = branch
        self.phone = phone
        self.address = address
    def change_details(self):
        name=input()
        self.name=name
        address=input()
        self.address= address
        print(self.name,self.address)
    def phone(self):
        print(self.phone)
    def branch(self):
        print(self.branch)
    def phonechanged(self):
        new_phone = input()
        self.phone= new_phone
        print("the phone number is successfully")


# In[60]:


class student(duplicate):
    def __init__(self,year,fee):
        self.fee = fee
        self.year = year
    def Fee(self):
        print(self.fee)


# In[61]:


st= student(2020,70000)


# In[62]:


st.fee


# In[63]:


st.year


# In[68]:


st.phonechanged()


# In[65]:


dp= duplicate("Lakshmi","ECE",1243435445,"HYD")


# In[66]:


dp.address


# In[70]:


dp.change_details()


# # Polymorphism
*
1. multiplication
2. repitation
3. variable length arguments
4.                  Polymorphism
                      |
-------------------------------------------------
|                 |                             |
duck type       overloading                   overriding
philosopy of      1.operator overloading        1.mothod overriding
python            2. method overloading         2. constructor overriding
                  3. cunstructor overloading
# In[ ]:


class st:
    def name(self, int):
        print("int data type")
    def name(self, float):
        print("float data type")
    def name(self, str):
        print("string data type")

method overloading: differant data type and  length of arguments. and same method namepython doen't support the method overloading. but, we can do multiple dispatch method
# # Operator overlaoding

# In[82]:


class sum:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return (self.a + other.a)


# In[83]:


c = sum(200)


# In[84]:


d= sum(300)


# In[85]:


c+d


# In[86]:


s=sum("hello")


# In[89]:


p= sum(" Lakshmi")


# In[90]:


s+p


# # Constructor

# In[91]:


class name:
    def __init__(self): # constructor name is init in this code. it takes the last constructor returns the that constructor only
        print("no arguments")
    def __init__(self,a):
        print("one argument")
    def __init__(self,a,b):
        print("two arguments")


# In[92]:


n= name()


# In[93]:


n= name(1)


# In[94]:


n =name(1,2)


# In[95]:


class name:
    def __init__(self): # constructor name is init in this code. it takes the last constructor returns the that constructor only
        print("no arguments")
    def __init__(self,a,b):
        print("two arguments")
    def __init__(self,a):
        print("one argument")


# In[96]:


s= name()


# In[97]:


s =name(1,2)


# In[98]:


s = name(2)


# # overriding
if we can write same method name and differant arguments in differant classes . that type of method is called overriding.
# In[99]:


class a:
    def method(self):
        print("class a")
class b:
    def method(self):
        print("class b")


# In[100]:


c= b()


# In[101]:


c.method()


# In[104]:


class a:
    def method(self):
        print("class a")
class b(a):
    def method(self):
        print("class b")


# In[106]:


d1= b()


# In[107]:


d1.method()


# In[108]:


class a:
    def method(self):
        print("class a")
class b(a):
    def method(self):
        super().method()
        print("class b")


# In[109]:


s=b()


# In[110]:


s.method()1


# # constructor overriding

# In[111]:


class name:
    def __init__(self):
        print("this is the name class")
class name1:
    def __init__(self):
        print("this is the name1 class")


# In[112]:


d= name1()


# In[117]:


class name:
    def __init__(self):
        print("this is the name class")
class name1(name):
    def __init__(self):
        super().__init__()
        print("this is the name1 class")


# In[118]:


e= name1()


# # Encapsulation

# Encapsulation is one of the fundamental principles of object-oriented programming (OOP) that focuses on bundling data and methods together within a class, hiding the internal details and providing a public interface to interact with the object
# 
# It promotes the concept of data hiding and information hiding.

# In[2]:


class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def display_info(self):
        print(f"Name: {self._name}, Age: {self.__age}")


# Create an instance of the Person class
person = Person("John", 30)

# Access the public attribute directly
print(person._name)  # Output: John

# Access the protected attribute (convention, not enforced)
print(person._Person__age)  # Output: 30

# Access the private attribute (name-mangled)
# print(person.__age)  # Raises an AttributeError

# Access the attribute using a getter method
print(person.get_age())  # Output: 30

# Modify the attribute using a setter method
person.set_age(35)

# Call a method that displays the person's information
person.display_info()  # Output: Name: John, Age: 35


# In[ ]:




