#!/usr/bin/env python
# coding: utf-8

# # Exception

# **EXCEPTION:** Exception is an event, that disturb's the normal flow of the program. during programm execution
# 1. Exception is a run time error
# 2. any abnormal event is called Exceeption.

# Error:error is a diviation from normal flow of the programm execution,that caused by various factors. like syntax error, logical error etc.

# In[ ]:


ERROR
  |
---------------------------
|            |             |                
syntax    logical        run time
error     error          error


# **Syntsx Error** : the error occures when the programmer writen the invalid syntax. that type of error is called Syntax error

# In[1]:


a=int(input())
if(a=10):
    print(a)
else:
    print("a")


# **Logical Error** the error occures when the programmer writen the invalid logic. that type of error is called Logical error

# # RUN TIME ERROR

#  **a unwanted and unexpected event that disturbs normal flow of program is called exception**
#Resky code
try:
    #risky code
except:
    #handling code/alternative code
else:
    
finally:
    
# In[2]:


print("*************************************")
try:
    a=int(input())
    b=int(input())
    print(a/b)
except(ValueError, ZeroDivisionError):
    print("enter valid number")
print("*************************************")


# In[4]:


print("*************************************")
try:
    a=int(input())
    b=int(input())
    print(a/b)
except(ValueError, ZeroDivisionError):
    b=int(input())
    print(a/b)
print("*************************************")


# In[3]:


try:
    a=int(input())
    b=int(input())
    print(a/b)


# In[7]:


try:
    a=int(input())
    b=int(input())
    print(a/b)
except Exception as msg:
    print(msg)


# In[1]:


try:
    a=int(input())
    b=int(input())
    print(a/b)
except(ValueError, ZeroDivisionError):
    b=int(input())
    print(a/b)


# In[4]:


a=input()
b=int(input())
print(a*b)


# In[20]:


try:
    a=input()
    b=int(input())
    print(a*b)
except ValueError:
    b=int(input())
    print(a*b)


# In[5]:


file=open("regex.txt","x")


# In[6]:


try:
    file=open("regex.txt","x")
except FileExistsError:
    print("FileExistsError")
    file=open("updated_data2.txt","x")
    


# In[7]:


try:
    a=input()
    b=int(input())
    print(a*b)
except Exception as msg:
    print(msg)
else:          # else part will run only there is no exception
    print("else is running")
finally:   # finally is excecuted irrespective of exception
    print("Exception handling is done successfully")


# In[32]:


try:
    a=input()
    b=int(input())
    print(a*b)
except Exception as msg:
    print(msg)
finally:  
    print("Exception handling is done successfully")


# In[8]:


try:
    a=input()
    b=int(input())
    print(a*b)
#except Exception as msg:
    #print(msg)
else:          # else part will run only there is no exception
    print("else is running")
finally:   # finally is excecuted irrespective of exception
    print("Exception handling is done successfully")


# In[9]:


try:
    a=input()
    b=int(input())
    print(a*b)
finally:   # finally is excecuted irrespective of exception
    print("Exception handling is done successfully")


# In[10]:


def password():
    pass1=input()
    if len(pass1)<8:
        raise ValueError
    else:
        print("password is correct")


# In[11]:


password()


# In[12]:


def password():
    pass1=input()
    if len(pass1)<8:
        raise ValueError
    else:
        print("password is correct")


# In[13]:


password()


# In[1]:


def div(a,b):
    if b==0:
        raise (ZeroDivisionError)
    else:
        print(a/b)


# In[2]:


div(3,4)


# In[3]:


div(4,0)


# In[4]:


div(4,"two")


# In[11]:


def div(a,b):
    if(b==0):
        raise ZeroDivisionError("Division by zoro is not allowed")
    elif not isinstance(b,int):
        raise TypeError("b must be integer")
    else:
        print(a/b)


# In[12]:


div(2,3)


# In[13]:


div(3,0)


# In[14]:


div(5,"two")


# In[15]:


div(4,5.0)

