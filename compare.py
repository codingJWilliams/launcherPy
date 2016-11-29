import hashlib
import urllib.request as urllib2
def compare(remoteHash, localName):
    data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
    remoteHash = data.read()
    data.close()
    with open(localName, 'rb') as f: localHash = hashlib.md5(f.read()).hexdigest()
    print(remoteHash + "\n" + localHash   
