import datetime
import winsound
from playsound import playsound
from time import sleep

def alarm(Timeing):
    Diff=str(datetime.datetime.now().strptime(Timeing,"%I:%M %p"))
    Diff=Diff[11:-3]
    hour=int(Diff[:2])
    min=int(Diff[3:5])
    print(f"Alarm has been set for {Timeing}")
    while True:
        if hour==datetime.datetime.now().hour:
            if min==datetime.datetime.now().minute:
                winsound.PlaySound("abc",winsound.SND_LOOP)
            elif min<datetime.datetime.now().minute:
                break


def Reminder(Timeing,speak,text):
    Diff=str(datetime.datetime.now().strptime(Timeing,"%I:%M %p"))
    Diff=Diff[11:-3]
    hour=int(Diff[:2])
    min=int(Diff[3:5])
    speak(f"Reminder has been set for {Timeing}")
    No_of_Time=7
    count=0
    while True:
        if hour==datetime.datetime.now().hour:
            if min==datetime.datetime.now().minute:
               speak(text)
               count+=1
               sleep(0.5)
            if count==No_of_Time:
                break




if __name__=="__main__":
    alarm("08:35 PM")