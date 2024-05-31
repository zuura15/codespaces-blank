import json
import datetime

# Load your JSON data from the file
with open('your_location_history.json') as f:
    data = json.load(f)

# Extract locations
locations = []
for entry in data['locations']:
    latitude = entry['latitudeE7'] / 1e7
    longitude = entry['longitudeE7'] / 1e7
    timestamp = datetime.datetime.fromtimestamp(int(entry['timestampMs']) / 1000).strftime('%Y-%m-%d %H:%M:%S')
    locations.append({
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    })

# Save as a JavaScript file
with open('locations.js', 'w') as f:
    f.write('var locations = ')
    json.dump(locations, f, indent=4)
    f.write(';')
