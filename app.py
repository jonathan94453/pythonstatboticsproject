from flask import Flask, request, jsonify
import Statboticsintegration 
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

if __name__ == '__main__':
    app.run(debug=True) 