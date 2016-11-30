import hashlib
import urllib.request as urllib2
langPack = {
    "grabbingRemote": " Download       | Retrieving remote hash from {}",
    "removingCrap":   " Calculation    | Removing the rubbish that web sends",
    "readingLocal":   " IO             | Reading mod into memory from local file, {}",
    "notice":         " Client/Info    | Remote Hash: {} Local Hash: {}",
    "comparing":      " Calculation    | Calculating difference between hashes.",
    "result":         " Client/Info    | Hashes identical: {}",
    "handoverWarn":   " Client/Info    | Handing back to main.py"
}
def compare(remoteHash, localName, lang = langPack):
    print(lang["grabbingRemote"].format(remoteHash))
    data = urllib2.urlopen(remoteHash) # it's a file like object and works just like a file
    remoteHashTemp = data.read()
    data.close()
    print(lang['readingLocal'].format(localName))
    with open(localName, 'rb') as f:
        localHash = hashlib.md5(f.read()).hexdigest()
    print(lang["removingCrap"])
    remoteHash = remoteHashTemp.decode('utf-8').replace("\n", "")
    print(lang['notice'].format(remoteHash, localHash))
    print(lang['comparing'])
    identical = remoteHash == localHash
    print(lang['result'].format(identical))
    print(lang['handoverWarn'])
    return identical
    
