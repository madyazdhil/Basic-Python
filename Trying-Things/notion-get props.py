import os
from notion.client import NotionClient

# Your Notion API secret
notion_token = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
# Your database ID
database_id = "c1147938b13d4a538dc5ecd3f7120188"

# Connect to Notion client
client = NotionClient(token_v2=notion_token)
database = client.get_collection_view(database_id)

# Fetching the schema to get all the properties
properties = database.collection.get_schema_properties()

# Printing the properties that need to be filled
print("Properties that need to be filled:")
for prop, value in properties.items():
    if value['type'] != 'formula' and value['type'] != 'rollup':
        print(f"{prop} - {value['type']}")

# Fetching all the data from the database
rows = database.collection.get_rows()

# Printing values for select properties
select_properties = [prop for prop, value in properties.items() if value['type'] == 'select']
print("\nValues for select properties:")
for row in rows:
    for prop in select_properties:
        print(f"{prop}: {row.get_property(prop)}")
