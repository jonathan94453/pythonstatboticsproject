import statbotics 
import tkinter as tk 

root = tk.Tk()
stats = statbotics.Statbotics() 

root.configure(background="black") 
root.title("Statbotics APP") 

entry = tk.Entry(root, width=40, ) 
entry.pack(pady=10) 


json_response = stats.get_team(4329) 

teamepa = json_response.get("norm_epa_recent") 

teamname = json_response.get("name") 


# adding the main loop function on the tk object which allows the app to run with the changes made 
root.mainloop() 