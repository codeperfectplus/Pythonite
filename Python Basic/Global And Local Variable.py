#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Global variable can access anywhere inside or outside the function
'''
value = 10


# In[11]:


# Local vriable only Can Be Access InSide the function.
def sum(value,b=20):
    value = 15
    return value + b


# In[10]:


sum(value)  # function Value with Local varible


# In[8]:


value   # Again Global variable


# In[ ]:




