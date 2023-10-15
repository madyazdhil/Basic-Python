import requests
import json

# Notion setup
notion_api_key = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
notion_url = "https://api.notion.com/v1/pages"
headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

# Prepare data
data = {
    "parent": {
        "database_id": "c1147938b13d4a538dc5ecd3f7120188"
    },
    "properties": {
        "title": {
            "title": [
                {
                    "text": {
                        "content": "Test Title"
                    }
                }
            ]
        }
    }
}

# Make the request
response = requests.post(notion_url, headers=headers, data=json.dumps(data))

# Check response
if response.status_code == 200:
    print("Data submitted successfully!")
    print(response.json())
else:
    print(f"Failed with status code {response.status_code}")
    print(response.text)
