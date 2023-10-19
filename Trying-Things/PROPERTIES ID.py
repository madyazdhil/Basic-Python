import requests

notion_api_key = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
database_id = "c1147938b13d4a538dc5ecd3f7120188"
headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

url = f"https://api.notion.com/v1/databases/{database_id}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    properties = data["properties"]
    for prop in properties:
        prop_id = properties[prop]['id']
        prop_name = prop
        prop_value = properties[prop]

        print(f"Property Name: {prop_name}")
        print(f"Property ID: {prop_id}")
        print(f"Property Value: {prop_value}")
        print("---------------------------")
else:
    print(f"Failed with status code {response.status_code}")
