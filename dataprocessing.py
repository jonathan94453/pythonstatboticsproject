import statbotics 
import Statboticsintegration 
class appfunctions: 
    def get_user_input(entry): 
        userinput = "test" 






class appcontrol:  
    def __init__(self):
        self.teamresponsename = None

    def exitapp(self, root): 
        root.destroy() 
    def on_enter(self, entry): 
        stats = Statboticsintegration.teaminformation() 
        self.teamresponsename = stats.get_team_name(int(entry)) 
    def getteamresponsename(self): 
        return self.teamresponsename