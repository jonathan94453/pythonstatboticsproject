import tkinter as tk
import customtkinter as ctk
import api 

import dataprocessing 
class EPAPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label1 = ctk.CTkLabel(parent, text="Welcome to EPA Page")
        self.label1.place(x=100, y=100)

class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, epa_page):
        super().__init__(parent)
        
        welcomefont = ctk.CTkFont(size=80)


        self.label1 = ctk.CTkLabel(parent, text="Welcome to Main Page", font=welcomefont)
        self.label1.pack(pady=10, padx=10)
        self.button1 = ctk.CTkButton(parent, text="EPA Page", command=self.switch_page)
        self.button1.place(x=100, y=200)

        self.control = dataprocessing.appcontrol()
        self.teamentrybox = ctk.CTkEntry(parent, width=80) 
        self.teamentrybox.bind("<Return>", self.onenter)
        self.teamentrybox.pack(padx=100, pady=100) 


        self.epa_page = epa_page 

    def onenter(self, event):
        self.control.on_enter(self.teamentrybox) 
        response = self.control.getteamresponsename() 
        self.label1.configure(text=response)









    def switch_page(self):
        # Hide the current page
        self.label1.pack_forget()
        self.button1.pack_forget()
        self.teamentrybox.pack_forget()
        # Show the EPA page
        self.epa_page.pack() 

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("900x900")
    root.title("4329 Scouting Integration Project")
    # Create instances of the WelcomePage and EPAPage
    epa_page = EPAPage(root)
    welcome_page = WelcomePage(root, epa_page) 
    
    # Initially, pack the welcome page
    welcome_page.pack()
    
    root.mainloop()