
import tkinter as tk 
from tkinter import font
from typing import Tuple 
import api 
import dataprocessing 
import customtkinter as ctk 

 
class EPAPage(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent) 
       

        parent.geometry("900x900")
        label1 = ctk.CTkLabel(parent, text="welcome to epa button") 
        label1.pack(pady=10, padx=10) 


class welcomepage(ctk.CTkFrame):
    def __init__(self, parent):
          super().__init__(parent)
       
        parent.geometry("800x800")  
        
        label1 = ctk.CTkLabel(parent, text="welcometomainpage")
        label1.pack(pady=10, padx=10)  
        def switchpage():
            switch = EPAPage(parent)
            switch.pack()
        button1 = ctk.CTkButton(parent, text="EpaButton", command=switchpage())



if __name__ == "__main__":  
    root = ctk.CTk() 
    epa_page = welcomepage(root)
    epa_page.pack() 
    root.mainloop()