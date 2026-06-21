import requests
API_KEY="9a6faba22dc1c60c317ab386f122266c"
def get_weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data=requests.get(url).json()
    temp=data["main"]["temp"]
    return temp 