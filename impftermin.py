# Written for MacOs. Adaptations needed for other systems. 
# This script depends on the terminal-notifier library e.g. using homebrew via $ brew install terminal-notifier
# Alternatively you can comment out lines 7 and 30 and use the webbrowser, but this will open quite a few tabs as soon as there are any availilibilities

import requests
import json
# import webbrowser
import os
import time

def check_availability():
    url = 'https://api.impfstoff.link/?v=0.3&robot=1'

    r = requests.get(url)

    result = json.loads(r.text)
    any_free = False

    impfzentren = {
        "arena": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158431",
        "tempelhof": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158433",
        "messe": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158434",
        "velodrom": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158435",
        "tegel": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158436",
        "erika": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158437"
    }

    for stat in result["stats"]:
        if(stat["open"] == True):
            # webbrowser.open(impfzentren[stat["id"]])
            os.system("terminal-notifier -title '💉 Impftermin 💉' -message 'Jetzt zu Impftermin Zentrum: " + stat["id"] + "' -open '" +
                      impfzentren[stat["id"]] + "'")
            any_free = True

            # add -sound 'default' option to terminal-notifier if you want a notification sound

    if any_free == False:
        print("No availability. Checking again in 5 seconds.")
        time.sleep(5)
    if any_free:
        print("Found availability. Checking again in 30 seconds.")
        time.sleep(30)
    check_availability()


check_availability()
