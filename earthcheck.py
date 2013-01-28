import urllib, csv

def getCSV():
	webcsv = urllib.urlopen('http://earthquake.usgs.gov/earthquakes/feed/csv/all/hour')
	csvreader = csv.reader(webcsv)
	data = []
	for row in csvreader:
		data.append(row)
	titleoff = data [1:-1]
	data = {'time':[], 'mag':[], 'place':[]}
	for x in titleoff:
		data['time'].append(x[0])
		data['mag'].append(x[4])
		data['place'].append(x[10])
	return data
#	for x in range(len(data)):
#    	print str(data.get('time')[x]) + "   " + str(data.get('mag')[x]) 

def getLocationKeys():
	webcsv = open('geosites.csv')
	csvreader = csv.reader(webcsv)
	data = []
	for row in csvreader:
		data.append(row)
	titleoff = data [1:-1]
	data = {'key': [], 'city': [],'obv': []}
	for x in titleoff:
		data['key'].append(x[0])
		data['city'].append(x[1])
		data['obv'].append(x[2])
	return data

keys = getLocationKeys()
change = False
oldTime = getCSV().get('time')[0]
while not change:
	data = getCSV()
	time = data.get('time')[0]
	place = data.get('place')[0]

	if oldTime == time:
		print "Still good."
	else:
		city = ''
		obv = ''
		for x in range(len(keys.get('key'))):
			if place.upper() == keys.get('key')[x].upper():
				city = keys.get('city')[x]
				obv = keys.get('obv')[x]
		print "Earthquake Detected!" + " on " + time + " at " + obv + " in " + city
		change = True