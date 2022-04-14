#!/usr/bin/env python
# coding: utf-8

# # Korkolaskut

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

# ### Negatiivinen potenssi 

# > Sievennetään $\frac {x^2}{x^5}$ kahdella tavalla:  
# >
# > Supistamalla $x^2$:lla saadaan $\frac {x^2}{x^5}$ = $\frac {1}{x^3}$  
# > Samankantaisten potenssien osamäärän kaavaa käyttäen $\frac {x^2}{x^5}$=$x^{2-5}$=$x^{-3}$  
# >
# > On siten mielekästä määritellä negatiivinen potenssi $x^{-3}$ = $\frac {1}{x^3}$

# ```{tip}
# $ x^{-n} = \frac {1} {x^n}$  
# ```

# ```{admonition} Sievennä $ {(\frac {2}{3})}^{-3}$
# :class: toggle
# $ {(\frac {2}{3})}^{-3} = {(\frac {3}{2})}^{3}=\frac {3 ^3}{2^3} =\frac {27}{8}$ 
# ```

# ### Nollas potenssi

# > Sievennetään $\frac {x^4}{x^4}$ kahdella tavalla:  
# >
# > Supistamalla saadaan $\frac {x^4}{x^4}$ = $\frac {1}{1}$ = 1
# > Samankantaisten potenssien osamäärän kaavaa käyttäen $\frac {x^4}{x^4}$=$x^{4-4}$=$x^{0}$  
# >
# > On siten mielekästä määritellä nollas potenssi $x^{0}$ = 1

# ```{tip}
# $ x^{0} = 1$  kaikille reaaliluvuille x
# ```

# ```{admonition} Sievennä $ {(\frac {2}{3})}^{0}$
# :class: toggle
# $ {(\frac {2}{3})}^{0} = 1$ , koska minkä tahansa luvun 0:s potenssi on 1 
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

# ## Monivalintatesti potenssien laskusäännöistä

# In[1]:


from jupyterquiz import display_quiz

display_quiz('mchoice1.json')


# In[2]:


get_ipython().system(' jupyter nbconvert --to html Jquizz.ipynb')

