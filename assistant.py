import Speech_recognition as src
import os
import wikipedia #To do Wikipedia searches,
import datetime #for date and time'''
import pyttsx3#A python library which will help us to convert text to speech. In short, it is a text-to-speech library'''
import webbrowser
#import googlemaps for google maps
#import smtplib for sending a mail'''


engine = pyttsx3.init('sapi5') #Speech API developed by Microsoft helps in synthesis and recognition of voice'''
voices = engine.getProperty('voices')
# (voices[1].id) for female voice
#(voices[0].id) for male voice or you can add your own'''
engine.setProperty('voice', voices[0].id)


def speak(audio): #speak() function for convert our text to speech.'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():

#wishMe fuction check the hour of machine and wise according to the hour'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning brother!!....")

    elif hour>=12 and hour<18:
        speak("Good Afternoon brother!!....")

    else:
        speak("Good Evening brother!!...")

    speak("I am your assistant . Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output'''

    reco = src.Recognizer()
    with src.Microphone() as source:
        print("Listening...")
        reco.pause_threshold = 1
        reco.energy_threshold =1000
        reco.dynamic_energy_threshold=True
        audio = reco.listen(source)

    try:
        print("Recognizing...")
        query = reco.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        
        print("Say that again please...")
        return "None"
    return query

""" def sendEmail(to, content):
           server = smtplib.SMTP('smtp.gmail.com')
           server.ehlo()
           server.starttls()
           server.login('youremail@gmail.com', 'your-password')
           server.sendmail('youremail@gmail.com', to, content)
           server.close()
"""

if __name__ == "__main__":
    '''main function code execting start from here'''
    wishMe()
    while True:

        query = takeCommand().lower()#help to change all command into lower case'''


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'thank you' in query:
            speak("thankyou archit!!..")


        elif 'play music' in query:
            music_dir = 'F:\\pythonProject\\assistantSong'
            songs = os.listdir(music_dir)
            print("music")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video song' in query:
            video_dir='F:\\pythonProject\\assistantVideo'
            video=os.listdir(video_dir)
            print("videosong")
            os.startfile(os.path.join(video_dir,video[0]))

        elif 'how are you' in query:
            speak("i am good")

        elif 'who are you' in query:
            speak("i am vinay your brother.")

        elif 'who i am' in query:
            speak("you are my big brother")

        elif ' whats the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Brother, the time is {strTime}")

        elif 'open visual code' in query:
            codePath = 'C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(f"visual code{codePath}")
                        
        elif 'open facebook' in query:
            print("facebook")
            webbrowser.open_new_tab("www.facebook.com")

        elif 'open instagram'in query:
            print("instagram")
            webbrowser.open_new_tab("www.instagram.com")

        elif 'open flipkart' in query:
            print("flipkart")
            webbrowser.open_new_tab("www.flipkart.com")

        elif 'open amazone' in query:
            print("amazone")
            webbrowser.open_new_tab("www.amazone.com")

        elif 'open w3school ' in query:
            print("w3school.com")
            webbrowser.open_new_tab("www.w3school.com")

        elif 'exit' in query:
            print("exit")
            exit()

        
             



 
      #  elif ' my loction' in query:
       #     speak("searching location")
        #    gmaps = googlemaps.Client(key='Add Your Key here')
         #   geocoding an address
          #  geocode_result = gmaps.geocode('')
           # Look up an address with reverse geocoding
            #reverse_geocode_result = gmaps.reverse_geocode((,))
             #Request directions via public transit
      #      now = datetime.now()
       #    speak("according to your current location")
        #    print(directions_result)
         #   speak(directions_result)
          
       # elif 'email to archit' in query:
        #    try:
         #       speak("What i say?")
          #      content = takeCommand()
           #     to = "archit15@gmail.com"    
            #    sendEmail(to, content)
             #   speak("Email has been sent!")
            #except Exception as e:
            

