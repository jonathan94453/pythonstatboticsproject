import statbotics 
import tkinter as tk 


from tkinter import font 

root = tk.Tk()
stats = statbotics.Statbotics() 

root.geometry("900x900")


root.configure(background="blue") 
root.title("Statbotics APP") 

mainheadingfont = font.Font(size=30)

mainheading = tk.Label(root, text="FRC EPA Info", font= mainheadingfont)
mainheading.place(x=300, y=12) 




entry = tk.Entry(root, width=20)  

entry.place(x=350, y=450) 
 


json_response = stats.get_team(4329) 

teamepa = json_response.get("norm_epa_recent") 

teamname = json_response.get("name") 


# adding the main loop function on the tk object which allows the app to run with the changes made 
root.mainloop() 