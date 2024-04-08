import statbotics

stats = statbotics.Statbotics() 

printstatement = stats.get_team_events(254, 2024,fields=[""])
 
print(printstatement)