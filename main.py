import json
from datetime import datetime

# Helper function to convert ISO 8601 string to milliseconds since epoch
def iso_to_millis(iso_str):
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# IMPLEMENT: Transform data-1.json to the unified format
def transform_data_1(data):
    result = []
    for item in data:
        transformed = {
            "timestamp": iso_to_millis(item["time"]),
            "temperature": item["temp"],
            "humidity": item["hum"]
        }
        result.append(transformed)
    return result


# IMPLEMENT: Transform data-2.json to the unified format
def transform_data_2(data):
    result = []
    for item in data:
        transformed = {
            "timestamp": item["timestamp"],
            "temperature": item["temperature"],
            "humidity": item["humidity"]
        }
        result.append(transformed)
    return result


# Load both input files
with open("data-1.json") as f1, open("data-2.json") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Transform both datasets
transformed_data = transform_data_1(data1) + transform_data_2(data2)

# Sort by timestamp to match result format (if required)
transformed_data.sort(key=lambda x: x["timestamp"])

# Save to result file
with open("my-result.json", "w") as result_file:
    json.dump(transformed_data, result_file, indent=2)
