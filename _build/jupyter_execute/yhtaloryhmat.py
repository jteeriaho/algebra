#!/usr/bin/env python
# coding: utf-8

# # Yhtälöryhmät

# ## 1. asteen yhtälöt  
# 
# ### Samankantaisten potenssien tulo  

# ````{margin} 
# Potenssien laskukaavoja:
# 
# 1. $x^mx^n=x^{m+n}$   
# 
# 2. $\frac{x^m}{x^n}=x^{m-n}$   
# 
# 3. ${x^m}^n=x^{mn}$   
# 
# 4. $x^0=1$   
# 
# 5. $x^{-n}=\frac{1}{x^n}$   
# 
# 6. ${(\frac{x}{y})}^{-n}={(\frac{y}{x})}^{n}$
# 
# 7. ${x y}^n=x^n y^n$   
# 
# 8. ${(\frac{x}{y})}^n=\frac{x^n}{y^n}$  
# 
# ````

# ```{tip}
# $x^n\cdot x^m = x^{n+m}$
# ```

# ```{admonition} Sievennä $ a^5\cdot a^7$
# :class: toggle
# $ a^5\cdot a^7 = a^{5+7}=a^{12}$
# ```

# ## 1. asteen epäyhtälöt

# ```{tip}
# $\frac {x^n}{x^m} = x^{n-m}$ 
# ```

# ```{admonition} Sievennä $ \frac{z^7}{z^3}$
# :class: toggle
# $ \frac{z^7}{z^3} = z^{7-3}=z^4$
# ```

# ## Suoran yhtälö ja lineaarinen malli

# ```{tip}
# $ x^{-n} = \frac {1} {x^n}$  
# ```

# ```{admonition} Sievennä $ {(\frac {2}{3})}^{-3}$
# :class: toggle
# $ {(\frac {2}{3})}^{-3} = {(\frac {3}{2})}^{3}=\frac {3 ^3}{2^3} =\frac {27}{8}$ 
# ```

# ## Monivalintatesti

# In[1]:


from jupyterquiz import display_quiz

display_quiz('mchoice1.json')


# In[2]:


get_ipython().system(' jupyter nbconvert --to html Jquizz.ipynb')

