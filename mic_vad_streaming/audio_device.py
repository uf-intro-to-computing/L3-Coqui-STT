# A helper script to list the pyaudio devices by index

import pyaudio

audio = pyaudio.PyAudio()

for d in range(0, audio.get_device_count()):
    print("Audio device {0}: {1}".format(d, audio.get_device_info_by_index(d)))
