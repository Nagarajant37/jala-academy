#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Python:
    staticVariable = 9 
print(Python.staticVariable)


# In[3]:


Python.staticVariable = 12
print(Python.staticVariable)


# In[4]:


instance = Python()
print(instance.staticVariable)


# In[5]:


instance.staticVariable = 15
print(instance.staticVariable) 
print(Python.staticVariable) 


# In[ ]:




