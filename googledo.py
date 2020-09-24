import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition for speech recognition
import datetime  #to draw real time dimensions
import wikipedia  #for searching section
import webbrowser
import os
#import smtplibv      #for sending email messages

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():                                  #This section I added to flabergast the user by wishing him/her wishes according to real time.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Google do.  I am Mr. URJIT's personal assistant. Please tell me how may I help you")       

def takeCommand():       ## speech as an input will be taken in this function
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1          #I have added this threshhold that is 1 because the machine will wait for 1 sec to get input voice. Or else if we stop takling for a sec then it will consider the collected set of commands as its processing input.
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')    #User Language should be english
       ## text = r.recognize_google(audio, language = 'hi-IN')    ## for hindi
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
'''# the section I have added below is for sending voice command emails.
def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('urjittembhurnikar08@gmail.com', 'Oneplusurjit@123personal')
    server.sendmail('ujwaltembhurnikar@gmail.com', to, content)
    server.close()
'''



if __name__ == "__main__":
    
    while 1:  # this loop is because to stay connected with the googledo even after executing our command. It will stop only after we say bye i.e. to break the loop XD.
        wishMe()
        query = takeCommand().lower()

            #Logic for exicuting task based on queries we asked
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results =  wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")
            speak("opening instagram")
        
        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")
            speak("opening urjit's Gmail account")
        
        elif 'open twitter' in query:
            webbrowser.open("www.twitter.com")
            speak("opening twitter")
        
        elif 'open linkedin' in query:
            webbrowser.open("http://linkedin.com/in/urjit-tembhurnikar-575a04189/a")
            speak("opening linkedin account")
        
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google")

        elif 'open my course' in query:
            webbrowser.open("https://www.udemy.com/course/machinelearning")
            speak("opening your machine learning course on udemy!")

        elif 'play movie' in query:
            moviePath = "C:\\HP laptop\\E drive\\MOVIES"
            os.startfile(moviePath)
            speak(f"Here are some movie options")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print("The time is ->"+ strTime + " now")
        
        elif 'what is your name' in query:
            speak("I sm Google do! I am invented by Urjit. Its my pleasure meeting you!")
            
        elif 'bye' in query:
            speak("Hope you enjoyed having conversation with me! Stay home,stay safe! Take care! bye bye!")
            break
            
           
    '''
        elif 'send an email' in query:
            try:
                speak("What shoul I say? ")
                content = takeCommand()
                to = "ujwaltembhurnikar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send email at the moment. Please try again after some time.")
    '''
