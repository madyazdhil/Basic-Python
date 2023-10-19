import requests

database_id = "c1147938-b13d-4a53-8dc5-ecd3f7120188"
token = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
url = f"https://api.notion.com/v1/databases/{database_id}/query"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-08-16",
}

data = {
    "filter": {},
    "sorts": [
        {
            "property": "priority",
            "direction": "ascending"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(f"Response status code: {response.status_code}")
print(f"Response content: {response.content}")

try:
    results = response.json()
    for item in results.get("results", []):
        title = item["properties"]["Tasks"]["title"][0]["text"]["content"]
        type_select = item["properties"]["Type"]["select"]["name"]
        assign_person = item["properties"]["Assign"]["people"]
        status_select = item["properties"]["Status"]["select"]["name"]
        created_time = item["created_time"]
        print(f"Title: {title}, Type: {type_select}, Assign: {assign_person}, Status: {status_select}, Created Time: {created_time}")
except KeyError as e:
    print(f"KeyError: {e}")
