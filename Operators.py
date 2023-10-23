#!/usr/bin/env python
# coding: utf-8

# # Operators

# Operator is a symbol that perform certain operation.

# **Operators available in python are:**
# 
# Arithmatic (+, -, *, /, %, //, ***)
# 
# Relational (>, >=, <, <=)
# 
# Equality (==, !=)
# 
# Logical (and, or, not)
# 
# Bitwise (&, |, ^, ~, <<, >>)
# 
# Assignment (=, +=, -=, *=, /=, etc..)
# 
# **Ternary Operators**
# 
# Identity --> is, is not (used for address comparision)
# 
# Membership --> in, not in

# **Arithematic operators**
1.Addition
2.subtraction
3.multiplication
4.division
5.Exponent
# **Addition**
# def: adding the numbers, 
# the numbers either int,float etc.
1.Integer
ex: 2,3,4,5,4564,78
2.Float
ex:2.3,4.5,6.7 etc
3.String
ex: lakshmi,laxmi
# In[1]:


3+5


# In[2]:


3+7.5

1.addition
2.concatenation
# In[6]:


"vangapandu"+" Lakshmi"


# In[7]:


"Lakshmi"+ 4


# In[8]:


"Lakshmi"+"4"


# In[9]:


2+ True


# in python True is consider as "1" and False is consider as "0"

# In[1]:


4+ False


# In[12]:


"string"+ True


# **Subtraction**(-)

# int,float etc.

# In[16]:


"string"-"string1"


# In[14]:


3-45


# In[15]:


2-4.2


# In[2]:


2 - True


# **Multiplication**

# In[1]:


2*4


# In[17]:


"lakshmi"*False # string with boolian.


# In[18]:


"lakshmi"*True


# In[20]:


"innomatics "*4 #Repetation (strings & int)


# In[21]:


"laxmi"*4.5


# In[22]:


4*4


# **Division**
normal division(/)
floor division(//)
modulor operator(%)
# **normal division(/)**  

# it gives exact value

# In[23]:


15/5


# In[24]:


45/4


# In[25]:


12/3


# **floor division**
it gives the quocient
# In[28]:


15//5


# In[29]:


45//4


# In[30]:


12//3


# **modulor operator**

# it gives the remainder

# In[31]:


15%5


# In[32]:


45%4


# In[33]:


12%3


# In[34]:


3/6


# In[35]:


3//6


# In[36]:


3%6


# In[37]:


125/3


# In[38]:


125//3


# In[39]:


125%3


# **use cases**

# even/odd numbers

# In[40]:


126%2


# In[41]:


127%2


# **Exponent/Power operator**

# sqare of 3^2

# In[42]:


3**2


# In[43]:


4**5


# In[44]:


9**(1/2) #square root


# In[46]:


16**(1/2)


# In[60]:


n1=20
n2=45
print("addtion ", n1+n2)
print("subtraction ", n1-n2)
print("multiplication ", n1*n2)
print("Normal division ",n1/n2)
print("floor division",n1//n2)
print("modulor operator",n1%n2)
print("exponent operator ",n1**0.5)
print("exponent operator ",n2**0.5)


# In[67]:


name1="Lakshmi "
name2="Vangapandu"
print(name2+" "+ name1)


# In[58]:


print(name1*3)


# **2. Comparative Operators**

# it returs boolean data type
>= greater than or equal
<= less than or equal
>  less than
<  greater than
==  equal
!= not equal
# In[61]:


20>=20


# In[62]:


20<=20


# In[63]:


20>20


# In[64]:


20<20


# In[65]:


20==20


# In[66]:


20!=20


# In[69]:


a=30
b=40


# In[70]:


a<b


# In[71]:


a>b


# In[72]:


a<=b


# In[73]:


a>=b


# In[74]:


a==b


# In[75]:


a!=b


# In[84]:


n1=20
n2=150
print(n1>n2)
print(n1>=n2)
print(n1<n2)
print(n1<=n2)
print(n1==n2)
print(n1!=n2)


# **3.Logical Operators**
AND (and)
OR  (or)
NOT  (not)
AND

i/p1    i/p2     o/p

false  false    false
false  true     false
true   false    false
true   true     true
# 0, 0.0, ""  -----> false

# In[85]:


True and False


# In[86]:


(4>3) and (5>4)


# In[89]:


0 and 0


# In[90]:


0 and 1


# In[91]:


1 and 1


# None zero:
#     it returns the last value

# In[3]:


0 and 2


# In[4]:


3 and 2 and 0 and 5


# In[94]:


3 and 4


# In[1]:


a=20
b=10
print("addtion ", a+b)
print("subtraction ", a-b)
print("multiplication ", a*b)
print("Normal division ",a/b)
print("floor division", a//b)
print("modulor operator",a%b)
print("exponent operator ", a**0.5)
print("exponent operator ", b**0.5)


# In[2]:


a=20
b=10
print(a>b)   
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)


# In[3]:


a and b  #it returs last value


# In[4]:


1-(1i+2)


# In[1]:


100 and 200 and 300


# In[27]:


9 and 0   # if we can take combination of binary and non-zero , at that time non-zero value converted into binary vslue .. 9-->1


# # OR 

# In[2]:


0 or 1


# In[3]:


1 or 1


# In[4]:


1 or 0


# In[5]:


0 or 0


# In[6]:


1 or 0 or 0


# In[7]:


True or False


# In[8]:


False or False


# In[9]:


200 or 100


# In[10]:


100 or 200


# In[11]:


200 or 300 or 122222


# not 100 ---> it returns false
#      |
#     true
# true ---> false
# false-->true

# In[12]:


bool(0)


# In[13]:


bool(0.0)


# In[14]:


bool("")

0, 0.0 , "" ---> false
non-zero, not empty string ----> true
# In[15]:


not False


# In[16]:


not True


# In[17]:


not 0


# In[18]:


not 0.0


# In[19]:


not ""


# In[20]:


not 100


# In[21]:


not"2"


# In[22]:


not " "


# In[23]:


not"@"


# In[24]:


not "."


# In[25]:


not 0.0000000000


# In[26]:


not 0.0000000001


# # Bitwise Operators
and (&)
or  (|)
not (~)
xor (^)
left shift(<<) 
right shift(>>)
#  Bitwise and(&) operator

# In[28]:


63 & 12


# In[29]:


20 &30


# In[30]:


54 & 97


# In[31]:


4 & 2


#  Bitwise or(|) operator

# In[34]:


0|1


# In[35]:


1|0


# In[36]:


1|1


# In[32]:


26 | 12   


# In[33]:


32 | 45


# xor(^)

# if odd number of ones in the input's  side than it returns 1. else 0

# In[44]:


1^0


# In[45]:


1^1^1^0


# In[46]:


1^1


# In[47]:


1^0^1


# In[48]:


21^33


# In[49]:


33^21


# leftshift operator(<<)
to shift lest side 
n*(2^m)
n--->number
m--> no of shifts
12 ----> 12*(2^3)  for 3 shifts  ----> 12*8=96
# In[53]:


12<<3


# In[54]:


10<<6


# In[55]:


6<<2


# Rightshift(>>)
to shift rightside
n/(2^m)
# In[56]:


16>>2


# In[ ]:


ignore decimal values and return only quotient value 


# In[57]:


4>>4


# In[58]:


100>>4


# not(~)

# ~x=-(x+1)

# In[1]:


~10


# In[2]:


~-10


# **4.Identity operators**

# it compare addresses 
is
is not
# In[60]:


a=10
b=10
id(a)


# In[61]:


id(b)


# In[62]:


a is b


# In[63]:


a=1219
b=2386
a is b


# In[64]:


id(a)


# In[65]:


id(b)


# In[5]:


num=2.5
num1=2.5
num is num1


# In[6]:


id(num)


# In[7]:


id(num1)


# In[67]:


2.5 ==2.5


# In[68]:


2.50 ==2.5


# In[69]:


n1=2.5
n2=2.50
n1==n2


# In[70]:


id(n1)


# In[71]:


id(n2)


# In[72]:


n1 is n2


# In[73]:


a= True
b= True
a is b


# In[74]:


a="hello"
b="hello"
a is b

int, string, boolean ---> if value is same , is operator returns True.
float ---> if values are same, but the addres is different so, is operator returns to False.
# **Membership operators**
in
not in"Hello world" 
"h" in "Hello world" --->false
"H" in "Hello world" ----> True
# In[75]:


name= "Lakshmi"
"s" in name


# In[77]:


"hello" in name


# In[78]:


"La " in name


# In[79]:


"" in name


# In[ ]:


name= "innomatics research lab"


# In[3]:


a=10
b=10
a is b


# In[4]:


id(a)


# In[5]:


id(b)


# In[6]:


id(a) is id(b)


# In[ ]:




