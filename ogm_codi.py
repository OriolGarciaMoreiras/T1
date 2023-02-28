## Nom i cognoms: Oriol Garcia Moreiras

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=3500                              # Freqüència de la sinusoide
fx1=4000
fx2=6500
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

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



# Exercici 1
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

# Gràfica1 periodes sinusoide
plt.figure(2)                            
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('fx= 4000 Hz, 5 periodes de la sinusoide')   
plt.show()                                
sd.play(x, fm)    


# Gràfica1 Transformada de fourier del senyal de Ls mostres amb DFT de N'
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


# Agafem la freqüència fx = 700 Hz
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

# Gràfica2 periodes sinusoide
plt.figure(4)                             
plt.plot(t[0:Ls], y[0:Ls])                
plt.xlabel('t en segons')                
plt.title('fy= 700 Hz,5 periodes de la sinusoide')   
plt.show()
sd.play(y, fm)    


# Gràfica2 Transformada de fourier del senyal de Ls mostres amb DFT de N'
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



# Exercici 2
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

# Gràfica3 Transformada de fourier del senyal de Ls mostres amb DFT de N'
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


# Exercici 3
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



# Exercici 4
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
