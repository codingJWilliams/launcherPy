import compare, json

# Prefs

baseUrl = "http://cdn.damnapi.me/beta"

# Load packages.json into memory

temp = urllib2.urlopen("{}/packages.json".format(baseUrl)) # it's a file like object and works just like a file
packages = json.loads(temp.read().decode('utf-8').replace("\n", ""))
temp.close()
del temp

