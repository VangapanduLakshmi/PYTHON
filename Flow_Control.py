#!/usr/bin/env python
# coding: utf-8

# # Flow Control
           flow control
                |
---------------------------------------------------
|                   |                              |
conditional     loop control                   transfer 
statements      statements                     statements
1.if             1.for                         1.break
                 2.while                       2.continue
2.elif           in python don't have          3.pass
3.else              dowhile.
syntax:if(condition):
          statement1
          statement2
          ......indentation--->1 tab. or 4 spaces.
# In[1]:


a=20
b=30
if(a==20 and b==20):   #true and false==false. therefore the if condition is not executed.
    print(a,b)


# In[2]:


a=20
b=30
if(a==20 or b==20):
    print(a,b)


# In[3]:


a=20
b=10
if a>b:
    print(a)


# In[4]:


s="innomatics"
if "n" in s:
    print(s)


# In[5]:


a=5
b=5
if a is b:
    print("a and b are equale")


# In[6]:


s="innomatics"
if "n" in s:
print(s)

elif: more than one condition
syntax: elif(condition):
             statement1
             statement2
            .........
# In[7]:


n1=int(input())
if(n1%2==0):
    print("even")
else:
    print("odd")


# **Generating a to z**

# In[2]:


val=[chr(i) for i in range(65,91)]
print(val)


# **Registration for any website**

# In[1]:


#registration
user_name=input()
mail_id=input()
password=input()


# In[2]:


#login
mail=input()
password1=input()
if(mail_id.endswith("@gmail.com") and mail_id==mail and password==password1 and mail_id.lower()):
    print("login successfully")
else:
    print("login faild")


# **Find the maximum number**

# In[4]:


n=int(input("n:"))
n1=int(input("n1:"))
n2=int(input("n2:"))
if(n>n1 and n>n2):
    print("n is greater")
elif(n1>n and n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater")


# **Tax Programm**

# In[3]:


income=float(input())
if(income>0):
    if(income>=0 and income<500000):
        print("no tax")
    elif(income>=500000 and income<700000):
        print(income*(5/100))
    elif(income>=700000 and income<1000000):
        print(income*(10/100))
    else:
        print(income*(15/100))
else:
    print("invalid income")


# **Ternary operator**
num=int(input())
val=firstvalue if(condition) else secondvalue   #syntax of ternary operator.
print(val)
# In[4]:


num=int(input())
res="even" if(num%2==0) else "odd"  # or print("even") if(condition) else print("odd") 
print(res)


# In[5]:


a=20
b=30
c= a if a>b else b
c


# # Iterative Statements

# **Range():**
1.Range data type represents a sequence of numbers.
2.the elements present in the range data type are not modified. i.e range() data type is a immutable.
syntax=range(start,stop,step)
# for loop:
# syntax: for i in collection:

# In[4]:


marks=[1,2,3,4,5,6,7,8]
for i in marks:  #i is temparary variable.
    print(i,end=" ")


# In[24]:


range(1,10,2)

for temparary in collection:  #collection---> list,tuple,string,dictionary 
# In[13]:


name="Innomatics research lab"
for i in name:
    if(i =="a" or i=="e" or i=="i" or i=="o" or i=="u"or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        print("*",end="")
    else:
        print(i,end="")


# In[15]:


name1="Innomatics Research Lab"
vow=["a","e","i","o","u"",A","E","I","O","U"]
for i in name1:
    if i in vow:
        print("*",end="")
    else:
        print(i,end="")


# for--> it associate with each enad every element in collection

# # WHILE
synt: while(condition):
        statement1
        statement2
        .........
        .........
# In[1]:


n=0
while(n<=10):
    print(n)
    n=n+1

num=20
while(True):  #infinite loop
    print(num)
# **Luck draw game**

# In[6]:


import random
system_num=random.randint(1,5)
attems=3
while(attems>0):
    user_num=int(input("enter the number:"))
    if(system_num==user_num):
        print("congrats.. you won")
        break
    else:
        attems=attems-1
        print(f"you have{attems} only")
        if(attems==0):
            print("you lost")
            break
            


# In[2]:


name="Innomatics research lab"
s=0
while(s<len(name)):
    if(name[s]=="r"):
        print(s)
        break
    else:
        s=s+1


# # Transfor Statements

# 1. break----> it stop the running 
# 2. continue ---> skip the current excution
# 3. pass  ---> nothing

# In[3]:


name


# In[19]:


lst=[20,30,40,50,70,30,38]
for i in lst:
    if(i<40):
        print(i)
        break


# In[13]:


lst=[20,30,40,50,70,30,38]
for i in lst:
    if(i<40):
        continue
    else:
        print(i)


# In[14]:


lst=[20,30,40,50,70,30,38]
for i in lst:
    if(i<40):
        break
    else:
        print(i)


# In[21]:


lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if(i>6):
        break
    else:
        print(i)
    
        
            


# In[26]:


lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if(i%2!=0):
        continue
    else:
        print(i)
    

