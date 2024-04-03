import json
import requests

response = requests.get('https://api.cpicpgx.org/v1/publication?guidelineid=not.is.null&select="fulltextfile"')

response_json = json.loads(response.text)

for line in response_json:
    filename = line["fulltextfile"].split("/")[-1]
    print(f"Downloading {filename}")
    response = requests.get(line["fulltextfile"])
    with open(f"cpic_guidelines/{filename}", 'wb') as outfile:
        outfile.write(response.content)