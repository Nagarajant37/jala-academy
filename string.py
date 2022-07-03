#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = 'Hello'
print(string)

string = "Hello"
print(string)

string1 = '''World'''
print(string1)

string2 = """Welcome to
           the world of Python""" 
print(string2)
print()


# In[2]:


str1 = string + string1
print("Concatenated two different strings:",str1)
print()


# In[3]:


print("length of the string:",len(str1))
print()


# In[5]:


str3 = 'kashish'
str1 = 'ish'
str2 = 'h'
print("Position of ish:",str3.index(str1))
print("Position of h:",str3.index(str2))
print()


# In[6]:


from ast import Str
import re
Substr = 'Madara'
str6 = 'Madara once said- Wake up to relity nothing goes as planned in this cursed world'
print(re.match(Substr,str6))
print()


# In[7]:


str8 = 'Itachi uchiha'
str1 = 'Madara uchiha'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)
print()


# In[8]:


string = 'Minato Namikaze'
print(string.startswith("Minato"))
print(string.endswith("kaze"))
print()


# In[9]:


str7 = 'Hello World hi'
print(str7.strip("hi"))
print()


# In[10]:


string = 'Hi World'
print(string.replace("Hi","Hello"))
print()


# In[11]:


str9 = 'hi-hello-bye'
print(str9.split("-"))
print()


# In[13]:


numb = 10
numb1 = str(numb)
print(numb1)
print(type(numb1))
print()


# In[14]:


string = 'hello'
string1 = 'WORLD'
print(string.upper())
print(string1.lower())


# In[ ]:




