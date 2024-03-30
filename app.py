
import tkinter as tk 
from tkinter import font 
import api 
import dataprocessing 
import customtkinter 

 
#app object 
root = customtkinter.CTk()



#set the size of the customtkinter object 
root.geometry("900x900")

root.title("Statbotics app") 
#Font object 
mainheadingfont = customtkinter.CTkFont(size=30)



mainheading = customtkinter.CTkLabel(root, text="STATBOTICS FRC APP", font= mainheadingfont)
Introheading = customtkinter.CTkLabel(root, text="Welcome to your FRC Statistics Portal", font=mainheadingfont)
mainheading.place(x=300, y=12) 
Introheading.place(x=300, y=80)

epabutton = customtkinter.CTkButton(root, width=40, command=)




# quit logic 
def quitcommand():
    control.exitapp(root)
quitbutton = customtkinter.CTkButton(root, width=40, text="QUIT", command=quitcommand)
quitbutton.place(x=30,y=100)









# loopend
root.mainloop() 