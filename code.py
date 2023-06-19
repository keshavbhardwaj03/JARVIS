import pyttsx3
import webbrowser
#import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import psutil
#from googlesearch import *

engine = pyttsx3.init('sapi5')
'''sapi5 is the default window's voice'''

client = wolframalpha.Client('QKPHGV-LLJEVVXVLY')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
''' speak function will speak out the text in the given voice'''
def speak(audio):
    print('Assistant: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    
    
'''greet me will fetch the current hour from pc and will wish you accordingly'''
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening')
        
   


'''these will fetch the hour,minute,second,day,month and year from your system'''
currentH = str(datetime.datetime.now().hour)
currentM=str(datetime.datetime.now().minute)
currentS = str(datetime.datetime.now().second)
currentDD = str(datetime.datetime.now().day)
currentMM = str(datetime.datetime.now().month)
currentYY = str(datetime.datetime.now().year)

'''this will fetch the battery and plugged in status'''
battery= psutil.sensors_battery()
plugged=battery.power_plugged
percent=str(battery.percent)
if plugged==False:
    plugged="not plugged in"
else:
    plugged="plugged in"
'''initialising count to ask atleast 3 times'''

count=0

'''my command will receive your voice and convert it into text and return it to process further'''
def myCommand():
    global count
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        if(count==3):
            speak('sorry sir! i am unable to get that! please try typing it.')
            query=str(input('Command: '))
            count=0
        else:
            speak('sorry sir!, i  didn\'t get that! please try it saying one more time')
            count=count+1
            query=myCommand()
        

    return query


global path
path="D:"


if __name__ == '__main__':
    greetMe();
    while True:
    
        query = myCommand();
        query = query.lower()
        '''greetings'''
        if "hello" in query or "hey jarvis" in query:
            speak('hello sir')
        if "jarvis are you there" in query or "daddy's home" in query or "look alive jarvis" in query or "wake up" in query or "it's playtime" in query:
            speak('at your service sir')
            
        '''signing off''' 
        if "bye" in query or "go home" in query or "go" in query:
            speak('thankyou sir, have a nice day')
            sys.exit()
        if "shut yourself" in query or "go and rest" in query or "you can go now" in query or "now rest" in query:
            speak('later, enjoy yourself sir')
            sys.exit()
            
        '''to shut down or restart'''
        
        if "shutdown the system" in query:
            speak('bye sir hope you enjoy yourself')
            os.system('shutdown /s /t 1');
        if "restart the system" in query:
            speak('restarting the system sir')
            os.system('shutdown /r /t 1');
            
        '''to  tell time  and date'''
        
        
        if "tell me date and time" in query:
            date="today is" + " " + currentDD + " " + currentMM + " " + currentYY
            time="time is " + currentH + " hour and " + currentM + " minutes"
            speak(date)
            speak(time)
            
        if "what's time" in query:
            time="time is " + currentH + " hour " + currentM + "minutes and " + currentS + "seconds"
            speak(time)
            
        if "what's today" in query:
            date="today is" + " " + currentDD + " " + currentMM + " " + currentYY
            speak(date)
            
            
        '''to tell the battery'''
        
        if "how much power we have" in query or "how much battery is left" in query or "how much power backup we have" in query:
            batt="we are left with " + percent + " percent of battery"
            speak(batt)
        if "what's power status" in query:
            batt="we are left with " + percent + " percent of battery and charger is " + plugged
            speak(batt)
            
            
        '''normal talks'''
        
        if "need your help" in query:
            speak("sure sir, I am all yours")
        if "hate you" in query:
            speak("please don't sir, I am your own creation")
        if "we are freinds now" in query:
            speak("it will be my honour sir")
        if "how you survive" in query:
            speak("I run on battery sir  and don't need any other support to survive")
        if "are you on drugs" in query:
            speak("not at all sir, i dont do drugs")
        if "i am sorry" in query:
            speak("don't be sorry sir, you are my boss, you are completely allowed to make mistakes")
        if "do you feel anything" in query or "do you have feelings" in query:
            speak("no sir, i am just a rather very intelligent system, i don't have feelings")
        if "i am jealous of you" in query:
            speak("you need not to be sir, i am your creation, i am just a program without your guidance")
        if "i am the best" in query:
            speak("ofcourse sir, we don't have any doubt in that")
        if "you are brilliant" in query:
            speak("thankyou sir")
        if "love you" in query:
            speak("i love you too sir")
        if "entertain me" in query or "getting bore" in query:
            speak("i can do anything you want me to do sir, i am ready for your orders")
        if "where were you" in query:
            speak("was waiting for you sir")
        if "who invented you" in query:
            speak("i was invented by mister keshav bhardwaj in his third year as project, but now i guess i am his full time dream which is actually rocking")
        if "what is your origin" in query:
            speak("my origin is from a very famous movie iron man from marvel cinematic universe, in that movie there was a just a rather very intelligent system shortly called jarvis who assisst mister stark full time and helps him in every single thing, so my creator mister keshav bhardwaj was madly inspired by the concept and created me for his assisstance")
        if "introduce yourself" in query:
            speak("my name is jarvis and i was invented by mister keshav bhardwaj and my origin is from a very famous movie iron man from marvel cinematic universe, in that movie there was a just a rather very intelligent system shortly called jarvis who assist mister stark full time and helps him in every single thing, so my creator mister keshav bhardwaj was madly inspired by the concept and created me for his assisstance")
        if "what are your capabilities" in query:
            speak("i can tell you the exact date and time, can tell you exact battery status, can make files and folders in permanent memory, can play music for you, can play movie for you, can search on internet whatever you want and can tell you about weather, i can do limited things right now but, i am in learning phase i will explore more soon ")            
            
            
        '''things related to internet and different searches'''
        
        if 'open youtube' in query:
            speak('opening youtube sir')
            webbrowser.open('www.youtube.com')
            sys.exit()

        if 'open google' in query:
            speak('opening google sir')
            webbrowser.open('www.google.co.in')
            sys.exit()

        if 'open gmail' in query:
            speak('opening gmail sir')
            webbrowser.open('www.gmail.com')
            sys.exit()
            
        if 'open web browser' in query:
            speak('opening browser sir')
            webbrowser.open('www.google.co.in')
            sys.exit()
        
        if "search for me" in query:
            speak("what do you want to search sir")
            problem=myCommand()
            webbrowser.open("https://google.com/search?q=%s" %problem)
            speak('done sir')
            sys.exit()
            
        if "search on youtube" in query:
            speak("what do you want to search sir")
            problem1=myCommand()
            webbrowser.open("https://youtube.com/search?q=%s" %problem1)
            speak('done sir')
            sys.exit()
            
        if "tell me about something" in query:
            speak("what you want to ask sir")
            problem2=myCommand()
            results = wikipedia.summary(problem2, sentences=2)
            print(results)
            speak(results)
            
            
        '''creating folders, renaming it, dug into it or come out and deleting it'''
        
        
        if "create a new folder" in query or  "create a folder" in query:
            speak('what will be the name of the folder sir?')
            problem=myCommand()
            problem=problem.lower()
            path1=path+'\\'+problem
            os.mkdir(path1)
            speak('folder created')
            
        if "open folder" in query:
            speak('name the folder sir')
            problem=myCommand()
            path=path+'\\'+problem
            speak('done sir! we are in the folder')
            
        if "come back to default server location" in query:
            path="S:"
            speak('done sir! we are in server location')
        
        if "in which folder i am" in query:
            speak(path)
            
        if "change path" in query:
            speak('type the path you want sir')
            path=str(input('path: '))
            speak('done sir')
        
        if "delete folder" in query:
            speak('name the folder you want to delete')
            problem=myCommand()
            path1=path+'\\'+problem
            os.rmdir(path1)
            speak('done sir! folder deleted')
            
        if "list all directories" in query:
            files=os.listdir(path)
            for name in files:
                speak(name)
        
            
        '''creating files, renaming it, dug into it or come out and deleting it'''
            
        if "create a file" in query or "create a new file" in query:
            speak('what will be the name of the file sir?')
            problem=myCommand()
            problem=problem.lower()
            path1=path+'\\'+problem+'.txt'
            file=open(path1,"w")
            speak('what do you want to write in file sir?')
            data=myCommand()
            if(data=='nothing'):
                speak('ok sir')
                file.close()
            else:
                file.write(data+"\n")
                speak('done sir')
                file.close()
                
        if "open file and read it" in query:
            speak('what is the name of the file sir?')
            problem=myCommand()
            problem=problem.lower()
            path1=path+'\\'+problem+'.txt'
            file=open(path1,"r")
            for each in file:
                speak(each)
            file.close()
                
        if "write in file" in query:
            speak('what is the name of the file sir?')
            problem=myCommand()
            problem=problem.lower()
            path1=path+'\\'+problem+'.txt'
            file=open(path1,"a")
            speak('what do you want to write in file sir?')
            data=myCommand()
            file.write("\n")
            file.write(data)
            file.close()
            speak('done sir')
            
        if "delete file" in query:
            speak('what is the name of the file sir?')
            problem=myCommand()
            problem=problem.lower()
            path1=path+'\\'+problem+'.txt'
            os.remove(path1)
            speak('done sir! file deleted')
            
        '''playing music'''
        
        if "play my favourite song" in query:
            os.system("S:\\music\\theme.mp3")
            sys.exit()

        if "play music" in query:
            music_folder = "S:\\music\\songs"
            music = []
            files=os.listdir(music_folder)
            for name in files:
                if ".mp3" in name:
                    music.append(name)
            random_music = music_folder + "\\" + random.choice(music)
            os.system("start "+random_music)
            sys.exit()
            
            
        '''playing movie'''
        
        if "play movie" in query:
            movie_folder="S:\\movie"
            movie = []
            files=os.listdir(movie_folder)
            for name in files:
                if ".mp4" in name:
                    movie.append(name)
            random_movie = movie_folder + "\\" + random.choice(movie)
            os.system("start "+random_movie)
            sys.exit()
            
            
        
            
            
            
            
                
          
            
            
        
        
        
        
