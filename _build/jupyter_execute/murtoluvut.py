#!/usr/bin/env python
# coding: utf-8

# # Murtoluvut ja murtolausekkeet 

# ```{admonition} Murtoluvut ja murtolausekkeet
# :class: tip
# **Murtoluvut** ovat muotoa $\frac {m}{n}$ olevia lukuja, missä m ja n ovat kokonaislukuja.
# Lukua m sanoitaan *osoittajaksi* ja lukua n *nimittäjäksi*  
#     
# **Murtolausekkeella** tarkoitetaan tässä muotoa $\frac {P}{Q}$ olevia lauskkeita,    
# missä osoittaja P ja nimittäjä Q voivat sisältää lukujen lisäksi parametrejä ja muuttujia.
# 
# ```

# ## Murtolukujen ja -lausekkeiden laskusääntöjä  

# ```{admonition} Murtolukujen ja lausekkeiden kertolasku
# :class: tip
# Kertolaskussa osoittajat ja nimittäjät kerrotaan keskenään
# $\frac{a}{b}\cdot \frac{c}{d}=\frac{a\cdot c}{b\cdot d}$
# ```

# ````{admonition} Esim. Laske $\frac{2}{7}\cdot \frac{3}{5}$
# :class: dropdown
# Vastaus $\frac {6}{35}$
# ```{admonition} Ratkaisu
# :class: dropdown
# $ \frac{2}{7}\cdot \frac{3}{5}=\frac{2\cdot 3}{5\cdot 7}=\frac {6}{35}$
# ```
# ````

# ````{admonition} Esim. Laske $\frac{2b}{a}\cdot \frac{3a^2}{14x}$
# :class: dropdown
# Vastaus $\frac {3ab}{7x}$
# ```{admonition} Ratkaisu:  
# :class: dropdown
# Osoittajat ja nimittäjät yhdistetään yhdeksi murtolausekkeeksi   
# $ \frac{2b}{a}\cdot \frac{3a^2}{14x}=\frac{6a^2b}{14ax}=\frac {3ab}{7x}$
# ```
# ````

# ```{admonition} Murtolukujen ja -lausekkeiden jakolasku
# :class: tip
# Jakolaskussa osoittaja kerrotaan nimittäjän käänteisluvulla
# $\frac{\frac{a}{b}}{\frac{c}{d}}=\frac{a}{b}\cdot \frac{d}{c}$ 
# ```

# ````{admonition} Esim. Laske $ \frac{\frac{2}{7}}{\frac{3}{5}}$
# :class: dropdown
# Vastaus $\frac{10}{21}$
# ```{admonition} Ratkaisu
# :class: dropdown
# $ \frac{\frac{2}{7}}{\frac{3}{5}}=\frac{2}{7}\cdot \frac{5}{3}=\frac{10}{21}$
# ```
# ````

# ````{admonition} Esim. Laske $ \frac{2h}{t}:\frac{2\pi rh}{5t^2}$
# :class: dropdown
# Vastaus: $\frac{5t}{\pi r}$
# ```{admonition} Ratkaisu:
# :class: dropdown
# Jakolasku suoritetaan kertomalla jakajan käänteisluvulla   
# 
# $ \frac{2h}{t}\cdot \frac{5t^2}{2\pi r h}=\frac{5t}{\pi r}$
# ```
# ````

# ### Pienin yhteinen jaettava pyj(m,n)

# > Murtolukujen yhteen- ja vähennyslaskussa pitää murtoluvut ensin "laventaa samannimisiksi",   
# > jolloin niille tulee yhteiseksi nimittäjäksi murtolukujen nimittäjien *pienin yhteinen jaettava*
# > 
# > Lukujen m ja n pienin yhteinen jaettava **pyj(m,n)** on pienin kokonaisluku, joka on jaollinen 
# > sekä luvulla m, että n

# ```{admonition} Algoritmi pienimmän yhteisen jaettavan **pyj(m,n)** laskemiselle 
# :class: tip
# 1. Muodosta lukujen m ja n *alkulukuhajotelmat* (=esitä m ja n alkulukujen potenssien tulona)
# 2. Valitse pyj:n kutakin lukujen m ja n alkutekijää suurin potenssi, mikä esiintyy lukujen
# m ja n alkulukuhajotelmissa
#     ```{admonition} Esim.  Laske pyj(42,12)
#     :class: tip
#     1. Alkulukuhajotelmat:  $ 42 = 7\cdot3\cdot2 \hspace{5mm}    12=2^2\cdot3 $
#     2. pyj(42,12) = $7\cdot3\cdot2^2$ = 84   *(tekijöitä 7,3 ja 2 otetaan maksimimäärät)*
#     ```
# ```

# ```{admonition} Laske pyj(20,14)
# :class: dropdown
# 1. Alkulukuhajotelmat:  $ 20 = 5\cdot2^2   \hspace{5mm}   14=2\cdot7 $
# 2. pyj(20,14) = $5\cdot7\cdot2^2$ = 140  *(tekijöitä 7,5 ja 2 otetaan maksimimäärät)*
# ```

# ###  Murtolukujen supistettu muoto

# Esimerkiksi $\frac {20}{12}$ , $\frac {10}{6}$ ja $\frac {5}{3}$ ovat yksi ja sama murtoluku.   
# Viimeinen muoto $\frac {5}{3}$ on luvun supistettu muoto, jossa osoittalla ja nimittäjällä  
# ei ole enää yhteisiä tekijöitä.  

# ###  Supistaminen

# Supistamisessa osoittaja ja nimittäjä jaetaan tekijöihin, ja supistetaan yhteiset tekijät pois.   
# Esim.   $\frac {20}{12}$  = $\frac {4 \cdot 5}{4 \cdot 3}$ = $\frac {5}{3}$

# ```{admonition} Supistaminen
# :class: tip
# $\frac {c \cdot a}{c \cdot b}$ = $\frac {a}{b}$  
# ```

# ```{admonition} Esim. Supista $ \frac {72} {30} $
# :class: dropdown
# $ \frac {72} {30} = \frac {3^2*2^3} {3*2*5} = \frac {12} {5} $
# ```

# ```{admonition} Esim. Supista $ \frac {2\pi r+3r} {5r} $
# :class: dropdown
# Osoittajassa voidaan r ottaa yhteiseksi tekijäksi    
# 
# $ \frac {(2\pi+3)r} {5r} = \frac {2\pi + 3} {5} $
# ```

# ```{admonition} Esim. Supista $ \frac {x+3} {x^2-9} $
# :class: dropdown
# Nimittäjä esitetään tulomuodossa käyttäen kaavaa $a^2-b^2=(a-b)(a+b)$     
# 
# $ \frac {x+3} {(x-3)(x+3)} = \frac {1} {x-3} $
# ```

# ```{warning} 
# Summasta ei voi supistaa!
# $ \frac {x + 5} {x} \neq \frac {1+5} {1} $
# 
# ```

# ### Murtolukujen yhteen- ja vähennyslasku

# ```{admonition}   Murtojen yhteen- ja vähennyslasku
# :class: tip
# 1. Lavenna murtoluvut samannimisiksi   
#     a. laske murtolukujen nimittäjien pienin yhteinen jaettava pyj      
#     b. käytä laventajina lukuja *pyj/nimittäjä1*, *pyj/nimittäjä2*, ...    
# 2. Suorita yhteen- ja vähennyslaskut osoittajien välillä     
# 3. Muunna tulos supistettuun muotoon, mikäli tarpeen    
# ```

# ````{admonition} Esim. Sievennä $ \frac {1} {3} + \frac {3} {2} $
# :class: dropdown
# Vastaus: $\frac {11} {6}$
# ```{admonition} Ratkaisu:
# :class: dropdown
# Lavennetaan luvut siten, että uudeksi nimittäjäksi tulee pyj(2,3) eli 6   
# 
# $ \frac {2} {6} + \frac {9} {6} = \frac {9+2} {6} = \frac {11} {6}  $
# ```
# ````

# ````{admonition} Esim. Sievennä $ \frac {1} {a} - \frac {1} {a-1} $
# :class: dropdown
# Vastaus: $-\frac {1} {a(a-1)}  $
# ```{admonition} Ratkaisu:
# :class: dropdown
# 
# Lavennetaan luvut siten, että uudeksi nimittäjäksi tulee pyj(a,a-1) eli a(a-1)   
# 
# $ \frac {a-1} {a(a-1)} - \frac {a} {a(a-1)} = \frac {a-1+a} {a(a-1)} = -\frac {1} {a(a-1)}  $
# ```
# ````

# ````{admonition} Esim. Yhdistä yhdeksi murtolausekkeeksi $ 1 - \frac {1} {x+2} $
# :class: dropdown
# Vastaus: $\frac {x+1} {x+2}  $
# ```{admonition} Ratkaisu:
# :class: dropdown
# Lavennetaan luvut siten, että uudeksi nimittäjäksi tulee pyj(1,x+2) eli x+2   
# 
# $ \frac {x+2} {x+2} - \frac {1} {x+2} = \frac {x+2-1} {x+2} = \frac {x+1} {x+2}  $
# ```
# ````

# ### Sekamurtoluvut

# ```{admonition} Sekamurtoluvut
# :class: tip
# Sekamurtoluvut ovat lukuja, joissa on kokonaisosa ja murto-osa.
# esim. $2\frac {1}{2}$ ja $4 \frac {2}{3}$ ovat sekamurtolukuja.
# 
# Ennen yhteen-, vähennys- , kerto- ja jakolaskua sekamurtoluku on muunnettava 
# perusmuotoiseksi murtoluvuksi muotoon $\frac {p}{q}$
# ```

# ```{admonition} Sekamurtoluvun muuntaminen perusmuotoiseksi murtoluvuksi.
# :class: tip
# Lavennetaan kokonaisosa niin, että se saa saman nimittäjän kuin murto-osa
# 
# esim. $2\frac {1}{2} = \frac {4}{2} + \frac {1}{2} = \frac {4+1}{2} = \frac {5}{2}$ 
# ```

# ````{admonition} Esim. Laske $2\frac {1}{2} + 4 \frac {2}{3}$
# :class: dropdown
# Vastaus: $\frac {43}{6}$
# ```{admonition} Ratkaisu:
# :class: dropdown
# Muunnetaan sekamurtoluvut perusmuotoisiksi murtoluvuiksi:
# $2\frac {1}{2}=\frac {5}{2}$   ja $4\frac {2}{3}=\frac {12}{3}+\frac {2}{3}= \frac {14}{3}$
# Lavennetaan yhteiseksi nimittäjäksi pyj(2,3) eli luku 6  =>   
# 
# $ \frac {5}{2} + \frac {14}{3} = \frac {15}{6} + \frac {28}{6} = \frac {43}{6}$ 
# ```
# ````
