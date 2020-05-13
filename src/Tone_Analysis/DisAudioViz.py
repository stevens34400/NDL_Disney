from __future__ import print_function
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt
import librosa
import librosa.display
from librosa.feature import chroma_stft
import librosa
import soundfile as sf
import librosa.display
import IPython.display
import matplotlib.style as ms
import librosa.display
import IPython.display
import matplotlib.style as ms

#y, sr = librosa.load('MoanaAudio2016.wav')
y, sr = librosa.load('SecondHalfOfMoana.wav', offset=30.0, duration=5.0)
from librosa.feature import chroma_stft
block_gen = sf.blocks('SecondHalfOfMoana.wav', blocksize=1024)
print(block_gen)

samplerate = sf.info('SecondHalfOfMoana.wav').samplerate
chromas = []
for bl in block_gen:
    # downmix frame to mono (averaging out the channel dimension)
    y=np.mean(bl, axis=1)
    # compute chroma feature
    chromas.append(chroma_stft(y, sr=sr))
print("This is Y:%d \n", y)


ms.use('seaborn-muted')
#%matplotlib inline
#Load the example track
y, sr = librosa.load(librosa.util.example_audio_file())
# How about something more advanced?  Let's decompose a spectrogram with NMF, and then resynthesize an individual component
D = librosa.stft(y)

# Separate the magnitude and phase
S, phase = librosa.magphase(D)

# Decompose by nmf
components, activations = librosa.decompose.decompose(S, n_components=8, sort=True)
plt.figure(figsize=(12,4))
print("Before SubPlot-1\n")
plt.subplot(1,2,1)
print("After SubPlot-1\n")
librosa.display.specshow(librosa.amplitude_to_db(np.abs(components), ref=np.max), y_axis='log')
plt.xlabel('Component')
plt.ylabel('Frequency')
ms.use('seaborn-muted')
#%matplotlib inline
# Load the example track
y, sr = librosa.load('SecondHalfOfMoana.wav')

D = librosa.stft(y)

# Separate the magnitude and phase
S, phase = librosa.magphase(D)

# Decompose by nmf
components, activations = librosa.decompose.decompose(S, n_components=8, sort=True)
plt.figure(figsize=(12,4))

print("Before SubPlot0\n")
plt.subplot(1, 2, 1)
print("After SubPlot0\n")
#Below gives the source of eror
librosa.display.specshow(librosa.amplitude_to_db(np.abs(components), ref=np.max), y_axis='log')
plt.xlabel('Component')
plt.ylabel('Frequency')
plt.title('Components')
print("Before SubPlot1\n")
plt.subplot(1,2,2)
print("After SubPlot1\n")
librosa.display.specshow(activations, x_axis='time')
plt.xlabel('Time')
plt.ylabel('Component')
plt.title('Activations')
print("Before SubPlot2\n")
plt.tight_layout()
plt.title('Components')
print("After SubPlot2\n")
plt.subplot(1, 2, 2)
librosa.display.specshow(activations, x_axis='time')
plt.xlabel('Time')
plt.ylabel('Component')
plt.title('Activations')

plt.tight_layout()
plt.show()