import app 

import customtkinter as ctk 


class Newpage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent) 
        self.controller = controller 



        controller = ctk.CTkFrame(self)
        controller.pack()
        label1 = ctk.CTkLabel(self, text="hello epa")
        label1.pack()