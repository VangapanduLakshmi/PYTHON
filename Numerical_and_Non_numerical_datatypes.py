#!/usr/bin/env python
# coding: utf-8
                   data types
                      |
    ----------------------------------------
    |                                       |
------------------------                 1.list
|                      |                 2.tuple
numerical         non numerical          3.set
1.int               1.string             4.dictionary
2.float             2.boolean            5.string
3.complexprint() ---> to disply the output in console
input() --->taking the input from user
len() ---> no.of values present in that dataset
id() ---> address of the variable
help()
type()
# In[3]:


name="Lakshmi"
city="vizianagaram"


# In[4]:


print(name,city)


# In[8]:


print("hello i am {} i am from {}".format(name,city)) #---> the {} takes the original value.


# In[9]:


print("hello i am{}, i am from {}".format(name,city))


# In[10]:


print(f"hello i am {name},i am from{city}")   # f is nothing but formate


# In[14]:


print('hello i am '+name+" i am from "+city)


# Input()

# In[15]:


name=input()


# In[16]:


print(name)


# In[17]:


len(name)


# In[1]:


name1=input()  #state name
name2=input()  #city name
print(name1+" "+name2)


# COMMENTS
1.Single line comment  ----> #
2.multi line comment/documentation ---->''' '''
# In[2]:


#vangapandu lakshmi from vizianagaram


# In[2]:


S='''My name is vangapandu lakshmi from vizianagaram, currently studying in innomatics research lab'''
type(S)


# **Numerical datatypes**

# **Integer**

# In[14]:


a=10
b=20
type(a+b)


# **float data type**

# In[15]:


type(3.4)


# In[16]:


len(a)


# In[17]:


n=int(input())


# In[18]:


print(a)
type(a)


# In[15]:


help(int)


# In[17]:


bin(34) #----> to convert the decimal to binary


# In[18]:


bin(12)


# In[19]:


int(0b1100) # to convert binary to integer


# In[20]:


oct(12)  #decimal to octa


# **bit_count**

# def: Number of ones in the binary representation of the absolute value of self

# In[3]:


bin(13)


# In[21]:


(13).bit_count()


# In[23]:


(13).bit_length()  #number of both ones and zeros in the binary representation of the absolute value of self


# **Complex data type**

# In[24]:


2+5j


# In[33]:


a=2+6j
b=2+6j


# In[34]:


a is b


# In[35]:


type(a)


# In[4]:


id(a)


# In[5]:


id(b)


# In[5]:


a=10
b=10


# In[6]:


type(a)


# In[7]:


a is b


# In[8]:


id(a)


# In[9]:


id(b)


# In[11]:


id(a) == id(b)


# **non numerical data type**

# **boolean data type**

# In[13]:


a=True


# In[14]:


type(a)


# help(a)

# In[16]:


id(a)


# # string

# textual data

# using single quoates or double quoates

# In[17]:


name="innomatics"


# In[18]:


type(name)


# In[19]:


len(name)


# In[20]:


id(name)


# In[21]:


help(str)


# Assignment operator(=)

# In[29]:


a=10
b=20


# In[30]:


a,b=10,20


# In[31]:


a


# In[32]:


b

