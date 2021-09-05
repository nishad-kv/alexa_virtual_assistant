import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    new_command = take_command()

    if 'play' in new_command:
        song = new_command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in new_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'tell me about' in new_command:
        person = new_command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in new_command:
        talk('sorry, I have a headache')

    elif 'are you single' in new_command:
        talk('Get lost')

    elif 'joke' in new_command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')


while True:
    run_alexa()
