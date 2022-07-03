#!/usr/bin/env python
# coding: utf-8

# In[1]:



num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
  

sum = float(num1) + float(num2)  

min = float(num1) - float(num2)  

mul = float(num1) * float(num2)  

div = float(num1) / float(num2)  

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  

print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  

print('The division of {0} and {1} is {2}'.format(num1, num2, div))


# In[2]:


a = 0
a += 1
a = a+1
print('The value of a is ',a)

print("INCREMENTED FOR LOOP")
for i in range(0, 5):
   print(i)

for i in range(4, -1, -1):
   print(i)


# In[3]:


a = input('Enter first number: ')
b = input('Enter second number: ')
if a==b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")
    


# In[4]:


a = 4
b = 5
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)


# In[5]:


a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

if a > b: 
     print(a, "is greater ")
else:
    print(b, " is greater ")

if a < b:
     print(a, "is smaller2 ")
else:
    print(b, " is smaller ")         


# In[ ]:




