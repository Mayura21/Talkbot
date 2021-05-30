"""
It is a simple talkbot which will give you the response to the questions that have been asked.
I have installed chatterbot of version 0.8.6, speech_recognition, pyttsx3.
I have created this in python version 3.6
The commands for windows to install these are
pip install chatterbot==0.8.6
pip install speech_recognition
pip install pyttsx3
pip install PyAudio

If you get any error regarding spacy, then
pip install spacy
If get error regarding pypiwin 32, then
pip istall pypiwin32

To avoid these errors, I recommend you to use python 3.6
If you have upgraded version, I recommend you to create python environment of version 3.6 and run all these
If you have conda, then to create a new environment
conda create -n env_name python=3.6
To activate environment
conda activate env_name

If you don't have conda installed, then
pip install virtualenv
virtualenv env_name python=3.6
"""

# Import all the libraries
import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the bot
myBot = ChatBot('MyBot')

# Create object for speech recognition
r1 = sr.Recognizer()
r2 = sr.Recognizer()

# Set the trainer
myBot.set_trainer(ChatterBotCorpusTrainer)

# Train the bot
myBot.train('chatterbot.corpus.english')

# Initialize python text to speech converter
friend = pyttsx3.init()

# An infinite loop to take the voice input from the user
while True:
    with sr.Microphone() as source:
        print('Listening')
        try:
            audio = r1.listen(source)                   # Record the audio data
            # my_input = r2.recognize_sphinx(audio)     # Recognise the audio input
            my_input = r1.recognize_google(audio)       # Recognise the voice
        except:
            my_input = 'hi'
            # print('You: ', my_input)
        print('You: ', my_input)
        if my_input == 'quit':                  # If input is quit, then quit
            break

        reply = myBot.get_response(my_input)    # Response by the model
        print('Bot: ', reply)
        friend.say(reply)                       # Response said by the bot
        friend.runAndWait()
