import json

# Read the station data from the file "list_of_stations.md"
with open("./list_of_stations.md", "r") as file:
    station_data = file.read()

# Split the data into individual lines
station_lines = station_data.strip().split("\n")

# Create an empty list to store station dictionaries
stations = []

# Process each line and extract the station details
for line in station_lines:
    # Split the line into station code, station name, and region code
    parts = line.split(" (")
    
    # Extract station code and station name
    station_code_name = parts[0].strip()
    region_code = parts[1].replace(")", "").strip()
    
    print(station_code_name)
    # Further split the station code and station name
    code, name = station_code_name.split("-", 1)
    
    # Create a dictionary for the station
    station_dict = {
        "station_code": code.strip(),
        "station_name": name.strip(),
        "region_code": region_code.strip()
    }
    
    # Append the station dictionary to the list
    stations.append(station_dict)

# Write the resulting list of stations into a JSON file "json_list_of_stations.md"
with open("list_of_stations.json", "w") as json_file:
    json.dump(stations, json_file, indent=4)

print("Data has been successfully written to json_list_of_stations.md")

