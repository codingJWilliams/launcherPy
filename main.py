# Import neccesary libraries

import compare, json
import urllib.request as urllib2

# Prefs

baseUrl = "http://cdn.damnapi.me/beta"
baseModFolder = "C:\\Users\\jaywi\\Desktop\\launcherTest"

# Load packages.json into memory

temp = urllib2.urlopen("{}/packages.json".format(baseUrl)) # it's a file like object and works just like a file
packages = json.loads(temp.read().decode('utf-8').replace("\n", ""))
temp.close()
del temp

# Logic
for mod in packages['mods']:
    ident = compare.compare("{}".format(mod['hash']).format(baseUrl), baseModFolder + "\\" + mod['filename'])
    if ident == True:
        pass
    else:
        print("Doesnt match")
