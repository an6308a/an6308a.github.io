from flask import Flask, render_template
from flask import request
app = Flask( __name__, instance_relative_config=True )
from wmata2 import station_info, travel_info, station_dict, money

@app.route( "/" )
def hello():
    station_list = station_info()["Stations"]
    return render_template("newhtml.html", station_list=station_list)


@app.route("/travel")
def results():
    origin = request.args.get("origin", '')
    destination = request.args.get("destination", '')
    info = travel_info(origin, destination)
    return render_template(
        "travel.html",
        origin=station_dict[origin],
        destination=station_dict[destination],
        travel_time=info["StationToStationInfos"][0]["RailTime"],
        offpeak_fare=money(info["StationToStationInfos"][0]["RailFare"]["SeniorDisabled"]),)


if __name__ == "__main__":
    app.run()
