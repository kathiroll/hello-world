#Atieve Wadhwa
#2017031
#Homework 1 CSE 101
# -*- coding: utf-8 -*-
import json,urllib2,datetime
# function to get weather response
def weather_response(location, API_key):
	url="http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+API_key
	x=urllib2.urlopen(url)
	y=x.read()
	#print y
	return y
#a = weather_response(loca, API)

# function to check for valid response 
def has_error(loca,json):
	cityin = json.index("name") + 7
	city = json[cityin:((json.find(",",-57))-1)]
	#print city
	if(loca.lower()==city.lower()):
		#print False
		return False
	else:
		#print True
		return True

#has_error(a, API)

def get_temperature (json, n=0, t="03:00:00"):
	now = datetime.datetime.now()
	date=now.day+n
	a = "2017-09-0"+str(date)+" "+t
	start = json.index(a)
	temperature = (json.find("temp",start)) + 6
	temp=json[temperature:(json.index(",",temperature))]
	temp = float(temp)
	#print temp
	return temp

#get_temperature(a,2,"09:00:00")

def get_humidity(json, n=0, t="03:00:00"):
	now = datetime.datetime.now()
	date=now.day+n
	a = "2017-09-0"+str(date)+" "+t
	start = json.index(a)
	humidity = (json.find("humid",start))+10
	humid=json[humidity:(json.find(",",humidity))]
	humid= float(humid)
	#print humid
	return humid

#get_humidity(a,2,"09:00:00")

def get_pressure(json, n=0, t="03:00:00"):
	now = datetime.datetime.now()
	date=now.day+n
	a = "2017-09-0"+str(date)+" "+t
	start = json.index(a)
	pressure = (json.find("pressure",start))+ 10
	pres=float(json[pressure:(json.find(",",pressure))])
	#print pres
	return pres

#get_pressure(a,2,"09:00:00")

def get_wind(json, n=0, t="03:00:00"):
	now = datetime.datetime.now()
	date=now.day+n
	a = "2017-09-0"+str(date)+" "+t
	start = json.index(a)
	wind = (json.find("speed",start))+7
	speed=float(json[wind:(json.find(",",wind))])
	#print speed
	return speed

#get_wind(a,2,"09:00:00")

def get_sealevel(json, n=0,t="03:00:00"):
	now = datetime.datetime.now()
	date=now.day+n
	a = "2017-09-0"+str(date)+" "+t
	start = json.index(a)
	sea = (json.find("sea_level",start))+11
	seal=float(json[sea:(json.find(",",sea))])
	#print seal
	return seal

#get_sealevel(a,2,"09:00:00")