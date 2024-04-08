import statbotics 
import Statboticsintegration 
class appfunctions: 
    def get_user_input(entry): 
        userinput = "test" 






class appcontrol:  
    def __init__(self):
        self.teamresponsename = None
        self.stats = Statboticsintegration.teaminformation() 
    def exitapp(self, root): 
        root.destroy() 


    def on_enter(self, entry): 
        self.teamresponsename = self.stats.get_team_name(int(entry)) 




    def findteamepa(self, teamnumber):
        self.teamcurrentepa = self.stats.get_team_epa(int(teamnumber))  

    def findteamwinrate(self, teamnumber): 
        self.teamwinrate = self.stats.get_team_win_rate(int(teamnumber)) 


    def getteamresponsename(self): 
        return self.teamresponsename
    def getteamnormepa(self):
        return self.teamcurrentepa 
    def get_teamwinrate(self):
        return self.teamwinrate 