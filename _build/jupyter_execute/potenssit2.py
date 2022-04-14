#!/usr/bin/env python
# coding: utf-8

# # Potenssien laskusäännöt

# ## Potenssin määritelmä  
# 
# 
# ```{important}
# $a^n = \underset{n\hspace{2mm} kpl} {a\cdot a\hspace{2mm}\cdot \hspace{2mm} ...\hspace{2mm}\cdot \hspace{2mm}a}$
# ```

# ## Potenssien laskulakeja  
# 
# ### Samankantaisten potenssien tulo 

# ```{tip}
# $x^n\cdot x^m = x^{n+m}$
# ```

# ```{admonition} Sievennä $ a^5\cdot a^7$
# :class: toggle
# $ a^5\cdot a^7 = a^{5+7}=a^{12}$
# ```

# ### Samankantaisten potenssien osamäärä 

# ```{tip}
# $\frac {x^n}{x^m} = x^{n-m}$ 
# ```

# ```{admonition} Sievennä $ \frac{z^7}{z^3}$
# :class: toggle
# $ \frac{z^7}{z^3} = z^{7-3}=z^4$
# ```

# ###  Potenssin korottaminen potenssiin

# ```{tip}
# $ (x^n)^{m} = x^{n m}$  
# ```

# ```{admonition} Sievennä $ (a^7)^{3}$
# :class: toggle
# $ (a^7)^{3}$ = $a^{7\cdot 3}$ = $a^{21}$
# ```

# ### Tulon korottaminen potenssiin

# $ {(\frac {z} {y})}^{2}$

# ```{tip}
# $ (x y)^{m} = x^n y^m$  
# ```

# ```{admonition} Sievennä $ (a\cdot b)^{3}$
# :class: toggle
# $ (a\cdot b)^{3}$ = $a^3\cdot b^3$ 
# ```

# ### Osamäärän korottaminen potenssiin

# ```{tip}
# $ {(\frac {x} {y})}^{m} = \frac {x^n} {y^m}$  
# ```

# ```{admonition} Sievennä $ {(\frac {z} {y})}^{2}$
# :class: toggle
# $ {(\frac {z} {y})}^{2} = \frac {z^2} {y^2}$ 
# ```

# ## Negatiivinen potessi

# ```{tip}
# $ x^{-n} = \frac {1} {x^n}$  
# ```

# ```{admonition} Sievennä $ {(\frac {2}{3}}^{-3}$
# :class: toggle
# $ {(\frac {2}{3})}^{-3} = {(\frac {3}{2})}^{3}=\frac {3 ^3}{2^3} =\frac {27}{8}$ 
# ```

# ## Monivalintatehtäviä potenssien laskusäännöistä

# In[1]:


from jupyterquiz import display_quiz

display_quiz('mchoice1.json')

