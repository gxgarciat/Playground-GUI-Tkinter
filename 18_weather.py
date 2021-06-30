from tkinter import *
from PIL import ImageTk,Image
import requests
import json

# This code will use API and connect to them by Tkinter

root = Tk()

root.title('Weather in:')
root.geometry("500x100") # This will define the starting size of the GUI


# Create Zipcode Lookup function
def zipLookup():
    zip.get()
    #zipLabel = Label(root,text=zip.get())
    #zipLabel.pack()
    #zipLabel.grid(row=1,column=0,columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" +zip.get() + "&date=2021-06-30&distance=25&API_KEY=91562611-885B-45AC-80C5-74D1FBD3C65E")
        api = json.loads(api_request.content)
        #print(type(api_request))
        #print(type(api))
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = Label(root,text=city + " Air Quality " + str(quality) + " " + category,font=("Helvetica",15),background=weather_color)
        #myLabel.pack()
        myLabel.grid(row=1,column=0,columnspan=2)

    except Exception as e: # -*- coding: utf-8 -*-
        api = "Error.."


zip = Entry(root)
#zip.pack()
zip.grid(row=0,column=0,stick=W+E+N+S)

zipButton = Button(root,text="Lookup Zipcode",command=zipLookup)
#zipButton.pack()
zipButton.grid(row=0,column=1,stick=W+E+N+S)


root.mainloop()
