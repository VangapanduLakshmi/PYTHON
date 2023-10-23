#!/usr/bin/env python
# coding: utf-8

# # Collection Data types

# 1. to store more than single value
# 2. we can store homogenous/heterogenous 
list
tuple
set (frozen set)
dictionary
# # List

# In[1]:


lst1=["innomatics","research","labs"]
print(lst1)


# In[2]:


type(lst1)


# In[4]:


len(lst2)


# In[6]:


lst2[3]


# In[18]:


lst3=["laxmi","lakshmi","lucky","rajlaxmi","potato"]


# In[8]:


print(lst3)


# In[9]:


type(lst3)


# In[10]:


len(lst3)


# In[11]:


lst3[3]


# In[12]:


lst3[-1:-3:-1]


# In[14]:


lst3[2:]


# In[15]:


lst3[::-1]


# In[17]:


lst3[-1:-5:-1]


# In[3]:


lst2=[1,2,3,4,5]
print(lst2)


# In[22]:


for i in range(len(lst3)):
    if(lst3[i].startswith("p")):
        print(lst3[i])


# **characteristics/attributes of list**
1. Mutable   #modify/change the original data
2. it follwos the ordered
3. allow's the duplicates elements
4. index based
# In[24]:


lst4=[1,2,3,4,5,6,1,2,3]  #allows the duplicates elements


# In[25]:


print(lst4)


# In[27]:


lst4[-1]  #index based(ordered)


# In[28]:


orig=[1,2,3,4,5]


# In[29]:


orig.append("bscdfas")   #string is immutable
print(orig)


# In[1]:


name="ehdgisjxn"


# In[5]:


name.replace("e","r")


# In[6]:


name


# In[40]:


lst3


# In[41]:


lst3.append("raw")


# In[42]:


lst3


# In[20]:


lst3=[0,2,4,6,8,10]


# In[21]:


lst3.insert(2,9)


# In[22]:


print(lst3)


# In[47]:


lst3.extend(lst2)


# In[48]:


print(lst3)


# In[49]:


lst4=[0,2,4,6,10]


# **List functions/methods**

# In[24]:


num=[1,2,3,4,5,6]


# In[51]:


num.append(7)  # adding the element/value at the end of the list
print(num)


# In[52]:


num.clear()   #clears the all the values and returns the empty list


# In[53]:


print(num)


# In[9]:


num=[1,2,3,4,5,6,6]


# In[11]:


num1=num.copy()       #it returns the original list


# In[12]:


num1.append(6)
print(num1)


# In[13]:


num


# In[19]:


s= "scvbdsdjncfr"


# In[15]:


num.count(6)  #frequency of occurance


# In[8]:


num.extend([7,8,9,10])
print(num)


# In[64]:


num.index(3)


# In[65]:


num.insert(3,10)  #if we want to add an value at the particular location/positin/index than use the insert function


# In[66]:


print(num)


# In[1]:


val=[1,2,3,4,5]
val.insert(3,6)


# In[2]:


print(val)


# In[3]:


val.pop(3)  #removing an value using index based


# In[4]:


val.pop() #if we don't provide the value, than it delete the last element in the list


# In[5]:


print(val)


# In[74]:


num.remove(10)#removing an value using elements in the list and if the list is having duplicate elements,than it revomes first occurance value


# In[26]:


num.remove(2)


# In[75]:


print(num)


# In[76]:


num.sort()


# In[77]:


print(num)


# In[27]:


task=[2,4,6,"even",'odd',2.3,5,6,2]


# In[79]:


task.append("true")
print(task)


# In[80]:


task1=task.copy()
print(task1)


# In[81]:


task


# In[82]:


task1.clear()
print(task1)


# In[7]:


task


# In[84]:


task.count(2)


# In[28]:


task.extend(['false',9,8,7,5.7])
print(task)


# In[87]:


task.index(0)


# In[86]:


task.index("even")


# In[31]:


task.pop()
print(task)


# In[9]:


task.remove(0)


# In[89]:


task.remove("even")
print(task)


# In[91]:


task.reverse()


# In[92]:


print(task)


# In[93]:


task.sort()   #if we want to sort the  heterogenous elements  in the list, it returns the type error. because it not supported b/w diff data types.
print(task)


# In[105]:


lst=[]


# In[109]:


name=input()
marks=int(input())
city=input()


# In[110]:


lst.append(name)
lst.append(marks)
lst.append(city)


# In[111]:


lst


# In[17]:


list1=[1,2,3,4,5]
list2=[1,2,3,4,5]


# In[19]:


list1.


# **membership operators**

# In[8]:


1 in list1


# In[9]:


"1" in list1


# In[10]:


1 not in list1


# **identity operators**

# In[16]:


list1 is list2         


# In[17]:


list1[0] is list2[0]


# In[3]:


list3=[1.1,1.2,1.3]
list4=[1.1,1.2,1.3]


# In[5]:


list3[0] is list4[0]


# In[13]:


list3


# In[34]:


lst = list([1,2,3,4])
lst


# # TUPLE

# **Attributes of tuple**
1. immutable
2. ordered
3. duplicates are allowed
4. index basedtwo ways to create tuple
1. using ()
2. tuple([])
# In[25]:


t=(1,2,3,4)         #using parathecis
print(type(t))
print(t)


# In[26]:


t1=tuple([1,2,3,4])   #from list
t1


# In[27]:


t2=1,2,3,4,5   #packing


# In[28]:


type(t2)


# In[29]:


t2


# **Method/fuctions on tuple**

# tuples have only two methods, there are count() and index()

# In[20]:


name= ("ramesh","rajesh","prakash","rajesh")


# In[21]:


name.count("ramesh")


# In[22]:


name.index("rajesh")


# In[23]:


name.index("rajesh",2)


# **Associate operators**

# In[15]:


x=1
y=1


# In[16]:


x=x+1
print(x)


# In[17]:


y+=1
y


# In[18]:


names=("laxmi","lucky","lakshmi")
names.append("rajlakshmi")


# In[19]:


names.insert(2,"lucky")


# In[33]:


names=(9,3,8.5)


# In[34]:


names1=(4,5,6)


# In[19]:


val=names+names1  #contatination


# In[29]:


names-2


# In[44]:


names*2  # it returns the repitation


# In[35]:


names*names1


# In[46]:


a=(1,2,3,"lakshmi")
b=(1,2,3,"lakshmi")
a is b


# In[43]:


a[0]


# In[44]:


a[1:]


# In[ ]:


a[0] is a[0]


# In[46]:


1 in a


# In[47]:


1 not in a

list                 tuple   
  |                     |
mutable              immutable              
[]                    ()
methods (11)         method(2)(count, index)list               tuple                   set
  |                  |                      |
mutable           immutable              mutable
ordered           ordered                not ordered
duplicates        duplicates             no duplicates
index             index                  not follow index
# # SET

# **Attributes of set data type**

# In[48]:


names={"laxmi","lakshmi","lucky"}
type(names)


# In[49]:


len(names)


# In[50]:


names.add(3)


# In[51]:


names


# In[52]:


names.add("laxmi")    #duplicates are not allowed.


# In[53]:


names


# In[54]:


names[0]  #unordered.


# **methods**

# In[10]:


name1={"lakshmi","laxmi","lucky",2}


# In[1]:


s = {}
print(type(s))


# In[2]:


name2=name1.copy()


# In[3]:


name2


# In[4]:


name1


# In[5]:


name2.clear()
name2


# In[6]:


name1


# In[7]:


name1.add("rajlakshmi")
name1


# In[12]:


name1.discard("laxmi")   #it removes the element. if there is no element, it deosn't throw any error.
name1


# In[9]:


name1.discard("ra")
name1


# In[10]:


name1.remove("lucky")  #it removes the element. if there is no element, it's throw  error.
name1


# In[11]:


name1.remove("raj")


# In[7]:


a = {1,1,1,False}
print(a)


# In[41]:


name3={1,2,3,5}
name4={8,9,10,1,2,3,5}
name3.difference(name4)


# In[17]:


name4.difference(name3)       #remove the comman elements


# In[18]:


name3.add(10)
name3


# In[19]:


name3


# In[18]:


name3.pop(7) 
name3 #in set data type the pop() is remove the first element from the set.


# In[21]:


name3.update({11,12,13,14})  #if we wnat to extand the set we can use the update().
name3


# In[30]:


set3={1,2,3,4,5}


# In[3]:


set4=set()   #empt set
type(set4)


# In[4]:


set5={}
type(set5)


# In[5]:


set3


# In[7]:


set3.difference(set4)


# In[8]:


set3


# In[32]:


set3


# In[32]:


set3.difference_update(set4)  #it reflects the original data.


# In[33]:


set3


# In[36]:


set3.isdisjoint(set4)  #if the two sets are having comman elents it returns the false. else it returns true.


# In[37]:


set4


# In[26]:


set3.union(set4)


# In[14]:


set3.intersection(set4)


# In[27]:


set3


# In[40]:


set1={1,2,3,4,1,2,5,6,7}
len(set1)


# In[42]:


name3.update(name4)


# In[29]:


set3


# In[44]:


name3.issubset(name4)


# In[46]:


name4.issuperset(name3)


# In[ ]:





# In[ ]:





# In[ ]:





# # DICTIONARY

# dic={key:value}

# In[41]:


dic1={0:"raju",1:"ramesh",2:"rajesh",3:"rakesh"}   #normal method
#{key:value}


# In[42]:


type(dic1)


# In[43]:


len(dic1)


# In[44]:


dic1


# In[45]:


id(dic1)


# In[46]:


dic2=dict([(1,'r'),(2,'a'),(3,'j'),(4,'u')])   #using dict() 
#dict([(key,value)])


# In[47]:


dic2


# In[49]:


fruits=dict([("apple",20),("banana",10),("kiwi",30),("orange",15)])
fruits


# In[2]:


fruits1={"apple":20,"banana":10,"kiwi":30,"orange":15}
fruits1


# In[60]:


list1=["apple","banana","mango"]
price=[20,30,40]


# In[61]:


k=dict(zip(list1,price))


# In[62]:


k


# In[63]:


empty_dic={}


# In[64]:


empty_dic


# In[65]:


type(empty_dic)


# In[86]:


fruits


# In[87]:


fruits["mango"]=40
#variable_name[key]=value.


# In[88]:


fruits


# In[89]:


fruits["grape","grape1"]=[50,60]


# In[90]:


print(fruits)


# In[91]:


fruits[0]


# In[92]:


fruits["banana"]


# In[93]:


fruits.keys()


# In[95]:


fruits.values()  #returns list of values.


# In[96]:


fruits.fromkeys(['apple', 'banana', 'kiwi', 'orange', 'mango', ('grape', 'grape1')],0.5)


# In[98]:


print(fruits)


# In[99]:


fruits.get("apple")


# In[100]:


fruits["apple"]


# In[ ]:





# In[101]:


fruits.items()  #combination of both keys and values


# In[51]:


fruits.pop("banana")  #it effects the original data


# In[104]:


print(fruits)  


# In[106]:


fruits.popitem()   #it removes the last item   
#two times runs that's why it remove the mango


# In[107]:


fruits


# In[108]:


fruits.update({"mango":40})


# In[109]:


fruits


# In[110]:


#keys are unique/not allowed duplicates, and it returns the ubdated last value
#values are duplicate


# In[111]:


f={1:"r",2:"a",3:"j",1:"u"}


# In[112]:


f


# In[113]:


f={1:"r",2:"a",3:"a",1:"u"}


# In[114]:


f

1.{key:value}
2.dict([(key:value)])
3.lst1=[]
  lst2=[]
  dict(zip(lst1,lst2))
# # typecasting

# In[117]:


lst=[1,2,3,4,5,1,2]
type(lst)


# In[118]:


set(lst)  #duplicates are removed


# In[119]:


tuple(lst)  #allows the duplicates


# In[ ]:


tuple1=(1,2,3,4,5,6,1,2,3,4)


# In[8]:


a = "Hello"
b ="Hello"
a is b

