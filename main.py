import json
from pprint import pprint

# Simple example of nestled JSON generation

raw_data = [
    dict(
        id="SE0441273000000001",
        en='bathing place näsholm',
        sv='badplats näsholm',
    ),
    dict(
        id="SE0441273000000002",
        en='bathing place kastholm',
        sv='badplats kastholm',
    )
]

# detta är vår dictionary som håller all data som ska skrivas till disk
data = {}
public_baths = []
languages = ["en", "sv"]
for bath in raw_data:
    entry = {}  # dictionary
    entry["Eionet bathingWaterIdentifier"] = bath["id"]
    names = {}  # list
    for language in languages:
        if language in bath.keys():
            names[language] = {'language': language,
                               'value': bath[language]}
    entry["name"] = names
    public_baths.append(entry)
data["public_baths"] = public_baths
pprint(data)
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(data))