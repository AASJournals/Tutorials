
# coding: utf-8

# In[44]:

import numpy as np


# In[45]:

import matplotlib.pylab as plt


# In[46]:

get_ipython().magic(u'matplotlib inline')


# In[48]:

from astropy.table import Table


# In[49]:

data = Table.read("Fougue2007_Cephieds.fits")


# In[50]:

data


# In[56]:

fig, ax = plt.subplots()
ax.scatter(data['_RAJ2000'], data['_DEJ2000'], c=data['E(B-V)'], s=100.*data['plx'], alpha=0.5)
ax.set_xlabel('RA', fontsize=20)
ax.set_ylabel('Dec', fontsize=20)
ax.set_title('Fougue2007_Cephieds')
ax.xaxis_inverted()
ax.grid(True)
fig.tight_layout()

plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



