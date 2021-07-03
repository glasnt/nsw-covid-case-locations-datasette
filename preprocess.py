import requests
import codecs
from bs4 import BeautifulSoup as bs
from sqlite_utils import Database
import json

WEBSITE_URL = "https://data.nsw.gov.au/data/dataset/nsw-covid-19-case-locations/resource/f3a28eed-8c2a-437b-8ac1-2dab3cf760f9"
OUTPUT_DB = "data.db"
OUTPUT_META = "metadata.json"


# In this case, the JSON URL changes, but the link has a consistent CSS tag. Parse that out of the landing page. 

html = requests.get(WEBSITE_URL).content
soup = bs(html, "html.parser")
link = soup.findAll("a", {"class": "resource-url-analytics"})[0]
if link:
    data_uri = link["href"]
else:
    print(f"No data URI found on {WEBSITE_URL}")
    sys.exit(1)

# Get JSON data.
response = requests.get(data_uri)
encoded = codecs.decode(response.text.encode(), 'utf-8-sig')
data = json.loads(encoded)

# Build SQLite Database
db = Database(OUTPUT_DB, recreate=True)
monitor = data['data']['monitor']

# Convert data into a rich popup
ignore = ["Lat", "Lon", "HealthAdviceHTML", "Alert"]
for entry in monitor:
    html = [f"<p><strong>{entry['Alert']}</strong><br>{entry['HealthAdviceHTML']}</p>"]
    for k in entry.keys():
        if k not in ignore:
            html.append(f"<strong>{k}</strong>: {entry[k]}")
    entry['popup'] = {'html': "<br>".join(html)}

# Insert data (acts as save)
db['nsw'].insert_all(monitor)

# Build Metadata
metadata = {
    "databases": {
        "data": {
            "tables": {
                "nsw": {
		    "title": f"{data['title']} as at {data['date']}",
                    "source": "NSW Ministry of Health - NSW COVID-19 case locations - data.nsw.gov.au",
                    "source_url": "https://data.nsw.gov.au/data/dataset/nsw-covid-19-case-locations",
                    "plugins": {
                        "datasette-cluster-map": {
                            "latitude_column": "Lat",
                            "longitude_column": "Lon"
                        }
                    }
                }
            }
        }
    }
}

# Save metadata
with open(OUTPUT_META, "w") as f:
	json.dump(metadata, f)

# Helpful prompt if running manually.
print(f"# run:  datasette serve {OUTPUT_DB} -m {OUTPUT_META}")
