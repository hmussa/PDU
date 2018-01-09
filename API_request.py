def Assign_on_infoblox(IP,MAC):

	import requests

	url = "https://infoblox.lint/wapi/v2.7/host"

	querystring = {"_return_fields+":"ipv4addr,mac","_return_as_object":"1"}

	payload = "{\"ipv4addr\":\"" + IP + "\", \"mac\":\"" + MAC + "\"}"
	headers = {
	    'Content-Type': "application/json",
	    'Authorization': "Basic aG11c3NhOldyeDkwU3RpIQ==",
	    'Cache-Control': "no-cache",
	    'Postman-Token': "5ca75fa3-53ca-dcba-55d5-0f6a905e2a42"
	    }


	#url = "https://infoblox.lint/wapi/v2.7/grid"   

	#headers = {
	#    'Content-Type': "application/json",
	#    'Authorization': "Basic aG11c3NhOldyeDkwU3RpIQ==",
	#    'Cache-Control': "no-cache",
	#    'Postman-Token': ""
	#    }


	response = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)

	print(response.text)
	print(Assign_on_infoblox)
	print "HOLA WORLD!"



