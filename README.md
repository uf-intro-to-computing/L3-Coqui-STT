### EGN4932 Lab 3 Repository

This repository contains python example code and instructions on how to use Coqui AI's Speech to Text conversion software (STT)

### Raspberry Pi 3 instructions

For use on a Raspberry Pi 3, the installation steps are slightly different. Because the RPi3 doesn't have a built-in microphone, you must use either a USB mic or an appropriate HAT. Whatever your input device is, make sure it is setup properly and recognized by ALSA.
* According to the PyPi page for [coqui-stt-model-manager](https://pypi.org/project/coqui-stt-model-manager/), you must use Python version 3.7.x to run Coqui STT on a Raspberry Pi. Use `pyenv` or a similar tool to manager multiple python installations on unix-like operating systems. On Windows install multiple versions of python using the Windows installer from the official Python website.
* Create and activate a Python 3.7.x virtual environment.
* Install the speech-to-text engine with `pip install -r rpi-requirements.txt`. This installs a version of `stt` specially compiled for the ARM architecture, along with the `coqui-stt-model-manager`.
* Run the model manager by typing `stt-model-manager` at the shell prompt. This will open a web browser and allow you to download the model files for your language.
* The `mic_vad_streaming.py` example uses the `pyaudio` library to access the microphone. This library depends on `portaudio`, so you must make sure your system has those shared libraries installed. On Raspberry Pi OS, this is achieved with `sudo apt-get install libportaudio2`.
* Navigate into the `mic_vad_streaming` directory. Run `pip install -r requirements.txt` to install the dependencies for the example.
* The example uses the system default audio device if the `-d` flag is not specified. Because we are using a USB mic or an audio HAT, the default device is probably not the correct one. Use the helper script `audio_device.py` to list the audio devices by their `pyaudio` index. After finding the index of your microphone, pass it to the example script with the `-d` flag.
* Now you should be able to run the example using `python mic_vad_streaming.py -d <mic_index> -m <path/to/model> -s <path/to/scorer>`. The model and scorer paths can be found from the stt-model-manager after installing your chosen model.
