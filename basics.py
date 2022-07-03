#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("nagarajan")


# In[2]:


print("Multi-line commenting")


# In[3]:


a = -5
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))


# In[4]:


a = 5

def f():
    print('Inside f() : ', a)

def g():
    a = 2
    print('Inside g() : ', a) 

def h():
    global a
    a = 4      
    print('Inside h() : ', a)  

print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

