import tkinter as tk
import customtkinter as ctk
import api 

import dataprocessing 
class EPAPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label1 = ctk.CTkLabel(self, text="Welcome to EPA Page")
        label1.pack(pady=10, padx=10)

class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label1 = ctk.CTkLabel(self, text="Welcome to Main Page")
        self.label1.pack(pady=10, padx=10)
        button1 = ctk.CTkButton(self, text="EPA Page", command=self.switch_page)
        button1.place(x=450, y=100) 
        button1.pack(padx=450, pady=100)

        self.control = dataprocessing.appcontrol()
        self.teamentrybox = ctk.CTkEntry(parent, width=80) 
        self.teamentrybox.bind("<Return>", self.onenter)
        self.teamentrybox.pack(padx=100, pady=200) 
    def onenter(self, event):
        self.control.on_enter(self.teamentrybox) 
        response = self.control.getteamresponsename() 
        self.label1.configure(text=response)









    def switch_page(self):
        # Hide the current page
        self.pack_forget()
        # Show the EPA page
        epa_page.pack()

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("900x900")
    # Create instances of the WelcomePage and EPAPage
    welcome_page = WelcomePage(root)
    epa_page = EPAPage(root)
    
    # Initially, pack the welcome page
    welcome_page.pack()
    
    root.mainloop()