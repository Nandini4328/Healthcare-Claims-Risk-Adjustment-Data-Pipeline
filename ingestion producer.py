import json
import time

def publish_events(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for record in data:
        print(f"Publishing event: {record}")
        time.sleep(1)  # simulate streaming

if __name__ == "__main__":
    publish_events("../data/sample_claims.json")
