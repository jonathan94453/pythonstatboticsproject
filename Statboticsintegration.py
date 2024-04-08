import statbotics 

statbotics = statbotics.Statbotics() 


class teaminformation: 
    def __init__(self): 
        self.statbotics = statbotics 
    def get_team_name(self, teamnumber): 
        json_response = self.statbotics.get_team(teamnumber) 
        teamname = json_response.get("name")  
        return teamname 
    def get_team_epa(self, teamnumber): 
        json_response = self.statbotics.get_team(teamnumber) 
        teamepa = json_response.get("norm_epa") 
        return teamepa 