import requests

notion_api_key = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
database_id = "c1147938b13d4a538dc5ecd3f7120188"
url = f"https://api.notion.com/v1/databases/{database_id}"

headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

response = requests.get(url, headers=headers)
data = response.json()

properties = data["properties"]

for key, value in properties.items():
    print(f"Property Name: {key}")
    print(f"Property Type: {value['type']}")
    print("---------------")
