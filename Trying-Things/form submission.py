import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mg
import requests
import json
from datetime import datetime
from tkcalendar import DateEntry

# Notion setup
notion_api_key = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
notion_url = "https://api.notion.com/v1/pages"
notion_database_id = "c1147938b13d4a538dc5ecd3f7120188"  # Replace with your Notion database ID

headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

class TimeEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.hour_values = [f"{str(i).zfill(2)}" for i in range(24)]
        self.minute_values = [f"{str(i).zfill(2)}" for i in range(60)]

        self.hour_label = tk.Label(self, text="Hour:")
        self.hour_label.pack(side=tk.LEFT)

        self.hour_combo = ttk.Combobox(self, values=self.hour_values, width=3)
        self.hour_combo.pack(side=tk.LEFT)

        self.minute_label = tk.Label(self, text="Minute:")
        self.minute_label.pack(side=tk.LEFT)

        self.minute_combo = ttk.Combobox(self, values=self.minute_values, width=3)
        self.minute_combo.pack(side=tk.LEFT)

    def get_time(self):
        selected_hour = self.hour_combo.get()
        selected_minute = self.minute_combo.get()
        return f"{selected_hour.zfill(2)}:{selected_minute.zfill(2)}:00"


# Function to convert date and time to Notion datetime format
def convert_to_notion_datetime(date, time):
    date_formatted = date.strftime('%Y-%m-%d')
    time_parsed = datetime.strptime(time, '%H:%M:%S')
    time_formatted = time_parsed.strftime('%H:%M:%SZ')
    return f"{date_formatted}T{time_formatted}"


# Function to handle form submission
def submit_data():
    try:
        name = name_entry.get()
        status = status_combo.get()
        assigned = assigned_combo.get()
        person = person_combo.get()
        description = description_entry.get("1.0", "end-1c")
        date_start = start_date_entry.get_date()
        date_end = end_date_entry.get_date()
        tags = tags_combo.get()
        event_type = type_combo.get()
        start_time = start_time_entry.get_time()
        end_time = end_time_entry.get_time()

        start_date_notion = convert_to_notion_datetime(date_start, start_time)
        end_date_notion = convert_to_notion_datetime(date_end, end_time)

        data = {
            "parent": {"database_id": notion_database_id},
            "properties": {
                "Tasks": {"title": [{"text": {"content": name}}]},
                "Status": {"select": {"name": status}},
                "Assign": {"people": [{"name": assigned}]},
                "Person": {"people": [{"name": person}]},
                "Description": {"rich_text": [{"text": {"content": description}}]},
                "Date Start": {"date": {"start": start_date_notion}},
                "Date End": {"date": {"start": start_date_notion, "end": end_date_notion}},
                "Tags": {"multi_select": [{"name": tags}]},
                "Type": {"select": {"name": event_type}}
            }
        }

        response = requests.post(notion_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            mg.showinfo("Success", "Data submitted successfully!")
        else:
            mg.showwarning("Error", f"Failed with status code {response.status_code}")
            print(response.text)  # Print response for debugging
    except Exception as e:
        mg.showerror("Error", f"An error occurred: {e}")


# Update the COMBOBOX values dynamically from the Notion database
# Update the COMBOBOX values dynamically from the Notion database
def update_combobox_values(combo, property_name):
    try:
        response = requests.get(f"https://api.notion.com/v1/databases/{notion_database_id}",
                                headers=headers)
        if response.status_code == 200:
            data = response.json()
            options = []
            for option in data['properties'][property_name]['select']['options']:
                options.append(option['name'])
            combo['values'] = options
        else:
            mg.showwarning("Error", f"Failed with status code {response.status_code}")
            print(response.text)  # Print response for debugging
    except Exception as e:
        mg.showerror("Error", f"An error occurred: {e}")
        print(e)
        print(response.text)


# Create a Tkinter window
root = tk.Tk()
root.geometry("400x600")
root.title("Data Entry Form")

# Entry fields
tk.Label(root, text="Name of the Event:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Status:").pack()
status_combo = ttk.Combobox(root, values=["To-Do", "In Progress", "Done", "Archive"])
status_combo.pack()

tk.Label(root, text="Assigned:").pack()
assigned_combo = ttk.Combobox(root, values=[])  # Empty for now
assigned_combo.pack()

# Date picker for start date
tk.Label(root, text="Start Date:").pack()
start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date_entry.pack(padx=10, pady=5)

# Create start_time_entry
tk.Label(root, text="Start Time:").pack()
start_time_entry = TimeEntry(root)
start_time_entry.pack(padx=10, pady=5)

# Date picker for end date
tk.Label(root, text="End Date:").pack()
end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date_entry.pack(padx=10, pady=5)

# Create end_time_entry
tk.Label(root, text="End Time:").pack()
end_time_entry = TimeEntry(root)
end_time_entry.pack(padx=10, pady=5)

tk.Label(root, text="Person:").pack()
person_combo = ttk.Combobox(root, values=[])  # Empty for now
person_combo.pack()

tk.Label(root, text="Tags:").pack()
tags_combo = ttk.Combobox(root, values=[])  # Empty for now
tags_combo.pack()

tk.Label(root, text="Type:").pack()
type_combo = ttk.Combobox(root, values=[])  # Empty for now
type_combo.pack()

tk.Label(root, text="Description:").pack()
description_entry = tk.Text(root, height=5, width=30)
description_entry.pack()

# Button to submit data
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.pack(pady=10)

# Use the function to update combo boxes
update_combobox_values(assigned_combo, 'Assign')
update_combobox_values(person_combo, 'Person')
update_combobox_values(tags_combo, 'Tags')
update_combobox_values(type_combo, 'Type')

# Start the main loop
root.mainloop()
