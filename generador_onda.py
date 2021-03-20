# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:58:59 2021

@author: oscar
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile 
from scipy import signal
from os.path import dirname, join as pjoin
from scipy.io import wavfile
from scipy.io.wavfile import write

#Constant
sampling=44100
time=5
t = np.linspace(0., 5., sampling)
#parameters:
#hacer funcion escalon
#hacer funcion impulso
#hacer funcion ram´pa
"""
can be a sawtooth signal
Triangular wave parameters
    frecuency [Hz]
    amplitude [Vpp]
    samples   arr[float]
    phase    -- optional default == 0
    simetry  -- optional default==0.5
    return[y_values][time]
    type [ndarray]
"""

def triangular_wave( frequency, amplitude ,samples, phase=0 , simetry=0.5 ):
    amplitude = np.iinfo(np.int16).max
    triangular_signal = amplitude * signal.sawtooth((2 * np.pi * frequency * samples) + phase, simetry)
    return triangular_signal

senalT=triangular_wave(50,5,t,phase=-np.pi/2)

print(senalT)    
print(type(senalT))
print(type(t))
plt.figure()
plt.subplot(611)
plt.plot(t,senalT)

"""
square wave parameters
    frecuency [Hz]
    amplitude [Vpp]
    samples   arr[float]
    phase    -- optional default == 0
    simetry  -- optional default==0.5
    return[y_values][time]
    type [ndarray]
"""

def square_wave(frequency, amplitude, samples, phase=0, simetry=0.5):
    amplitude = np.iinfo(np.int16).max
    square_signal = amplitude * signal.square( 2 * np.pi *frequency * samples, simetry )
    
    return square_signal
senalSQ=square_wave(50,5,t)
print(senalSQ)    
print(type(senalSQ))
print(type(t))
plt.figure()
plt.subplot(612)
plt.plot(t,senalSQ)

"""
sine wave parameters
    frecuency [Hz]
    amplitude [Vpp]
    samples   arr[float]
    phase    -- optional default == 0
    simetry  -- optional default==0.5
    return[y_values][time]
    type [ndarray]
"""

def sin_wave(frequency, amplitude,samples,phase=0):
    amplitude = np.iinfo(np.int16).max
    sin_signal=amplitude * np.sin(2*np.pi*frequency*samples)
    return sin_signal

senalSin=sin_wave(293.66,5,t)
print(senalSin)    
print(type(senalSin))
print(type(t))
plt.figure()
plt.subplot(613)
plt.plot(t,senalSin)

"""
here we may put operations between our signals

""" 
add_signals=senalSin+senalSQ

plt.figure()
plt.subplot(614)
plt.plot(t,add_signals)

tS_signals = senalT+senalSin
plt.figure()
plt.subplot(615)
plt.plot(t,tS_signals)


amplitude = np.iinfo(np.int16).max
print("********************************")
print(amplitude)
print("********************************")

final=tS_signals+add_signals
plt.figure()
plt.plot()
#plt.xlim(0.0,0.2)
plt.plot(t,final)
scipy.io.wavfile.write("final_signals.wav",sampling,final.astype(np.int16))






