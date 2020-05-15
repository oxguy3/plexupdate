#!/usr/bin/env python3
import os
import requests
import json
import appdirs
import hashlib

appname = "plexupdate"
appauthor = "Hayden Schiff"

# based on https://stackoverflow.com/a/16696317
def download_file(url, filename, checksum=None):
    sha1 = None
    if (checksum != None):
        sha1 = hashlib.sha1()

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
                if (checksum != None):
                    sha1.update(chunk)

    if checksum == None:
        return None
    else:
        return sha1.hexdigest()

def get_config():
    datadir = appdirs.user_data_dir(appname, appauthor)
    config = None
    with open(os.path.join(datadir,"config.json")) as f:
        config = json.load(f)
    return config

def get_release(token, build, distro, plexpass=True):
    params={}
    if (plexpass):
        params['channel'] = 'plexpass'
    url = "https://plex.tv/api/downloads/5.json"
    headers = {'x-plex-token': token}
    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    release = None
    for category in data.values():
        for ostype in category.values():
            for rel in ostype["releases"]:
                if rel["build"] == build and rel["distro"] == distro:
                    release = rel
                    break
            if release != None:
                break
        if release != None:
            break

    return release

config = get_config()
rel = get_release(config["token"], config["build"], config["distro"], config["enablePlexpass"])
if (rel == None):
    raise Exception("No releases could be found for build '%s' and distro '%s'" % (config["build"], config["distro"]))

url = rel["url"]
filename = url.split('/')[-1]
checksum = None
if (config["enableChecksum"] != False):
    checksum = rel["checksum"]

print("Downloading %s..." % filename)
actualsum = download_file(url, filename, checksum)
if (actualsum != checksum):
    raise Exception("Bad checksum! The download appears to be corrupted.\nExpected: %s\nActual: %s" % (checksum, actualsum))
