import os, time, argparse, pyfiglet, numpy as np, requests
from colorama import Fore, Style, init

init(autoreset=True)
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# ASCII art for weather
WEATHER_ART = {
    "Clear": """
    ☀️
   /|\\
  / 0 \\
 ( === )
  `---' 
    """,
    "Clouds": """
     ☁️
    / 0 \\
   ( === )
    `---' 
    """,
    "Rain": """
     ☔
    / 0 \\
   ( === )
    `---' 
    """,
    "Snow": """
     ❄️
    / 0 \\
   ( === )
    `---' 
    """,
    "Thunderstorm": """
     ⚡
    / 0 \\
   ( === )
    `---' 
    """,
    "Mist": """
     🌫️
    / 0 \\
   ( === )
    `---' 
    """,
    "default": """
     🌈
    / 0 \\
   ( === )
    `---' 
    """
}


def get_weather(city):
    """Fetch current weather"""
    try:
        r = requests.get(BASE_URL, params={"q":city,"appid":API_KEY,"units":"metric"})
        r.raise_for_status(); d=r.json()
        return {"temp":d["main"]["temp"],"feels_like":d["main"]["feels_like"],
                "humidity":d["main"]["humidity"],"pressure":d["main"]["pressure"],
                "cond":d["weather"][0]["main"],"desc":d["weather"][0]["description"].capitalize(),
                "city":d["name"],"country":d["sys"]["country"]}
    except: return None

def get_forecast(city):
    """Fetch tomorrow + 5-day forecast"""
    try:
        r=requests.get(FORECAST_URL,params={"q":city,"appid":API_KEY,"units":"metric"})
        r.raise_for_status(); d=r.json(); now=time.time()
        tomorrow=None; forecast={}
        for i in d["list"]:
            dt=i["dt"]
            if not tomorrow and dt>now+24*3600:
                tomorrow={"temp":i["main"]["temp"],"cond":i["weather"][0]["description"].capitalize()}
            date=i["dt_txt"].split()[0]; hour=int(i["dt_txt"].split()[1].split(":")[0])
            if hour==12 and date not in forecast: forecast[date]={"temp":i["main"]["temp"],
                                                            "cond":i["weather"][0]["description"].capitalize()}
            if len(forecast)>=5: break
        return tomorrow, forecast
    except: return None, None

def evolve_temp_matrix(T0,T_env,k=0.03,dt=0.2,steps=40,zones=5):
    """Simulate temperature across zones using matrix"""
    T=np.full((steps+1,zones),T0,float)
    for t in range(steps): T[t+1,:]=T[t,:]+(-k*(T[t,:]-T_env)*dt)
    return T

def temp_bar(temp,min_t=-10,max_t=40,width=40):
    """ASCII temp bar"""
    fill=int((temp-min_t)/(max_t-min_t)*width)
    return "█"*fill+"-"*(width-fill)

def animate_weather(data,zones=5):
    temp=data["temp"]; T_env=temp-5 if temp>15 else temp+5
    sim=evolve_temp_matrix(temp,T_env,steps=40,zones=zones)
    for i,row in enumerate(sim):
        avg=row.mean(); os.system("cls" if os.name=="nt" else "clear")
        print(Fore.CYAN+pyfiglet.figlet_format(f"{data['city']}, {data['country']}")+Style.RESET_ALL)
        print(WEATHER_ART.get(data["cond"],WEATHER_ART["default"]))
        print(f"Cond:{data['desc']} | Temp avg:{avg:.2f}°C | Feels:{data['feels_like']}°C")
        print(f"Hum:{data['humidity']}% | Press:{data['pressure']} hPa\n")
        print(temp_bar(avg)); print(f"Step {i+1}/{len(sim)} | Zones:{zones}")
        time.sleep(0.08)
    print("\nSimulation complete ")

def main():
    parser=argparse.ArgumentParser(description="Current weather info")
    parser.add_argument("city",type=str,help="City name"); args=parser.parse_args()
    data=get_weather(args.city)
    if data: animate_weather(data)
    tomorrow, forecast=get_forecast(data["city"])
    if tomorrow: print(f"\nTomorrow: {tomorrow['temp']:.2f}°C | {tomorrow['cond']}")
    if forecast:
        print("\n5-day Forecast:")
        for date,info in forecast.items(): print(f"{date}: {info['temp']:.2f}°C | {info['cond']}")

if __name__=="__main__": main()
