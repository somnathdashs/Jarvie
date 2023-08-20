import json
import datetime
import threading
from plyer import notification


def Start_Time_Table(speak):
    threading.Thread(target=__Start,args=[speak]).start()


def __Start(speak):
    Time_Table=json.load(open("./Module/Datas/schedule.json","r"))
    days=list(Time_Table.keys())
    today=days[datetime.datetime.now().weekday()]
    times=list(Time_Table[today].keys())
    Acurracy=[]
    for time in times:
        Diff=str(datetime.datetime.now().strptime(time,"%I:%M %p"))
        Diff=Diff[11:-3]
        hour=int(Diff[:2])
        val=datetime.datetime.now().hour-hour
        Acurracy.append(val if val<=0 else -5000 )

    count_start=Acurracy.index(max(Acurracy))
    times=times[count_start:]

    if all(i==-5000 for i in Acurracy):
        times=[]

    for time in times:
        Diff=str(datetime.datetime.now().strptime(time,"%I:%M %p"))
        Diff=Diff[11:-3]
        hour=int(Diff[:2])
        min=int(Diff[3:5])
        if datetime.datetime.now().minute>min and datetime.datetime.now().hour==hour:
            continue
        elif datetime.datetime.now().minute!=min:
            print(f"Next Schedule is set at {time}")

        while True:
            if hour==datetime.datetime.now().hour:
                if min==datetime.datetime.now().minute:
                    msg=Time_Table[today][time]
                    notification.notify(
                        title="Schedul from your Time Table",
                        message=msg,
                        timeout=5 # displaying time
                    )
                    speak(msg)
                    break

    speak("Your Time table schedule is successfully completed.")

if __name__=="__main__":
    Start_Time_Table(print)