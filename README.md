Primera tasca APA 2023: Anàlisi fitxer de so
============================================

## Nom i cognoms: Oriol Garcia Moreiras



## Representació temporal i freqüencial de senyals d'àudio.

### Domini temporal

Per llegir, escriure i representar un fitxer en format `*.wav` en python podem fem servir els següents mòduls:

- Numpy:
```python
import numpy as np
```
- Matplotlib: 
```python
import matplotlib.pyplot as plt
```
- Soundfile:
```python
import soundfile as sf
```

Per **crear** i **guardar** a un fitxer un senyal sinusoidal de freqüència `fx Hz`, digitalitzat a `fm Hz`, de durada `T` segons i amplitud 
`A` fem:

```python
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
```

El resultat és un fitxer guardat al directori de treball i que es pot reproduir amb qualsevol reproductor d'àudio

Per **representar** gràficament 5 períodes de senyal fem:

```python
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
```

El resultat del gràfic és:

<img src="img/sinusoide.png" width="480" align="center">

> Nota: Si es treballa amb ipython, es pot escriure %matplotlib i no cal posar el plt.show() per veure gràfics

El senyal es pot **escoltar (reproduir)** directament des de python important un entorn de treball amb els dispositius de so, com per 
exemple `sounddevice`:

```python
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio
```

### Domini transformat

Domini transformat. Els senyals es poden analitzar en freqüència fent servir la Transformada Discreta de Fourier. 

La funció que incorpora el paquet `numpy` al submòdul `fft` és `fft`:

```python
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
```

I podem representar el mòdul i la fase, en funció de la posició de cada valor amb:

```python
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics
```
<br>
<img src="img/TF.png" width="480" align="center">
<br> <br>

Proves i exercicis a fer i entregar
-----------------------------------

1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera $f_x = 4$ kHz, a banda d'una
    freqüència pròpia en el marge audible. Comenta els resultats.

```python
# Agafem la freqüència fx = 4000 Hz
T = 2.5                               
fm = 8000                              
fx = 4000                              
A = 4                                  
pi = np.pi                            
L = int(fm * T)                      
Tm = 1/fm                              
t = Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)      
sf.write('so_1.wav', x, fm)   
Tx = 1/fx                                   
Ls = int(fm*5*Tx)

# Periodes sinusoide
plt.figure(2)                            
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('fx= 4000 Hz, 5 periodes de la sinusoide')   
plt.show()                                
sd.play(x, fm)
``` 
<br>
<img src="img/figure2(ex1).PNG" width="500" align="center">
<br> <br>

```python
# Transformada de fourier del senyal de Ls mostres amb DFT de N'
N = 5000                       
X = fft(x[0 : Ls], N)           
k = np.arange(N)                       
plt.figure(3)                         
plt.subplot(211)                      
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show()
```
<br>
<img src="img/figure3(ex1).PNG" width="500" align="center">
<br> <br>

```python
# Agafem la freqüència fy = 700 Hz
T = 2.5                              
fm = 8000                            
fy = 700                              
A = 4                               
pi = np.pi                            
L = int(fm * T)                      
Tm = 1/fm                              
t=Tm*np.arange(L)                    
y = A * np.cos(2 * pi * fy * t)     
sf.write('so_2.wav', y, fm)   
Ty = 1/fy                                  
Ls = int(fm*5*Ty)                          

# Periodes sinusoide
plt.figure(4)                             
plt.plot(t[0:Ls], y[0:Ls])                
plt.xlabel('t en segons')                
plt.title('fy= 700 Hz,5 periodes de la sinusoide')   
plt.show()
sd.play(y, fm)
``` 
<br>
<img src="img/figure4(ex1).PNG" width="500" align="center">
<br> <br>

```python
# Transformada de fourier del senyal de Ls mostres amb DFT de N'
N=5000                        
Y=fft(y[0 : Ls], N)           
k=np.arange(N)                      
plt.figure(5)                        
plt.subplot(211)                      
plt.plot(k,abs(Y))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|Y[k]|')               
plt.subplot(212)                     
plt.plot(k,np.unwrap(np.angle(Y)))  
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show()
```
<br>
<img src="img/figure5(ex1).PNG" width="500" align="center">
<br> <br>

### COMENTA ELS RESULTATS: <br>
Com podem veure en la primera gràfica (figure2) hi ha 5 períodes, on cada període té una durada aproximada de 0.0002 segons (0.2 ms) i una amplitud de valor 4, per tant, els 5 períodes junts tenen una durada d'aproximadament 0.001 segons (1 ms) i una amplitud de valor 4.
En la gràfica de la transformada (figure3) podem apreciar 10 mostres amb una dimensió de la transformada discreta igual a 5000, on tenim dues mostres per cada període, i cal ressaltar el pols que veiem en 2000-3000.

En canvi, en la tercera gràfica (figure4) continuem tenint 5 períodes d'amplitud 4, però cada període té una durada aproximada de 0.00015 segons (0.15 ms), per tant, els 5 períodes junts tenen una durada d'aproximadament 0.00075 segons (0.75 ms).
En la gràfica de la transformada (figure5) veiem dos polsos. El primer el veiem en 425-575 aproximadament, i el segon en 4425-4575. Per una altra part, ens trobem que la gràfica té 57 mostres en els 5 períodes.

<br> <br>

2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat 
    (`x_r, fm = sf.read('nom_fitxer.wav')`).

    - Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

    - Explica el resultat del apartat anterior.

```python
x_r, fm = sf.read('so_1.wav')     #read del primer fitxer
Tm = 1/fm
T = np.arange(len(x_r))                              
t = Tm*T              
sf.write('ex2_so.wav', x_r, fm) 

f = fm/2
T = 1/f                                   # Període del senyal
Ls = int(fm*5*T)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(6)                             
plt.plot(t[0:Ls], x_r[0:Ls])                
plt.xlabel('t en segons')              
plt.title('Exercici 2, 5 periodes de la sinusoide')   
plt.show() 
sd.play(x_r, fm)    
``` 
<br>
<img src="img/figure6(ex2).PNG" width="500" align="center">
<br> <br>

```python
# Transformada de fourier del senyal de Ls mostres amb DFT de N'
N = 5000                       
X = fft(x_r[0 : Ls], N)         
k = np.arange(N)                        
plt.figure(7)                        
plt.subplot(211)                     
plt.plot(k,abs(X))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                 
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))   
plt.xlabel('Index k')               
plt.ylabel('$\phi_x[k]$')             
plt.show()
``` 
<br>
<img src="img/figure7(ex2).PNG" width="500" align="center">
<br> <br>

### Explica el resultat del apartat anterior: <br>
Com indicava en l'enunciat el fitxer wav l'hem creat a partir de f , la qual és fm/2, per tant, es 4000 Hz. Observant la gràfica comprovem que hi ha 5 períodes d'amplitud 1, on cada període té una durada de 0.0002 segons (0.2 ms) aproximadament. Per una altra part, podem observar el mateix gràfic de la transformada que hem comentat en el primer exercici.

<br> <br>


3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de
    $0$ a $f_m/2$ en Hz.

    - Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.

    - Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada?
      Comprova-ho amb el senyal generat.

> NOTES:
>
> - Per representar en dB has de fer servir la fórmula següent:
>
> $X_{dB}(f) = 20\log_{10}\left(\frac{\left|X(f)\right|}{\max(\left|X(f)\right|}\right)$
>
> - La relació entre els valors de l'índex k i la freqüència en Hz és:
>
> $f_k = \frac{k}{N} f_m$

Com l'operació de dividir X(f) entre el màxim de X(f) equival a 1 no podem fer el que demana l'enunciat.

```python
# Creem i guardem un fitxer un senyal sinusoidal de freqüència fx, digitalitzat a fm, de durada T segons i amplitud A:
T= 2.5                               
fm=8000                             
fx=440                               
A=4                                  
pi=np.pi                           
L = int(fm * T)                     
Tm=1/fm                              
t=Tm*np.arange(L)                   
x = A * np.cos(2 * pi * fx * t)     
sf.write('nom_fitxerej3.wav', x, fm)  
Tx=1/fx                                   
Ls=int(fm*Tx*5)                           

# Gràfica Exercici 3
plt.figure(8)                             
plt.plot(t[0:Ls], x[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('Exercici 3 (5 períodes)')  
plt.show()
sd.play(x, fm)
```    
<br>
<img src="img/figure8(ex3).PNG" width="500" align="center">
<br> <br>

```python
# Modul & Fase FFT a partir de 
N=5000                        
X=fft(x[0 : Ls], N)        
k=np.arange(N)                                            
plt.figure(9)                         
XdB = 20*np.log10(np.abs(X)/max(np.abs(X))) # Representar en dB
fk = k[0:N//2+1]*fm/N         # Relació entre els valors de l'índex k i la freqüència en Hz
plt.subplot(211)   
plt.plot(fk,XdB[0:N//2+1]) 
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')              
plt.show()    
``` 
<br>
<img src="img/figure9(ex3).PNG" width="500" align="center">
<br> <br>

4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). 
    Llegeix el fitxer d'àudio i comprova:

    - Freqüència de mostratge.
    - Nombre de mostres de senyal.
    - Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
    - Representa la seva transformada en dB en funció de la freqüència, en el marge $f_m\le f\le f_m/2$.
    - Quines son les freqüències més importants del segment triat?


```python
import wave as readwave
obj = readwave.open('so_exercici4.wav','r')                   # Obrim el fitxer
print( "Nombre de canals:",obj.getnchannels())            # Nombre de canals
if(obj.getnchannels()==1): {print("Mono")}
else: {print("Stereo")}
print ( "Freqüència de mostratge:",obj.getframerate())    # Freqüència de mostratge.
print ("Nombre de mostres de senyal: ",obj.getnframes())  # Nombre de mostres de senyal.
obj.close()                                               # Sortim del fitxer
```
```python
T= 0.025                               
data, fm =sf.read('so_exercici4.wav')       
L = int(fm * T)                     
Tm=1/fm                            
t=Tm*np.arange(L)                  
sf.write('fitxer_exercici4.wav', data, fm)  

plt.figure(10)                          
plt.plot(t[0:L],data[0:L])              
plt.xlabel('t en segons')               
plt.title('Exercici 4 (5 períodes)')  
plt.show()                             
```
<br>
<img src="img/figure10(ex4).PNG" width="500" align="center">
<br> <br>

```python
N=5000                        
X=fft(data[0 : L], N)    
k=np.arange(N)                                         
plt.figure(11)                         
XdB = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N
plt.subplot(211)   
plt.plot(fk,XdB[0:N//2+1]) 
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')          
plt.show()   
``` 
<br>
<img src="img/figure11(ex4).PNG" width="500" align="center">
<br> <br>

Nombre de canals: 1 <br>
Mono <br>
Freqüència de mostratge: 48000 <br>
Nombre de mostres de senyal:  307618 <br>

### Quines son les freqüències més importants del segment triat? <br>
Totes les freqüències són igual d'importants, ja que en la gràfica s'observa una línia gairebé recta on podem apreciar que a mesura que augmenta la freqüència disminueix el '$\phi_x[k]$'.


Entrega
-------

- L'alumne ha de respondre a totes les qüestions formulades en aquest mateix fitxer, README.md.
    - El format del fitxer es l'anomenat *Markdown* que permet generar textos amb capacitats gràfiques (com ara *cursiva*, **negreta**,
      fòrmules matemàtiques, taules, etc.), sense perdre la llegibilitat en mode text.
    - Disposa d'una petita introducció a llenguatge de Markdown al fitxer `MARKDOWN.md`.
- El repositori GitHub ha d'incloure un fitxer amb tot el codi necesari per respondre les qüestions i dibuixar les gràfiques.
- El nom del fitxer o fitxers amb el codi ha de començar amb les inicials de l'alumne (per exemple, `fvp_codi.py`).
- Recordéu ficar el el vostre nom complet a l'inici del fitxer o fitxers amb el codi i d'emplar el camp `Nom i cognoms` a dalt de tot
  d'aquest fitxer, README.md.
