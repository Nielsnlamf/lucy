import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

engine.say("testing")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as data_taker:
            print("Say Something")
            voice = listener.listen(data_taker)
            instruct = listener.recognize_google(voice)
            instruct = instruct.lower()
            return instruct

    except:
        pass

def run_ai():
    instruct = take_command()
    talk("The command I got was" + str(instruct))
    print(instruct)
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in instruct:
        time = datetime.datetime.now().strftime('%I: %M')
        print(time)
        talk('current time is' + time)
    elif 'tell me about' in instruct:
        thing = instruct.replace('tell me about', '')
        info = wikipedia.summary(thing, 2)
        print(info)
        talk(info)
run_ai()
