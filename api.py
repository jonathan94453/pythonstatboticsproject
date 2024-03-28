import statbotics 

statbotics = statbotics.Statbotics() 


class teaminformation: 
    def get_team_name(self, teamnumber): 
        json_response = statbotics.get_team(teamnumber) 
        print(json_response.get("name")) 
        