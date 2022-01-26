import json
import requests 
import smtplib, ssl

def get_weather():
    # Email settings
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sender@gmail.com"  # Enter your address
    receiver_email = "receiver@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    
    # API settings for OpenWeather
    api_key = 'ee121a67d0c1335e5b072651915ee973'
    lat = 43.33
    lon = -89.02
    part = 'minutely,alerts'
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={APIkey}&units=imperial".format(lat = lat, lon = lon, APIkey = api_key, part = part )
    r = requests.get(base_url)
    j = json.loads(r.text)
    
    # Get daily temp data  
    dailyTemp = j['daily'][0]['temp']

    # Temps during the day
    morn_temp = dailyTemp['morn']
    day_temp = dailyTemp['day']
    eve_temp = dailyTemp['eve']
    night_temp = dailyTemp['night']
    low_temp = dailyTemp['min']
    high_temp = dailyTemp['max']

    # Weather description
    weather_description = j['daily'][0]['weather'][0]['description']

    # Write email message
    message = (\
    "Subject: Todays Weather Brief\n"
    \
    "Here are the temperatures for today - \n"
    "Low: " + str(low_temp) + " degrees\n"
    "High: " + str(high_temp) + " degrees\n"
    "Morning: " + str(morn_temp) + " degrees\n"
    "Daytime: " + str(day_temp) + " degrees\n"
    "Evening: " + str(eve_temp) + " degrees\n"
    "Nighttime: " + str(night_temp) + " degrees\n"
    "Expect " + str(weather_description) + " today"
    )

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)    
get_weather()