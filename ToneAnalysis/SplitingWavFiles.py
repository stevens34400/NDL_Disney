# Author: Danny Zhu
# For Audio Analysis
# Purpose: Wav Files over 1 GB are not accepted in analysis. Therefore
# we must split the large wav file into smaller pieces to make the size smaller
# Issues: There may be some accuracy errors as we are splitting the movie into parts and viewing them separately as if
# they were individual movies

from pydub import AudioSegment
import ctypes


# Its Important to check the bits your python is running in.
# If result is 4, you are using 32 bit Python
# If Result is 8, you are using 64 bit Python
# Crucial to use 64 bit if you are splitting large wav file or else
# there is not enough memory to split it successfully.
print(ctypes.sizeof(ctypes.c_voidp))

# Make sure file is located in folder or in PATH
newAudio = AudioSegment.from_wav("MoanaAudio2016.wav")

#Splits movie in half. Modify the 2 value to adjust the number of splits
halfway_point = len(newAudio) // 2


# Creates a wave that is one half of the movie

#For First Half of Movie
#newAudio = newAudio[:halfway_point]

# This is for Second Half of Movie
newAudio = newAudio[halfway_point:]

newAudio.export('newSong.wav', format="wav")