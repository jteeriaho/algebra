#!/usr/bin/env python
# coding: utf-8

# # Potenssien laskusäännöt

# ## Potenssin määritelmä  
# 
# ```{admonition} **Potenssin määritelmä**
# :class: tip
# $a^n = \underset{n\hspace{2mm} kpl} {a\cdot a\hspace{2mm}\cdot \hspace{2mm} ...\hspace{2mm}\cdot \hspace{2mm}a}$
# ```

# ## Potenssien laskulakeja    

# ```{admonition} **Samankantaisten potenssien tulo**
# :class: tip
# $x^n\cdot x^m = x^{n+m}$
# ```

# ```{admonition} Esimerkki. Sievennä $ a^5\cdot a^7$
# :class: dropdown
# $ a^5\cdot a^7 = a^{5+7}=a^{12}$
# ```

# ```{admonition} **Samankantaisten potenssien osamäärä**
# :class: tip
# $\frac {x^n}{x^m} = x^{n-m}$ 
# ```

# ```{admonition} Esim. Sievennä $ \frac{z^7}{z^3}$
# :class: dropdown
# $ \frac{z^7}{z^3} = z^{7-3}=z^4$
# ```

# > **Negatiivisen potenssin määritelmä**
# >
# > Sievennetään $\frac {x^2}{x^5}$ kahdella tavalla:  
# >
# > Supistamalla $x^2$ :lla saadaan $\frac {x^2}{x^5}$ = $\frac {1}{x^3}$  
# > Samankantaisten potenssien osamäärän kaavaa käyttäen $\frac {x^2}{x^5}$=$x^{2-5}$=$x^{-3}$  
# >
# > On siten mielekästä määritellä negatiivinen potenssi $x^{-3}$ = $\frac {1}{x^3}$

# ````{admonition} **Negatiivinen potenssi**
# :class: tip
# $ x^{-n} = \frac {1} {x^n}$  
# ```{admonition} Seuraus
# :class: tip
# Murtoluvun negatiivinen potenssi = sen käänteisluvun vastaava positiivinen potenssi    
# $ {(\frac {a}{b})}^{-n} = {(\frac {b}{a})}^{n}$
# ```
# ````

# ```{admonition} Esim. Sievennä $ {(\frac {2}{3})}^{-3}$
# :class: dropdown
# $ {(\frac {2}{3})}^{-3} = {(\frac {3}{2})}^{3}=\frac {3 ^3}{2^3} =\frac {27}{8}$ 
# ```

# > **Luvun potenssi nolla**
# >
# > Sievennetään $\frac {x^4}{x^4}$ kahdella tavalla: Supistamalla saadaan $\frac {x^4}{x^4}$ = $\frac {1}{1}$ = 1  
# >
# > Samankantaisten potenssien osamäärän kaavalla saadaan $\frac {x^4}{x^4}$ = $x^{4-4}$ = $x^{0}$ 
# >   
# > On siten mielekästä määritellä nollas potenssi $x^{0}$ = 1

# ```{admonition} **Nollas potenssi**
# :class: tip
# $ x^{0} = 1$  kaikille reaaliluvuille x
# ```

# ```{admonition} Esim. Sievennä $ {(\frac {2}{3})}^{0}$
# :class: dropdown
# $ {(\frac {2}{3})}^{0} = 1$ , koska minkä tahansa luvun 0:s potenssi on 1 
# ```

# ```{admonition} **Peräkkäiset potenssiin korotukset**
# :class: tip
# $ (x^n)^{m} = x^{n m}$  
# ```

# ```{admonition} Sievennä $ (a^7)^{3}$
# :class: dropdown
# $ (a^7)^{3}$ = $a^{7\cdot 3}$ = $a^{21}$
# ```

# ```{admonition} **Tulon korottaminen potenssiin**
# :class: tip
# $ (x y)^{m} = x^n y^m$  
# ```

# ```{admonition} Esim. Sievennä $ (2a b)^{3}$
# :class: dropdown
# $ (2a b)^{3}$ = $2^3a^3 b^3$=$8a^3 b^3$ 
# ```

# ```{admonition} **Osamäärän korottaminen potenssiin**
# :class: tip
# $ {(\frac {x} {y})}^{m} = \frac {x^n} {y^m}$  
# ```

# ```{admonition} Esim. Sievennä $ {(\frac {3z} {2y})}^{2}$
# :class: dropdown
# $ {(\frac {3z} {2y})}^{2} = \frac {3^2z^2} {2^2y^2}=\frac {9z^2} {4y^2}$ 
# ```
