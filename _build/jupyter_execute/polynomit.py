#!/usr/bin/env python
# coding: utf-8

# # Polynomien peruslaskutoimitukset    

# ```{admonition} **Polynomin määritelmä**
# :class: tip
# Ao. muotoa olevaa lauseketta kutsutaan *polynomiksi*     
# 
# $ a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots +a_{1}x+a_{0}$
# 
# 
# x = *muuttuja*   
# 
# n = polynomin *asteluku* (= muuttujan x korkein potenssi polynomissa)  
# 
# $a_{0}$ on polynomin *vakiotermi*   
# 
# 
# ```

# ## Polynomien laskutoimitukset    
# 
# ### Polynomien yhteenlasku 

# Polynomien yhteenlaskussa sulut voidaan poistaa suoraan, jonka jälkeen yhdistetään samanasteiset termit laskemalla niiden kertoimet yhteen.

# ```{admonition} Esimerkki
# :class: tip
# $(2x^3-5x^2+7x-3)+(4x^3+2x+6)$  
# 
# $=2x^3-5x^2+7x-3+4x^3+2x+6$    
# 
# $=(2+4)x^3-5x^2+(7+2)x-3+6$   
# 
# $= 6x^3 - 5x^2 +9x+3$
# ```

# ````{admonition} Laske polynomien $-2x^2+5x+3$ ja $5x^2-7x-2$ summa.
# :class: dropdown
# Vastaus: $3x^2-2x+1$
# ```{admonition} Ratkaisu
# :class: dropdown
# Yhteenlaskussa sulkumerkkejä ei tarvita.
# $-2x^2+5x+3 +5x^2-7x-2$ = $(-2+5)x^2+(5-7)x+3-2 = 3x^2-2x+1$
# ```
# ````

# ### Polynomien vähennyslasku

# Polynomien vähennyslasku suoritetaan laskemalla yhteen vähennettävä ja vähentäjän vastapolynomi, joka saadaan vaihtamalla vähentäjäpolynomien termien etumerkit.  Ts. P(x) - Q(x) = P(x) + (-Q(x))

# ```{admonition} Esimerkki
# :class: tip
# $(2x^3-5x^2+7x-3)\color{red}{-(4x^3+2x+6)}$    
# 
# $=2x^3-5x^2+7x-3\color{red}{ -4x^3-2x-6}$   
# 
# $=(2-4)x^3-5x^2+(7-2)x-3-6$   
# 
# $= -2x^3 - 5x^2 +5x -9$
# ```

# ````{admonition} Laske polynomien$-2x^2+5x+3$ ja $5x^2-7x-2$ erotus.
# :class: dropdown
# Vastaus: $-7x^2+12x+5$
# ```{admonition} Ratkaisu
# :class: dropdown
# Sulkuja poistettaessa vähentäjän etumerkit käännetään.
# $(-2x^2+5x+3) -(5x^2-7x-2)$ = $-2x^2+5x+3-5x^2+7x+2 = -7x^2+12x+5$
# ```
# ````

# ###  Polynomin kertominen vakiolla

# Polynomi kerrotaan vakiolla siten, että polynomin jokainen termi kerrotaan ko. vakiolla

# ```{admonition} Esimerkki
# :class: tip
# $ \color{red}{3}\color{black}{\cdot(2x+5)} = \color{red}{3}\color{black}{\cdot2x}+\color{red}{3}\color{black}{\cdot5} = 6 x +15$  
# ```

# ````{admonition} Sievennä poistamalla sulut lausekkeesta $ -5\cdot(3x^2-2)$
# :class: dropdown
# Vastaus: $-15x^2+10$
# ```{admonition} Ratkaisu
# :class: dropdown
# $  -5\cdot(3x^2-2) = -5\cdot3x^2-5(-2) = -15x^2+10$
# ```
# ````

# ### Polynomin jakaminen vakiolla

# Polynomi kerrotaan vakiolla siten, että polynomin jokainen termi jaetaan ko. vakiolla

# ```{admonition} Esimerkki
# :class: tip
# $ \frac {5 x-2} {\color{red}3} = \frac {5} {\color{red}3} x -\frac {2} {\color{red}3}$  
# ```

# ### Polynomien kertolasku

# Kertolasku P(x)Q(x) suoritetaan kertomalla jokainen P(x):n termi jokaiselle Q(x):n termillä.("ristiin kertominen")   
# 
# Jos polynomissa P(x) on n termiä ja polynomissa Q(x) m termiä, syntyy kertolaskussa mxn termiä, joista samanasteiset termit voidaan yhdistää.   

# ```{admonition} Esimerkki
# :class: tip
# $ \color{red}{(2x+3)}\color{black}{(3x^2-5x+2)}$     
# 
# = $\color{red}{2x}\color{black}{\cdot3x^2}+\color{red}{2x}\color{black}{\cdot(-5x)}+\color{red}{2x}\color{black}{\cdot2}+\color{red}{3}\color{black}{\cdot3x^2}+\color{red}{3}\color{black}{\cdot(-5x)}+\color{red}{3}\color{black}{\cdot2}$   
# 
# = $6x^3-10x^2+4x+9x^2-15x+6$   
# 
# = $6x^3+(-10+9)x^2+(4-15)x+6$   
# 
# = $6x^3 - x^2 -11x + 6$
# ```

# ````{admonition} Sievennä poistamalla sulut lausekkeesta $ (5x-2)(3-7x^2)$
# :class: dropdown
# Vastaus: $-35x^3+14x^2+15x-6$
# ```{admonition} Ratkaisu
# :class: dropdown
# $ (5x-2)(3-7x^2)=5x\cdot3+5x(-7x^2)-2\cdot3-2(-7x^2)$   
# = $ 15x-35x^3-6+14x^2 = -35x^3+14x^2+15x-6$
# ```
# ````

# ### Polynomien potenssi

# Potenssi $P(x)^n$ voidaan laskea kertolaskuna $\overset{n\hspace{2mm} kpl}{P(x)\cdots P(x)}$. Binomin neliö voidaan laskea myös kaavalla    
# $(a\pm b)^{^2}=a^{2}\pm 2ab+b^{2}$

# ```{admonition} Esimerkki
# :class: tip
# Tapa1: $(2x-3)^{2}=(2x-3) (2x-3)=2x\cdot2x+2x\cdot(-3)-3 \cdot2x-3 (-3)=4x^{2}-12x+9$
# 
# Tapa2: $(2x-3)^{2}=(2x)^2-2\cdot 2x\cdot 3+3^{2}=4x^{2}-12x+9$
# ```

# ````{admonition} Sievennä poistamalla sulut $ (5x-2)^2$
# :class: dropdown
# Vastaus: $25x^2-20x+4$
# ```{admonition} Ratkaisu
# :class: dropdown
# Tapa1: $ (5x-2)^2 = (5x-2)(5x-2) = 5x\cdot5x+5x(-2)-2(5x)-2(-2)=25x^2-20x+4$   
#   
# Tapa2: $ (5x-2)^2 = (5x)^2-2(5x)2+(-2)^2 = 25x^2-20x+4 $    $\hspace{10mm}\color{red}{kaava: (a\pm b)^{^2}=a^{2}\pm 2ab+b^{2}}$
# ```
# ````

# ```{admonition} WolframAlpha:n expand
# :class: tip
# WolframAlpha.com -laskimessa polynomien summa, tulo ja potenssi lasketaan komennolla *expand*   
# esim. expand $x (3x-2)^2$    
# 
# ```

# ### Polynomien jakolasku

# Polynomin jakaminen toisella polynomilla suoritetaan **jakokulmassa**.  
# 
# Alla olevassa kuvassa   on suoritettu jakokulmaa käyttäen jakolasku
# $\frac {x^4 -3x^3-x^2-1}{x^2+1} $     
# 
# Osamääräksi on saatu $x^2 -3x -2$  ja jakojäännökseksi $3x+1$ (katso ao.video)

# <video width="600" height="450" controls="True">
#     <source src="jako.mp4" type="video/mp4">
# </video>

# ## Polynomin jakaminen tekijöihin (faktorointi)

# Polynomin kertolaskulle käänteinen operaatio on **polynomin jakakaminen tekijöihin**.   
# Siinä polynomi pyritään esittämään alempiasteisten polynomien tulona.    
# 
# > Keinoja polynomin tekijöihin jakamiseksi:   
# > 
# > 1. Yhteisen tekijän löytäminen
# > 2. Neliöiden erotuksen kaava $\color{red}{a^2-b^2 = (a-b)(a+b)}$
# > 3. Binomin neliön kaavat $\color{red}{(a\pm b)^2 = a^2\pm 2ab+b^2}$
# > 4. Polynomin jakaminen tekijöihin juurten avulla    
# ```{admonition} Sääntö
# :class: tip
# Jos $x_0$ on polynomin P(x) juuri, niin $x-x_0$ on polynomin tekijä.
# ```

# ````{admonition} Esim1. Esitä tulona $ 6ax^2 - 2x $
# :class: dropdown
# Vastaus: $2x(3ax-1) $
# ```{admonition} Ratkaisu
# :class: dropdown
# Termeillä on yhteisinä tekijöinä 2x, joten lauseke voidaan esittää tulomuodossa  
# 
# $ 6ax^2 - 2x = 2x(3ax-1) $  
# 
# (Toinen tekijä 3ax-1 saadaan jakamalla alkuperäisen polynomin molemmat tekijät 2x:llä) 
# ```
# ````

# ````{admonition} Esim2. Esitä tulona $ 25 - a^2 $
# :class: dropdown
# Vastaus: $(5-a)(5+a)$ 
# ```{admonition} Ratkaisu
# :class: dropdown
# Lauseke on lukujen 5 ja a  neliöiden erotus, joten voidaan kirjoittaa  
# 
# $ 25 - a^2 = (5-a)(5+a)$ 
# 
# ```
# ````

# ````{admonition} Esim3. Esitä tulona $ x^2 + 4 x + 4 $
# :class: dropdown
# Vastaus: $(x+2)^2$
# ```{admonition} Ratkaisu
# :class: dropdown
# Tähän soveltuu binomin neliön kaava, koska termeinä ovat lukujen x ja 2 neliöt, sekä niiden kaksinkertainen tulo 2*x*2.  
# 
# $ x^2 + 4 x + 4 = x^2 + 2\cdot2x + 2^2 = (x+2)^2$
# 
# ```
# ````

# ````{admonition} Esim3. Esitä tulona $ 2x^2 + 3 x - 5$
# :class: dropdown
# Vastaus: $(x-1)(2x+5)$ 
# ```{admonition} Ratkaisu
# :class: dropdown
# Huomataan, että x=1 on polynomin juuri, koska $2\cdot1^2 + 3\cdot1 - 5 = 2+3-5=0$   
# 
# Siten $ 2x^2 + 3 x - 5 = (x-1)(ax+b)$ , missä ax+b on toinen tekijöistä.  
# 
# Suorittamalla oikean puolen kertolasku todetaan, että on oltava a=2 ja -b=-5 => b=5   
# 
# Siten $ 2x^2 + 3 x - 5 = (x-1)(2x+5)$ 
# 
# ```
# ````

# ```{admonition} WolframAlpha:n factor
# :class: tip
# WolframAlpha.com online laskimessa polynomien faktorointikomento on *factor*   
# esim. factor $2x^3+3x^2-5x$ 
# ```
