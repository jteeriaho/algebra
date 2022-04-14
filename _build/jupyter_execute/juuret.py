#!/usr/bin/env python
# coding: utf-8

# # Juurilausekkeet 

# ```{admonition} Neliöjuuri $\sqrt{a}$
# :class: tip
# $\sqrt{a}$  tarkoittaa sitä positiivista lukua, jonka neliö on a 
#     
# ts. ${\sqrt{a}}^2 = a$
# 
# ```

# Esim. $\sqrt{4}=2$, koska $2^2=4$   
#       $\sqrt{49}=7$, koska $7^2=49$    
#       $\sqrt{2}\approx1.414$, koska $1.414^2\approx2$     
#       $\sqrt{-4}$ ei ole olemassa (minkään luvun neliö ei ole negatiivinen)

# ```{note}
# Neliöjuuren määritelmä voidaan esittää myös muodossa    
# $\sqrt{a}$ on yhtälön $x^2=a$ positiivinen juuri.
# ```

# ```{admonition} Kuutiojuuri $\sqrt[3]{a}$
# :class: tip
# $\sqrt[3]{a}$ tarkoittaa lukua, jonka 3. potenssi on a 
#     
# ts. ${\sqrt[3]{a}}^3 = a$
# 
# ```

# Kuutiojuuren voi ottaa myös negatiivisesta luvusta. Tällöin juuren arvo on negatiivinen.   
# 
# $\sqrt[3]{8} = 2$  , koska $2^3 = 8$    
# $\sqrt[3]{-125} = -5$  , koska ${(-5)}^3 = -125$    
# $\sqrt[3]{10} \approx 2.154$  , koska $2.154^3 \approx 10$ 

# ```{note} 
# $\sqrt[3]{a}$ on yhtälön $x^3=a$ juuri.
# ```

# ```{admonition} Yleinen juuri $\sqrt[n]{a}$
# :class: tip
# $\sqrt[n]{a}$ tarkoittaa lukua, jonka n. potenssi on a 
#     
# ${\sqrt[n]{a}}^n = a$    
# 
# 
# > Kun n on parillinen, $\sqrt[n]{a}$ on määritelty vain kun $a\gt0$    
# > Kun n on parillinen, $\sqrt[n]{a}$ on määritelty myös kun a < 0
# 
# ```

# ```{admonition} Juurten esitys murtopotensseina
# :class: tip
# $\sqrt{a}$ voidaan esittää potenssimuodossa $a^{\frac{1}{2}}$    
# 
# $\sqrt[3]{a}$ voidaan esittää potenssimuodossa $a^{\frac{1}{3}}$ 
#     
# $\sqrt[n]{a}$ voidaan esittää potenssimuodossa $a^{\frac{1}{n}}$ 
# 
# Perustelu:  ${(a^{\frac{1}{2}})}^2 = {a^{\frac{1}{2}\cdot 2}} = a$ (vrt. neliöjuuren määritelmä)    
# 
# Murtopotensseja voi käyttää vain positiivisille kantaluvuille a
# 
# ```

# Esimerkkejä eräiden lausekkeiden juuri- ja potenssiesityksistä 
# 
# | Juuriesitys                   | Potenssiesitys       |
# |-------------------------------|----------------------|
# | $\sqrt{x}$                    | $x^{\frac{1}{2}}$    |
# | $\frac{1}{\sqrt{x}}$          | $x^{-\frac{1}{2}}$   |
# | $\sqrt[3]{x^2}$               | $x^{\frac{2}{3}}$    |

# ## Juurilausekkeiden sievennyssääntöjä

# Useimmat laskimet sieventävät automaattisesti neliöjuurilausekkeet muotoon, jossa 1) nimittäjässä ei esiinny neliöjuuria 2) juurten sisällä ei ole kokonaisluvun tai parametrien neliöitä tai parillisia potensseja. Sievennys perustuu seuraaviin sääntöihin.

# ```{admonition} Neliöjuurilausekkeiden sievennys
# :class: tip
# 
# 1. $\frac{1}{\sqrt{a}}= \frac{\sqrt{a}}{a}$ 
# 
# 
# 2. $\sqrt{a\cdot b} = \sqrt{a}\sqrt{b}$   
# 
#     
# 3. $\sqrt{\frac{a}{b}}=\frac{\sqrt{a}}{\sqrt{b}}$
# 
# ```

# Laskimissa $\frac{1}{\sqrt{3}}$ usein lavennetaan muotoon $\frac{\sqrt{3}}{3}$. Samoin useat laskimet sieventävät juurilausekkeita seuraavasti:   
# 
# $\sqrt{50}=\sqrt{2\cdot 25}=\sqrt{2}\cdot \sqrt{25}=5\sqrt{2}$    
# 
# $\sqrt{6}\sqrt{2}=\sqrt{3}\sqrt{2}\sqrt{2}=2\sqrt{3}$    
# 
# $\frac{\sqrt{3}}{\sqrt{6}}= \sqrt{\frac{3}{6}}=\sqrt{\frac{1}{2}}=\frac{1}{\sqrt{2}}=\frac{\sqrt{2}}{2}$

# ```{admonition} Sievennä a) $\sqrt{12}$ ja $\frac{\sqrt{10}}{\sqrt{2}}$
# :class: dropdown
# $\sqrt{12}=\sqrt{4}\sqrt{3}=2\sqrt{3}$
# 
# $\frac{\sqrt{10}}{\sqrt{2}}=\sqrt{\frac{10}{2}}=\sqrt{5}$
# ```
