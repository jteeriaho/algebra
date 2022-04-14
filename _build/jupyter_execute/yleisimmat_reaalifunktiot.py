#!/usr/bin/env python
# coding: utf-8

# # Kokeiluja

# In[1]:


# shared imports 
from myst_nb import glue
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 12 * np.pi, 200)
y = np.sin(x)+np.sin(2*x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# In[9]:


from ipywidgets import interact
from sympy.ntheory import isprime
    # use interact decorator to decorate the function, so the function can receive the slide bar's value with parameter x.\n",
@interact(x=(0, 100))
def alkulukuko(x):
    print("The primality of ",x," is ",isprime(x))


# In[10]:


import sympy as sp
x, y = sp.symbols('x y')  
expr = y - x **2 + 2
ratkaisu = sp.solveset(expr, x)
print("Rj =", ratkaisu)


# In[4]:


get_ipython().run_cell_magic('html', '', '<iframe src=vektorit.htm width=100% height=500></iframe>')

