
import tkinter as tk 
from tkinter import font 
import api 
import dataprocessing 


root = tk.Tk()




root.geometry("900x900")


root.configure(background="blue") 
root.title("Statbotics APP") 

mainheadingfont = font.Font(size=30)



mainheading = tk.Label(root, text="STATBOTICS FRC APP", font= mainheadingfont)
mainheading.place(x=300, y=12) 



entry = tk.Entry(root, width=20)  
control = dataprocessing.appcontrol() 
entry.place(x=350, y=450) 
def onenter(event):
    control.on_enter(entry) 
    responsename = control.getteamresponsename()
    answerlabel.config(text=responsename)

entry.bind('<Return>', onenter)  
answerlabel = tk.Label(root, text="", font=mainheadingfont) 
answerlabel.place(x=10,y=200)

# stats.get_team_name(int(entry.get())) 

# adding the main loop function on the tk object which allows the app to run with the changes made 






root.mainloop() 