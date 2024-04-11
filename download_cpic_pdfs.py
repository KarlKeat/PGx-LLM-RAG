import json
import requests
import os

response = requests.get('https://api.cpicpgx.org/v1/publication?guidelineid=not.is.null&select="fulltextfile"')

response_json = json.loads(response.text)

os.makedirs("cpic_guidelines", exist_ok=True)

for line in response_json:
    filename = line["fulltextfile"].split("/")[-1]
    print(f"Downloading {filename}")
    response = requests.get(line["fulltextfile"])
    with open(f"cpic_guidelines/{filename}", 'wb') as outfile:
        outfile.write(response.content)