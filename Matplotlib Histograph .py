#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


mens_weight =[62,65,70,73,85,92,97,105,120]
women_weight =[45,41,47,62,70,86,90,100,63]


# In[33]:






plt.xlabel("No of people",)
plt.ylabel("Weight ")
plt.hist([mens_weight,women_weight],bins=[47,65,80,97],rwidth=0.95,color=["blue","orange"],label=["Men","Women"])

plt.legend(shadow=True)


# In[ ]:





# In[ ]:





# In[ ]:




