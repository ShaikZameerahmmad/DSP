import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('wave1.wav')
print (fs,len(data),data)
plt.subplot(311)
plt.plot(data)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(312)
plt.plot(t,data)
plt.show()
wav.write('wave1-speed.wav',2*fs,data)
wav.write('wave1-slow.wav',0.5*fs,data)