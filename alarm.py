import time
import webbrowser
from datetime import datetime
class Openwebpage:
    def openwebsite(Set_Alarm,Actual_time,url):
        while(Actual_time!=Set_Alarm):
            print("This time is"+Actual_time)
            now=datetime.now()
            Actual_time=now.strftime("%H:%M:%S")
            time.sleep(1)
        if(Actual_time==Set_Alarm):
            print("You should open the webpage now")
            webbrowser.open(url)
class Alarm:
    def __init__(self):
        Set_Alarm=input("Enter the time you want to open the website as H:M:S:")
        url=input("Enter the website you want")
        now=datetime.now()
        Actual_time=now.strftime("%H:%M:%S")
        Openwebpage.openwebsite(Set_Alarm,Actual_time,url)

obj=Alarm()
