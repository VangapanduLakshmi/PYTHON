#!/usr/bin/env python
# coding: utf-8

# # Function
1.code reusability
synt: def function_name(param/args):   def means define
        coede//def fun(a,b):
    return a*b
fun(a=10,20)
     |   |
keyword  position
# **creating a function**

# In[1]:


def name():
    print("Function is  succesfully created")     #creating the function


# In[2]:


name()  #calling the function


# In[3]:


name()


# In[4]:


#sum of two numbers
def add(a,b):
    print(a+b)   #here a,b are arguments


# In[5]:


add(4,6)


# In[6]:


def even(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")


# In[7]:


even(4)


# In[8]:


even(9)


# # Types of arguments
types of arguments.
1. positional arguments  --->based on the position -->call by value --->uses at calling
2.keyword ---->  call by referance  ---> uses at calling
3.default  ----> uses at while creating a function
4.variable
# **positional arguments**

# In[9]:


def add(a,b,c):
    print(a+b-c)


# In[10]:


add(4,5,2)


# In[11]:


add(3,5,1)


# In[12]:


def hai(c,b,a):
    print(c-a+b)
hai(1,3,2)


# In[13]:


hai(2,1,3)


# In[14]:


hai(1,4,"h")


# In[15]:


def concat(name1,name2):
    print(name1 + name2)


# In[16]:


name1 = input("enter first name: ")
name2 = input("enter second name: ")
concat(name1,name2)


# **keyword Arguments**

# In[17]:


def sub(a,b):
    print(a-b)


# In[18]:


sub(4,2)


# In[19]:


sub(a = 20,b =10)


# In[20]:


sub(b =10,a = 20)


# In[21]:


sub(b = int(input("B value")),a = int(input("enter a value: ")))


# In[22]:


def division(n,n1):
    print(n/n1)
    print(n//n1)
    print(n%n1)


# In[23]:


division(n = int(input('n value : ')),n1 = int(input('n1 value : ')))


# **combination of postion and keyword arguments**

# In[25]:


def div(n1,n2):
    print(n1/n2)


# In[26]:


div(10,4) #postion


# In[28]:


div(n1 = 10,n2 = 4)  #keyword


# In[29]:


div(10,n1 = 4)   #both combination


# In[30]:


div(n1 = 10, 4)  #both combination

#positional argument follows keyword argument


# In[31]:


div(10, n2=95)


# **Default arguments:**
if user doesn't provide any value ,it tackes the default value.
def default(name,city,age,role):
    print(name)
    print(city)
    print(age)
    print(role)
default("ram","hyd",27,"data science") if name="ram"-->it gives positional error,
default("laxmi","hyd",23)  ---->mismatch error.

# In[1]:


def details(name,city,age,role):
    print(name)
    print(city)
    print(age)
    print(role)
details("laxmi","hyd",21,"data science")


# In[2]:


def details(name,city,age,role):
    print(name)
    print(city)
    print(age)
    print(role)
details("laxmi","hyd",21,role="data science")


# In[3]:


def details(name,city,age,role):
    print(name)
    print(city)
    print(age)
    print(role)
details(name="laxmi","hyd",21,"data science")


# In[4]:


def details(name,city,age,role):
    print(name)
    print(city)
    print(age)
    print(role)
details("laxmi","hyd",21)


# In[5]:


def details(name,city,age,role="data science"):
    print(name)
    print(city)
    print(age)
    print(role)
details("laxmi","hyd",21)


# In[6]:


def details(name,city,age,role="data science"):
    print(name)
    print(city)
    print(age)
    print(role)
details("laxmi","hyd",21,"data analysis")


# In[9]:


def wishes(name="lakshmi"):
    print(f"hello {name}. how are you")
wishes()


# In[10]:


wishes("laxmi")


# In[11]:


name="python programming languages"


# In[12]:


name.split()


# In[13]:


name.split("r")


# In[17]:


def student(name,class1,city="hyd",school="HPS"):
    print(f"name:{name}")
    print(f"class:{class1}")
    print(f"city:{city}")
    print(f"school:{school}")
student("ram",9,"hyd","HPS")


# In[19]:


student("laxmi",8)


# In[20]:


def player(name,age,team,country="india"):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"team:{team}")
    print(f"country:{country}")
player("Dhoni",30,"csk")


# In[22]:


player("virat",35,"rcb")


# In[23]:


player("rohith",32,'mi')


# In[24]:


def player(name,age,team,country="india"):
    print(f"{name},{age},{team},{country}")


# In[25]:


player("rohith",32,"MI")


# In[26]:


def add(a,b):
    print(a+b)


# In[27]:


add(3,7)


# **Variable length arguments**

# In[28]:


#12,23,45,67,89,09  -- add or multiply multiple values. at that time we can use the variable length arguments.


# In[29]:


def mul(n):
    print(n)


# In[30]:


mul(2)


# In[31]:


mul(2,3,4)


# In[32]:


def mul(*n):
    print(n)


# In[33]:


mul(1,2,3,4,6,7,8,9)


# In[34]:


def mul(*n):
    for i in n:
        print(i,end=" ")


# In[35]:


mul(1,2,3,4,5,6,7,8,9)


# In[36]:


def mul(*n):
    for i in n:
        print(i+3,end=" ")
mul(1,2,3,4,5,6,7)


# In[37]:


def mul(*n):
    for i in n:
        print(i*i,end=" ")
mul(1,2,3,4,5,6,7)


# In[39]:


def mul(*n):
    for i in n:
        if(i.startswith("a")):
            print(i)
mul("apple","grape","mango")


# In[40]:


def mul(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum)
mul(1,2,3,4,5,6,7)


# In[41]:


mul(23,45,12,34)


# In[46]:


def mul(*n):
    for i in n:
        print(i)
n=[1,2,3,4,5,6,7,8]
mul(n)


# In[44]:


n=[34,56,78,1,2,4,6,8,9,8]
mul(n)


# In[47]:


def key(**val):
    print(val.items())


# In[48]:


key(name="ram",age=34)


# In[49]:


def key(**val):
    for i,j in val.items():
        print(j)

        


# In[50]:


key(name="ram",age=34)


# **Fuction variable:**
two tyeps of variables:
    1. local variables  ---> the variable is declared inside of the function is called local varaibles
    2.global variables  ---->the variable is declared outside of the function is called global varaibles
 note. if we wnat to declared global variable inside the function. we can use the global keyword
# In[51]:


a=10   #global veriable
def val(a):
    b=20     #local variable
    print(a+b)
val(a)


# In[57]:


def val(a):
    b=20     #local variable
    print(a+b)
def val1(a):
    b=30
    print(a*b)
val1(a)
val(a)


# In[58]:


def val(a):  # global variables are acces from any function.
    b=20     #local variable
    print(a+b)
def val1(a):
    print(a*b)   #b not defined. local varibles are can't acces other function. it is acces only with in the particular function.
val1(a)
val(a)


# In[63]:


x=10
def f(x):
    global y
    y=20
    print(x+y)
def f1(x):
    print(x*y)
f(x)
f1(x)


# # LAMBDA FUNCTION
a function without any name, such functions are called nameless functions or ananymous function
2. function can be written in a single line.
# syntax: **lambda argument_list: expression**

# In[70]:


a=lambda n:n**2
print(a,(4))


# In[71]:


a=lambda n:n**2
print(a(4))


# In[72]:


d=lambda a,b:a+b
print(d(5,7))


# In[73]:


d(6,8)


# In[74]:


f=lambda a,b,c:a*b*c
f(3,5,4)


# In[75]:


f(1,2,4)


# **what is the diff b/w return and print:**

# In[83]:


def add(a,b):
    print(a+b)  #jest print the statement.
t=add(5,6)
t
print(type(t))


# In[85]:


def add(a,b):
    return a+b   # store the  return value to the function.
d=add(5,6)
d
print(type(d))


# In[2]:


create a simple function that tacke two inputs from the user and 
a=int(input())
b=int(input())
def module(a,b):
    return a%b
res=module(a,b)
print(res)


# In[4]:


def module(a=int(input()),b=int(input())):
    return a%b
module()


# # lambda function with loops and conditions

# In[5]:


lst=[1,2,3,4,5]


# In[8]:


s=lambda x:x%2==1
s(4)


# # Recursive Function
a function that call itself is called recursive function.
# **factorial**

# In[11]:


def fact(n):
    if(n>=0):
        if n<=1:
            return 1
        else:
            return n*fact(n-1)
    else:
        print("enter +ve values only")
        
n=int(input())
fact(n)


# In[19]:


n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)    


# In[21]:


n=int(input())
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print(fact)
    


# In[4]:


def feb(n):
    if(n<=1):
        return n
    else:
        val= feb(n-1)+feb(n-2)
        return val
feb(4)
            


# In[33]:


n=int(input())
if(n<=0):
    print("+ve values only")
else:
    for i in range(n):
        print(feb(i))


# # Filter():
syntax:filter(function,sequence)
# In[39]:


def even(n):
    if(n%2==0):
        return n
    else:
        pass


# In[40]:


lst=[1,2,3,4,5,6,7,8,9]
filter(even,lst)


# In[41]:


list(filter(even,lst))


# In[1]:


def string(i):
    if(i.startswith("a")):
        return i
    else:
        pass


# In[2]:


lst1=["apple","banana","grape","avacado","appricod"]
set(filter(string,lst1))


# In[49]:


tuple(filter(string,lst1))


# In[58]:


lst2=["a","e","i","o","u","A","E","I","O","U"]
def vowel(n):
    for i in n:
        if i in lst2:
            return i
        else:
            pass


# In[59]:


string=input()
list(filter(vowel,string))


# # MAP FUNCTION():
syntax: map(function,sequence)
# In[10]:


def type1(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"


# In[11]:


lst3=[1,2,3,4,5,6,7,8,9]
list(map(type1,lst3))


# In[75]:


lst4=[10,20,30,40,50,60,70,80,90,100]
def div(n):
    return n//10
list(map(div,lst4))


# In[5]:


def vowel(n):
    for i in n:
        if i in ["a","e","i","o","u","A","E","I","O","U"]:
            return "VOWEL"
        else:
            return i


# In[7]:


string=input()
list(map(vowel,string))


# # Reduce()

# In[83]:


from functools import *
l=[10,20,30,40]
func1=lambda x,y:x+y


# In[84]:


reduce(func1,l)


# # Enumerate

# In[8]:


lst=[1,2,3,4,5]
for i,j in enumerate(lst):
    print((i,j))


# # zip()

# In[6]:


lst=[1,2,3,4,5,6]
lst1=["a","b","c","d"]
lst3=["A","B","C","D","E"]
for i,j,k in zip(lst,lst1,lst3):
    print(i,j,k)


# In[6]:


lst=[1,2,3,4,5,6]
lst1=["a","b","c","d"]
lst3=["A","B","C","D","E"]
for i,j,k in zip(lst,lst1,lst3):
    print(f"{i}:{j}->{k}")


# In[8]:


lst2=[chr(65+i) for i in range(26)]
print(lst2)


# In[9]:


lst4=[i for i in range(1,27)]
print(lst4)


# In[10]:


for i,j in zip(lst2,lst4):
    print(i,j)


# In[2]:


data = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
transposed = list(zip(*data))
transposed


# In[3]:


pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)


# In[4]:


numbers


# In[5]:


letters


# In[ ]:




