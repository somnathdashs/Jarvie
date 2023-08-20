from Module.Sound import *
from Module.Task import *
from Module.Contact import *
import random,pywhatkit
from Module.Alarm import alarm,Reminder
import threading
# from PPP_Lang_Translation import Languages,Translator
from Module.Time_table_schedule import Start_Time_Table
import os

Sleep_in_null_command=5
Current_null_command=0


Speak(WhisMe())

while True:
    if Current_null_command>=Sleep_in_null_command:
        Hot_Word_Detection()

    Command=Listen()

    if not Command :
        continue

    if Command==1:
        Current_null_command+=1
        continue

    if Current_null_command>0 and Command and Command!=1:
        Current_null_command=0


    print("You: ",Command)
    Command=str(Command)
    # Command=Translator(Command,Languages.Hindi,Languages.English).translate
    Command=str(Command).lower()
    if "time" in Command:
        Current_Time=datetime.datetime.now().strftime('%I:%M %p')
        Speak("Current time is "+Current_Time)
    
    elif "date" in Command:
        Today_Date=datetime.datetime.now().strftime("%d %m %Y") #25 06 2023
        Speak("Today's Date is "+Today_Date)
    
    elif "your name" in Command or "what name" in Command or "name" in Command or ("who" in Command and "you" in Command):
        Answer=["Hey, I am jarvis, an artificial intelligence.","I am an artificial intelligence, people called me jarvis"," I am a computer program and my name is jarvis"]
        Ans=random.choice(Answer)
        Speak(Ans)
        time.sleep(0.3)
        Speak("How may i help you?")
    
    elif "bye" in Command:
        Speak("Have a good day.")
        break

    elif "music" in Command or "song" in Command or "play" in Command:
        topic=Command.replace("play","").replace("music","").replace("song","")
        pywhatkit.playonyt(topic)
    
    elif "hii" in Command or "hello" in Command or "hey" in Command:
        Answer=["Hello sir, how may i help you","Nice to meet you again!","Hey, Good to see you again"]
        Ans=random.choice(Answer)
        Speak(Ans)

    elif "thanks"in Command or "thank"in Command or "thankful"in Command:
        Answer=["I an happy to hear that","Welcome"]
        Ans=random.choice(Answer)
        Speak(Ans)
    
    elif "google search" in  Command:
        Speak("What you want me to search ?")
        query=Listen()
        Google_search(query)
        
    elif "joke" in Command or ("make" in Command and ("laugh" in Command or "smile" in Command or "happy" in Command)and "me" in Command ):
        Speak("Sure, here is a joke")
        time.sleep(0.2)
        Speak(Tell_Joke())
    
    elif ("wikipedia" in Command or "wiki" in Command and "search" in Command) or ("tell" in Command and "about" in Command and "me" in Command):
        ignor_word=["wikipedia","wiki","search","tell","about","me"]
        if ("wikipedia" in Command or "wiki" in Command and "search" in Command):
            Speak("what you want about to ask ?")
            query=str(Listen())
        else:
            query=Command

        for i in ignor_word:
            query.replace(i,"")
        Get_wiki(query)
    
    elif "alarm" in Command:
        Speak("Alright! Set it for when?")
        Timing=Listen()
        Timing=str(Timing).replace(".","")
        Timing=Timing.upper()
        threading.Thread(target=alarm,args=[Timing]).start()

    elif "send" in Command and "whatsapp" in Command or ("message" in Command or "whatsapp" in Command):
        Speak("To whome you want to send message ?")
        Person=Listen()
        if IsinContact(Person):
            contactInfo=Get_Mob_or_GID(Person)
            Speak("What message you want to send ?")
            Msg=Listen()
            if IsGroup(Person):
                Send_msg_whatsapp_Grp(contactInfo,Msg)
            else:
                Send_msg_whatsapp_indivisual(contactInfo,Msg)
        else:
            Speak(Get_Mob_or_GID(Person))

    elif "send" in Command and "email" in Command:
        Speak("Whome you want to send email ?")
        statment=Listen()
        if Is_In_Email_Contact(statment):
            Speak("What is the message you want to send ?")
            Msg=Listen()
            To=Get_Email_add(statment)
            Send_Email(To,Msg)
            
        else:
            Speak(Get_Email_add(statment))
    
    elif "weather" in Command or "temperature" in Command:
        pro=[" at "," in "," of "," on "]
        if any(i in Command for i in pro):
            Speak(Weather(Command))
        else:
            Speak("Of which city you want to known the weather?")
            city=Listen()
            Speak(Weather("What is the current weather of"+city))

    elif "reminder" in Command or "set reminder" in Command:
        Speak("what is your reminder ?")
        reminder=Listen()
        Speak("When you want to set the reminder ?")
        Timming=Listen()
        Timming=str(Timming).replace(".","")
        Timming=Timming.upper()
        threading.Thread(target=Reminder,args=[Timming,Speak,reminder]).start()
        
    elif "sleep" in Command or "nap" in Command or "rest" in Command:
        Hot_Word_Detection()

    elif "start" in Command and ("time table"in Command or "routine" in Command or "scheldule" in Command):
        Start_Time_Table(Speak) 
    
    elif "open" in Command or ("website" in Command ):
        x,y=OpenWebsite(Command)
        Speak(x)
        if y==0:
            OpenApps(Command)
        
    elif "shutdown" in Command or "shut down" in Command:
        Speak("Are you really want to shut down the pc ?")
        YN=Listen()
        if "yes" in YN or "yeah" in YN:
            os.system("shutdown /s /t 5")
        else:
            pass

    elif "restart" in Command or "restart" in Command:
            Speak("Are you really want to restart the pc ?")
            YN=Listen()
            if "yes" in YN or "yeah" in YN:
                os.system("shutdown /r /t 5")
            else:
                pass
            
    elif "write" in Command or "type" in Command and ("word" in Command or "para" in Command or "sentence" in Command or "paragraph" in Command):
        Speak("What should i write for you ?")    
        Text = Listen()
        WriteSen(Text)

    elif "read" in Command and ("sentence" in Command or "para" in Command or "paragraph" in Command or "select" in Command):
        Speak(ReadSelectedText())
    
    elif "select" in Command and "all" in Command:
        SelecteALL()
        Speak("Selected successfully")

    
    elif "copy" in Command:
        Copy()
        Speak("Copied successfully")

    elif "cut" in Command:
        Cut() 
        Speak("Cut successfully")

    elif "paste" in Command or ("move" in Command and ("here" in Command)):
        Paste() 
        Speak("pasted successfully")



    elif Command!=None: 
        try:
            ans=Wolfarm_Alpha(Command)
            Speak(ans)
        except Exception as E:
            Speak("I am unable to understand your query. Try again")

    



        

    
        

