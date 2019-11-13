import http.client, urllib.request, urllib.parse, urllib.error, base64, json
def station_info():
	headers = {
    # Request headers
    'api_key': 'e93ecdd1d06b42b2a4e8dcd58d1b066d',
	}

	params = urllib.parse.urlencode({
     #Request parameters
    #'lineCode': '{string}',
	})

	try:
		conn = http.client.HTTPSConnection('api.wmata.com')
		conn.request("GET", "/Rail.svc/json/jStations?%s" % params, "{body}", headers)
		response = conn.getresponse()
		data = response.read()
		#print(data)
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))  

	data = json.loads(data) 
	return data

def travel_info(origin,destination):

	headers = {
    # Request headers
    'api_key': 'e93ecdd1d06b42b2a4e8dcd58d1b066d',
	}

	params = urllib.parse.urlencode({
    # Request parameters
    'FromStationCode': origin,
    'ToStationCode': destination,
	})

	try:
		conn = http.client.HTTPSConnection('api.wmata.com')
		conn.request("GET", "/Rail.svc/json/jSrcStationToDstStationInfo?%s" % params, "{body}", headers)
		response = conn.getresponse()
		data = response.read()
		#print(data)
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror)) 
	data = json.loads(data)
	return data 

def money(value):
	return "{:.2f}".format(value) 

station_dict = dict((station["Code"],station["Name"]) for station in station_info()['Stations'])