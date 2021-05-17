# This script depends on the terminal-notifier library e.g. using homebrew via $ brew install terminal-notifier
# Alternatively you can comment out lines 6 and 36 and use the webbrowser, but this will open quite a few tabs as soon as there are any availilibilities

import requests
import json
# import webbrowser
import os
import time


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def checkAvailability():
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

            # ass -sound 'default' option if you want a notification sound

    if any_free == False:
        print("No availability. Checking again in 5 seconds.")
        time.sleep(5)
    if any_free:
        print("Found availability. Checking again in 30 seconds.")
        time.sleep(30)
    checkAvailability()


checkAvailability()
