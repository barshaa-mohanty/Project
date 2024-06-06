import os
import datetime
import random
import wikipedia
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import openai
import webbrowser

# Set your OpenAI API key directly here
OPENAI_API_KEY = 'your_openai_api_key'
openai.api_key = OPENAI_API_KEY

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')
# Function to record audio and transcribe it to text
def takeCommand():
    fs = 34100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file

    # Transcribe audio to text using OpenAI's Whisper model
    try:
        with open("output.wav", "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            query = transcript['text']
            return query
    except Exception as e:
        speak("I'm sorry, I couldn't understand the audio. Please try again.")
        return ""

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = 'path_to_your_music_directory'  # Replace with actual path
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, random.choice(songs)))
                else:
                    speak("There are no songs in the music directory.")
            else:
                speak("The music directory does not exist.")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'search on wikipedia' in query:
            query = query.replace("search on wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There were multiple results for {query}. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"No Wikipedia page found for {query}.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")

        else:
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=query,
                    max_tokens=1024,
                    temperature=0.5,
                )
                speak(response.choices[0].text)
            except Exception as e:
                speak("I'm sorry, I couldn't process your request. Please try again.")
