#!/usr/bin/env python
# coding: utf-8
     FILES
       |
--------------
|             |
text file    binary files
1.string      1.images
              2.videos
              3.audio
              4.voicetext files---> .txt-->creaate a file. if there is no file.
if the file is created. we can 1.read,2.write,3.appendfile=pen(filename/file path/mode)
mode-->action(i.e read,write,create,append)
# In[5]:


file=open(r"C:\Users\laxmi\OneDrive\Desktop\AWS_Academy_Graduate___AWS_Academy_Cloud_Architecting_Badge20220110-53-1b7jtp3.pdf","r")


# In[8]:


file.read()


# # File Object Properties

# In[2]:


f = open("test.txt", 'w')

print('File Name: ', f.name)

print('File Mode: ', f.mode)

print('Is file readable: ', f.readable())

print('Is file Writable: ', f.writable())

print('Is file closed: ', f.closed)
print(f.seekable())

f.close()

print('Is file closed: ', f.closed)


# # modes
"r"  open for reading(only read, loading/reading the data in the file)
"w" open for writing(only write, we can add data to file)
"x" creating a new file and open it for writing
"a"  open for writing, appending to the end of the file if it exists(add data to existing data)
"b"  binary mode
"r+" read then writing
"w+" write then reading
"a+" writing and reading
# # Creating file

# In[20]:


dat1=open("data1.txt","x")


# In[21]:


dat1.writelines("Hello this is the writing process using mode as a x")


# In[22]:


dat1.close()


# In[31]:


file3=open("python1.txt","x")


# In[32]:


file3.writelines("python is high programming language and it is having some featurs, i.e 1.easy to learn,2.object oriented")


# In[34]:


file3.close()


# # Reading file

# In[35]:


file=open("data1.txt","r")


# In[36]:


file.readlines()


# In[38]:


file.writelines("hii")


# In[39]:


file.close()


# In[40]:


file.writelines("hii")


# In[41]:


fil1=open("data1.txt","w")


# In[43]:


fil1.writelines("hello i am data science")  #write always overwrites/


# In[46]:


fil1.readlines()


# In[47]:


fil1.close()


# **READ AND WRITE**

# In[49]:


file=open("data1.txt","r+")


# In[50]:


file.readlines()


# In[51]:


file.writelines("and aloso python programming")


# In[52]:


file.close()


# **Write and Read**

# In[53]:


file1=open("data1.txt","w+")


# In[54]:


file1.writelines("hello data science") #attributes are given first priority


# In[55]:


file1.close()


# **A+**

# In[56]:


file2=open("data1.txt","a+")


# In[57]:


file2.writelines("hello i am python programming")


# In[60]:


file2.close()


# In[1]:


f=open("data1.txt","r")


# In[3]:


f.read()  # it reads the end of the text. there is no data . that's why it gives the empty string


# In[4]:


f.tell()


# In[5]:


f1=open("data1.txt","w")


# In[6]:


f1.writelines(["hello how are you"])


# In[7]:


f1.close()


# In[8]:


f2=open("data1.txt","r")


# In[10]:


f2.read()


# In[11]:


f2.tell()


# In[12]:


f3=open("data1.txt","r")


# In[13]:


f3.read()     #it show the entaire the data which is present in the file.


# In[14]:


#if we want to remove the \n. use the print() function


# In[18]:


file=open("regex.txt","r")


# In[16]:


file.read()


# In[19]:


print(file.read())  # it returns the data with line by line. remove the \n"


# In[22]:


file1=open("regex.txt","r")  # it reads the only one line. and returns the only one one line
print(file1.readline())
file1.close()


# In[23]:


file2=open("regex.txt","r")
print(file2.readlines())   #it reads the all lines and return the same data. not line by line.
file2.close()

r+ --> we can read and write.
# In[28]:


f4=open("regex.txt","r+")


# In[29]:


f4.read()


# In[30]:


f4.write("hello world")


# In[31]:


f4.close()


# # Write

# **w,w+**

# In[33]:


f5=open("data1.txt","w")


# In[35]:


f5.write("python programming language")


# In[36]:


f5.close()


# In[50]:


f6=open("data1.txt","w+")


# In[51]:


f6.writelines(["hello\n","how are\n","hii\n"])  #if we want to write data in line by line, we can use the write lines()


# In[53]:


f6.close()


# **csv=comma separated values**

# In[59]:


f7=open(r"C:\Users\laxmi\Downloads\redacted-2022-december-31-wprdc.csv","r")


# In[57]:


print(f7.read())


# In[60]:


print(f7.readline())


# In[70]:


file7=open("data1.txt","r+")


# In[71]:


file7.seek(28)  # if we want to write some data at particulare position. it shift the cursor to the partucular position


# In[72]:


file7.tell()  #it returns the where the cursor is present.


# In[73]:


file7.write("i am data analyst too")


# In[74]:


file7.close()


# 1. open
# 2. mode/action
# 3. close()

# # Genarator function

# In[78]:


with open("gen.txt","w") as file:  #as means aliasing.
    file.write("here i'm working on files without close function")


# In[79]:


with open("gen.txt","r") as file:
    print(file.read())


# In[80]:


with open("cls.txt","a") as file1:
    file1.writelines(["hii\n","hello\n","how are you\n"])


# In[81]:


with open("cls.txt","r") as file1:
    print(file1.read())


# In[84]:


with open("regex.txt","r") as f:
    print(f.read())


# # Binary file

# In[94]:


import os
os.getcwd()


# In[95]:


file=open("inn.txt","w+")


# In[96]:


file.write("file handling in python")


# In[97]:


file.close()


# In[98]:


import shutil  #if we want to change the file into oter directory. use the shutil.


# In[100]:


shutil.move("inn.txt",r'C:\Users\laxmi\OneDrive\Documents')


# In[102]:


import os 
os.getcwd()


# In[104]:


with open ("featurs.txt","a+") as fl1:
    fl1.writelines(["Free and Open Source.\n","Easy to code.\n","Object-Oriented Language.\n","GUI Programming Support.\n","High-Level Language.\n"])


# In[107]:


with open("featurs.txt","r") as fl1:
    print(fl1.read())


# In[119]:


import os
os.getcwd()


# In[118]:


import shutil


# In[1]:


shutil.move()


# In[2]:


f1=open("updated_data.txt",'r')
f1.read()


# In[3]:


f1.close()


# In[4]:


f2=open("updated_data.txt","a+")
f2.read()

x=it creates a new file(if the file already exist,it will throw an error)
w=("sample.txt","w")
write()--> if already exists, thst adds the data(overwrite the data)
    \--->if there is no file automatically it creates,
a=("sample.txt","w")
append()--> if already exists, thst adds the data,
    \--->if there is no file automatically it creates,
# **file:** collection of elements, the elements are string data type only.

# **create a file**

# In[1]:


x=open("sample.txt","x")


# In[6]:


w=open("sample_1.txt","w")
w.close()


# In[4]:


a=open("sample_2.txt","a")
a.close()


# **delete the file**

# In[7]:


import os
os.remove("sample_1.txt")


# In[9]:


os.remove("sample_2.txt")


# In[10]:


x.close()


# In[11]:


os.remove("sample.txt")


# **reading the file**

# read(): it shows the entaire data present in the file at a         time
# 
# readline():shows single line at a time
# 
# readlines(): shows the data in the list data i.e[data]

# In[12]:


file=open("python.txt","w")


# In[13]:


file.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule")


# In[14]:


file.close()


# In[30]:


f=open("python.txt","r")


# In[17]:


f.write("hello")


# In[18]:


f.readable()


# In[19]:


f.writable()


# In[20]:


f.read()


# In[23]:


f.readline()  # the cursore position at end of the data. that why it returns the empty string


# In[22]:


f.tell()


# In[25]:


f.readline()


# In[31]:


f.readlines()


# **writing to file**

# In[38]:


file=open("python.txt","w")


# write()-->add the entaire data
# 
# writeline() adds the data as the new line
# 
# writelines()-->add multiple lines

# In[33]:


file.write("i am learning python")


# In[34]:


file.close()


# In[40]:


file.writelines(["hello world\n","how are you\n"])


# In[41]:


file.close()


# **Adding the data without overriding**

# In[42]:


file=open("python.txt","a")


# In[43]:


file.append()


# In[44]:


file.writelines("we are adding new data to check append method. it will not override the existed data\n")


# In[45]:


file.close()


# In[46]:


with open("python.txt","w") as f:
    f.write("I am deleting existed data")


# **Cursor position**

# In[55]:


file=open("python.txt","w+")


# In[48]:


file.tell()


# In[50]:


file.seek(30)  #--> shifting the cusore position


# In[51]:


file.write("this is shifted data")


# In[52]:


file.close()


# In[61]:


file=open("python.txt","w")


# In[62]:


file.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule")


# In[63]:


file.close()


# In[74]:


#delete the data from the file
f1=open("python.txt","w")


# In[75]:


f1.write("")


# In[76]:


f1.close()

