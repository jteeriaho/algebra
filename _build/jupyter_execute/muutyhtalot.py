#!/usr/bin/env python
# coding: utf-8

# # Muita yhtälötyyppejä

# ## Murtoyhtälöt ja epäyhtälöt

# ```{admonition} **Murtoyhtälön perusmuoto**
# :class: tip
# $\frac{p(x)}{q(x)}=0$ , missä p(x) ja q(x) ovat x:n polynomeja    
# 
# Murtoyhtälön ratkaisumenetelmä:
# 
# 1. Todetaan yhtälön määritysjoukko, joka on kaikki reaaliluvut lukuunottamatta nimittäjän q(x) nollakohtia.     
# 2. Murtoyhtälön ratkaisujoukkona ovat ne yhtälön p(x) = 0 nollakohdat, jotka kuuluvat määritysjoukkoon  
# 
# Käytännössä murtoyhtälöä ei tarvitse viedä perusmuotoon, vaan se voidaan ratkaista toteamalla yhtälön määritysjoukko, jonka jälkeen yhtälö voidaan kertoa siinä esiintyvien nimittäjien pienimmällä yhteisellä jaettavalla siten, että nimittäjät poistuvat. Ratkaistaan tuloksena saatu polynomiyhtälö.  Murtoyhtälön ratkaisut ovat ne polynomiyhtälön ratkaisut, jotka ovat määritysjoukossa. 
# ```

# ````{admonition} Esim1. Ratkaise yhtälö $\frac{x^2-x}{x+1}=0$
# :class: dropdown
# Vastaus; x = 0  tai  x = 1
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown  
# Määritysjoukkona on kaikki reaaliluvut poislukien nimittäjän nollakohta.  Mj: $x\neq -1$    
# Kerrotaan yhtälö (x+1):llä, jolloin saadaan yhtälö $x^2 - x$ = 0.  Tämä ratkaistaan seuraavasti:      
# 
# $ x (x-1) = 0$       
# $ x = 0$ tai $x = 1$   
# Kumpikin osoittajan juurista kuuluu määritysjoukkoon, joten ne muodostavat yhtälön ratkaisut.
# ```
# ````

# ````{admonition} Esim2. Ratkaise yhtälö $\frac{2}{x}+1=\frac{6}{x+1}$
# :class: dropdown
# Vastaus; x = 1 tai x = 2
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown  
# Määritysjoukkona on kaikki reaaliluvut poislukien nimittäjien nollakohdat.  Mj: $x\neq 0, -1$     
# Kerrotaan yhtälö yhtälön nimittäjien pyj:llä eli x(x+1):llä, jolloin saadaan     
# $\frac{2x(x+1)}{x}+x(x+1)=\frac{6x(x+1)}{x+1}$, josta supistamalla saadaan    
# 
# $ 2(x+1)+x(x+1)=6x$     
# $ 2x+2+x^2+x=6x$     
# $ x^2-3x+2=0$    
# $ x=1$ tai $x = 2$    
# Kumpikin juurista kuuluu määritysjoukkoon, joten ne muodostavat yhtälön ratkaisut.
# ```
# ````

# ## Potenssiyhtälöt

# ```{admonition} **Potenssiyhtälön perusmuoto**
# :class: tip
# $x^n = a$ , missä n on positiivinen kokonaisluku ja a on vakio    
# 
# Potenssiyhtälön ratkaisu:
# 
# Jos n on parillinen ja a > 0, ratkaisuja on kaksi:  $x=\pm \sqrt[n]{a}$    
# Jos n on parillinen ja a < 0, yhtälöllä ei ole ratkaisuja       
# Jos n on pariton, ratkaisuja on yksi: $x=\sqrt[n]{a}$ riippumatta a:n etumerkistä
# 
# ```

# ````{admonition} Esim1. Ratkaise yhtälö $2x^4=7$
# :class: dropdown
# Vastaus; $x=\pm \sqrt[4]{\frac{7}{2}}$
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown  
# Jaetaan yhtälö 2:lla, jolloin saadaan perusmuotoinen potenssiyhtälö     
# $x^4=\frac {7}{2}$          Ratkaisuja on kaksi:      
# $x=\pm \sqrt[4]{\frac{7}{2}}$
# ```
# ````

# ````{admonition} Esim1. Ratkaise yhtälö $ 4x^6+1 = 0$
# :class: dropdown
# Vastaus; ei reaalisia ratkaisuja
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown  
# Viedään yhtälö perusmuotoon    
# 
# $x^4=-\frac {1}{4}$          
# Parillinen potenssi ei voi olla negatiivinen, joten yhtälöllä ei ole ratkaisuja. 
# ```
# ````

# ````{admonition} Esim1. Ratkaise yhtälö $ x^3+5 = 0$
# :class: dropdown
# Vastaus; $x=-\sqrt[3]{5}$
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown  
# Viedään yhtälö perusmuotoon       
# $ x^3 = -5$                 
# Otetaan kuutiojuuri molemmista puolista    
# 
# $x=\sqrt[3]{-5} = -\sqrt[3]{5}$     
# (huom! miinusmerkin voi siirtää juuren alta etumerkiksi:  $\sqrt[3]{-a} = -\sqrt[3]{a}$ )        
#  
# ```
# ````

# ## Korkeamman asteen polynomiyhtälöt

# ```{admonition} Korkeamman asteen polynomiyhtälöt
# :class: tip
# $ a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots +a_{1}x+a_{0} = 0$, missä polynomin asteluku n > 2
# ```

# Tarkastellaan erikoistapausta, jota sanotaan **bikvadraattiseksi yhtälöksi**.

# ```{admonition} **Bikvadraattinen yhtälö**
# :class: tip
# Korkeamman asteen polynomiyhtälöiden eräs erikoistapaus on bikvadraattinen yhtälö, jonka vasen puoli on neljännen asteen polynomi, jossa esiintyy vain x:n parillisia potensseja    
# 
# $ a_{4}x^{4}+a_{2}x^{2}+a_{0} = 0$   
# 
# Ratkaisu:  Tehdään sijoitus $t = x^2$, ja ratkaistaan t toisen asteen yhtälöstä $ a_{4}t^{2}+a_{2} t+a_{0} = 0$.    
# Ratkaistaan x:n mahdolliset arvot yhtälöistä $x^2 = t_1$  ja  $x^2 = t_2$ , missä $t_1$ ja $t_2$ ovat em. toisen asteen yhtälön juuret.   
# 
# ```

# ````{admonition} Esim1. Ratkaise yhtälö $ x^4 - 3x^2 + 2 = 0$
# :class: dropdown
# Ratkaisujoukko: {$-1,1,-\sqrt{2},\sqrt{2}$}
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown  
# Tehdään sijoitus t = $x^2$, ja ratkaistaan t toisen asteen yhtälöstä :   
# $ t^2 - 3 t + 2 = 0$    
# $ t=1$ tai $t = 2$     
# Sijoittamalla t:n tilalle $x^2$ saadaan kaksi yhtälöä:     
# 
# $x^2 = 1$ , jonka ratkaisut ovat x=-1 tai x=1      
# $x^2 = 2$ , jonka ratkaisut ovat x=-$\sqrt{2}$ tai x=$\sqrt{2}$     
# 
# Yhdistämällä molemmat ratkaisut saadaan ratkaisujoukoksi ${-1,1,-\sqrt{2},\sqrt{2}}$
#  
# ```
# ````
