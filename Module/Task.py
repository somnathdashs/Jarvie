import time
import datetime
import webbrowser
import pyjokes,random
import wikipedia
from   Module.Sound import *
import wolframalpha 
from   Module.Personal import *
import pywhatkit.whats as whatsapp
import smtplib
import requests
import bs4 #pip install beautifulsoup4
import pyautogui
from tkinter import Tk
import os

Wolfarm_app= wolframalpha.Client(WolfarnID)



Websites={
    "google":"https://google.com/",
    "instagram":"https://www.instagram.com/",
    "facebook":"https://www.facebook.com/",
    "amazon":"https://www.amazon.in/",
    "youtube" : "https://www.youtube.com/"
}


def OpenWebsite(Command):
    Web_title=list(Websites.keys())
    if any(i in Command for i in Web_title):
        titles=[i for i in Web_title if i in Command]
        for title in titles:
            webbrowser.open_new_tab(Websites[title])
        
        return "Opening {} website.".format(titles),1

    else:
        return "website not found in database. Trying to find local app or software",0


def OpenApps(Command):
    Command=str(Command).replace("open","").lower()
    pyautogui.hotkey("winleft")
    pyautogui.typewrite(Command,0.2)
    time.sleep(0.5)
    pyautogui.hotkey("enter")



def WhisMe():
    greeting=""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        greeting="Good morning"
    elif hour>=12 and hour<16:
        greeting="Good Afternoon"
    else:
        greeting="Good Evening"
    return greeting
        
def Google_search(query):
    Url="https://www.google.com/search?q="+query
    webbrowser.open_new_tab(Url)


def Tell_Joke():
    c=['neutral', 'chuck', 'all']
    catgo=random.choice(c)
    return pyjokes.get_joke(category=catgo)

def Get_wiki(search):
    try:
        print("Jarvis: ",wikipedia.summary(search,5))
        Speak(wikipedia.summary(search,2),False)
    except:
        Speak("Having some problem while fetching data.")
    
def Wolfarm_Alpha(quary):
    respons=Wolfarm_app.query(quary)
    respons=(next(respons.results).text)
    return respons
    

def Send_msg_whatsapp_Grp(ID,Msg):
    whatsapp.sendwhatmsg_to_group_instantly(ID,Msg,wait_time=7)

def Send_msg_whatsapp_indivisual(Mob,Msg):
    whatsapp.sendwhatmsg_instantly(Mob,Msg,wait_time=7)

def Send_Email(To,Msg):
    Mail=smtplib.SMTP("smtp.gmail.com",587)
    Mail.connect("smtp.gmail.com",587)
    Mail.ehlo()
    Mail.starttls()
    Mail.ehlo()
    Mail.login("Your_Email@xyz.com",EmailPass)
    Mail.sendmail("Their_Email@xyz.com",To,Msg)
    Mail.close()
    return "Mail has been send successfully."
    

def Google_web_search(query):
    base_url="https://google.com/search?q="
    url=base_url+query
    requests_result=requests.get(url)
    soup=bs4.BeautifulSoup(requests_result.text,"html.parser")
    ans=soup.find("div",class_="BNeawe").text
    return ans


def Weather(query):
    temp=Google_web_search(query)
    return temp



def Hot_Word_Detection():
    Hot_Words=["jarvis","wake"]
    Speak("I am going to take a power nap")
    dots=[".","..","...","....","....."]
    count=0
    while True:
        print("Jarvis is sleeping"+dots[count],end="\r")
        sentence=str(Listen(IsSleep=True)).lower()
        if any(i in sentence for i in Hot_Words):
            Answer=["Hello sir, how may i help you","Nice to meet you again!","Hey, Good to see you again"]
            Ans=random.choice(Answer)
            Speak(Ans)
            break
        count+=1
        if count>=len(dots):
            count=0
            print("",end="\r")


def WriteSen(text):
    time.sleep(0.5)
    pyautogui.typewrite(text,0.1)

def ReadSelectedText():
    root = Tk()
    root.withdraw()
    pyautogui.hotkey("ctrl","c")
    clipboard=root.clipboard_get()
    return clipboard


def SelecteALL():
    pyautogui.hotkey("ctrl","a")

def Copy():
    pyautogui.hotkey("ctrl","c")

def Cut():
    pyautogui.hotkey("ctrl","x")

def Paste():
    pyautogui.hotkey("ctrl","v")
