import statbotics 
class appfunctions: 
    def get_user_input(entry): 
        userinput = "test" 

   



class appcontrol: 
    def exitapp(self, root): 
        root.destroy() 
    def on_enter(self, entry):
        entry_text = entry.get()
        return entry_text 
