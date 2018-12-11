#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


x = [1400,600,300,410,250]
y = ["PG Rent","Food","Travel","Home","other"]


# In[25]:


plt.axis("equal")
plt.pie(x,labels=y,radius=1.5,autopct='%0.1f%%',shadow=True,explode=[0,0.2,0.3,0],startangle=45)


# In[11]:





# In[ ]:




