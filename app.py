from flask import Flask, request, jsonify 
import dataprocessing 
app = Flask("4329-Statbotics-Integration") 

base_url = "/LutheranRoboteers"


@app.route(base_url + "/hello", methods=['GET'])
def hello():
    return "hello"

@app.route(base_url + "/TeamName/<Teamnumber>", methods=['GET']) 
def giveteamname(Teamnumber):
    control = dataprocessing.appcontrol() 
    control.on_enter(Teamnumber)
    teamname = control.getteamresponsename()
    return teamname  

@app.route("/LutheranRoboteers/TeamEPA/<Teamnumber>", methods=['GET'])
def giveteamcurrentepa(Teamnumber): 
    control = dataprocessing.appcontrol() 
    control.findteamepa(Teamnumber)  
    teamnormepa = control.getteamnormepa() 
    if teamnormepa is not None:
        return jsonify(teamnormepa)  # Convert to JSON and return
    else:
        return jsonify({'error': 'Team EPA not found'}), 404  
        return teamnormepa 

if __name__ == '__main__':
    app.run(debug=True) 