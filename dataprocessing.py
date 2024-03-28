import statbotics 
import api 
class appfunctions: 
    def get_user_input(entry): 
        userinput = "test" 






class appcontrol:  
    def __init__(self):
        self.teamresponsename = None

    def exitapp(self, root): 
        root.destroy() 
    def on_enter(self, entry): 
        entry_text = entry.get()
        stats = api.teaminformation() 
        self.teamresponsename = stats.get_team_name(int(entry_text)) 
    def getteamresponsename(self): 
        return self.teamresponsename