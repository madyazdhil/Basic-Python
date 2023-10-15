import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests
import json
from datetime import datetime

# Notion setup
notion_api_key = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
notion_url = "https://api.notion.com/v1/pages"

headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

# Function to convert date and time to Notion datetime format
def convert_to_notion_datetime(date, time):
    date_formatted = date.strftime('%Y-%m-%d')
    time_formatted = time.strftime('%H:%M:%SZ')
    return f"{date_formatted}T{time_formatted}"

# Function to handle form submission
def submit_data():
    name = name_entry.get()
    status = status_combo.get()
    assigned = assigned_combo.get()
    date_start = start_date_entry.get()
    date_end = end_date_entry.get()
    person = person_combo.get()
    tags = tags_combo.get()
    event_type = type_combo.get()
    description = description_entry.get("1.0", "end-1c")
    date_start_formatted = datetime.strptime(date_start, '%Y-%m-%d').strftime('%A, %B %d, %Y')
    date_end_formatted = datetime.strptime(date_end, '%Y-%m-%d').strftime('%A, %B %d, %Y')
    start_date_notion = convert_to_notion_datetime(start_datetime_entry.get_date(), start_time_entry.get_date())
    end_date_notion = convert_to_notion_datetime(end_datetime_entry.get_date(), end_time_entry.get_date())

    data = {
        "parent": {"database_id": "40d0c5e5d4874c3696d0b24cbfc27db3"},
        "properties": {
            "Name": {"title": [{"text": {"content": name}}]},
            "Status": {"select": {"name": status}},
            "Assigned": {"select": {"name": assigned}},
            "Date Start": {"date": {"start": date_start_formatted}},
            "Date End": {"date": {"start": date_end_formatted}},
            "Person": {"select": {"name": person}},
            "Tags": {"multi_select": [{"name": tags}]},
            "Type": {"select": {"name": event_type}},
            "Description": {"rich_text": [{"text": {"content": description}}],
            "Date Start": {"date": {"start": start_date_notion}},
            "Date End": {"date": {"start": end_date_notion}}
        }
    }}

    response = requests.post(notion_url, headers=headers, data=json.dumps(data))
    print(response.status_code)  # Check the status code for successful submission

# Create a Tkinter window
root = tk.Tk()
root.geometry("400x500")
root.title("Data Entry Form")

# Entry fields
tk.Label(root, text="Name of the Event:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Status:").pack()
status_combo = ttk.Combobox(root, values=["To-Do", "In Progress", "Done", "Archive"])
status_combo.pack()

tk.Label(root, text="Assigned:").pack()
assigned_combo = ttk.Combobox(root, values=["Mr. Ahmad", "Mr. Eko", "Mr. Rifal", "Mr. Fauzan", "Ms. Sasha", "Ms. Rina", "Pak Suryadi"])
assigned_combo.pack()

# Date picker for start date
tk.Label(root, text="Start Date:").pack()
start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date_entry.pack(padx=10, pady=5)

# Start time picker
tk.Label(root, text="Start Time:").pack()
start_time_combo = ttk.Combobox(root, values=["10.30", "13.30", "15.15", "17.00"])
start_time_combo.pack(padx=10, pady=5)

# Date picker for end date
tk.Label(root, text="End Date:").pack()
end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date_entry.pack(padx=10, pady=5)

# End time picker
tk.Label(root, text="End Time:").pack()
end_time_combo = ttk.Combobox(root, values=["12.00", "15.00", "16.45", "18.30"])
end_time_combo.pack(padx=10, pady=5)

tk.Label(root, text="Person:").pack()
person_combo = ttk.Combobox(root, values=["Mr. Ahmad", "Mr. Eko", "Mr. Rifal", "Mr. Fauzan", "Ms. Sasha", "Ms. Rina", "Pak Suryadi"])
person_combo.pack()

tk.Label(root, text="Tags:").pack()
tags_combo = ttk.Combobox(root, values=["Koding Next", "ESDA", "PERSONAL"])
tags_combo.pack()

tk.Label(root, text="Type:").pack()
type_combo = ttk.Combobox(root, values=["To-do", "Trial KN", "Catch-up KN", "Agenda"])
type_combo.pack()

tk.Label(root, text="Description:").pack()
description_entry = tk.Text(root, height=5, width=30)
description_entry.pack()

# Button to submit data
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.pack(pady=10)

# Start the main loop
root.mainloop()


# Notion setup
notion_api_key = "secret_dE4BUTXi4GQWLAus2k92XeaPH9fEzcPvuqJfC3NpFd7"
notion_url = "https://api.notion.com/v1/pages"

headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

# Function to handle form submission
def submit_data():
    name = name_entry.get()
    status = status_combo.get()
    assigned = assigned_combo.get()
    date_start = start_datetime_entry.get_date().strftime('%Y-%m-%d')
    date_end = end_datetime_entry.get_date().strftime('%Y-%m-%d')
    person = person_combo.get()
    tags = tags_combo.get()
    event_type = type_combo.get()
    description = description_entry.get("1.0", "end-1c")

    data = {
        "parent": {"database_id": "40d0c5e5d4874c3696d0b24cbfc27db3"},
        "properties": {
            "Name": {"title": [{"text": {"content": name}}]},
            "Status": {"select": {"name": status}},
            "Assigned": {"select": {"name": assigned}},
            "Date Start": {"date": {"start": date_start}},
            "Date End": {"date": {"start": date_end}},
            "Person": {"select": {"name": person}},
            "Tags": {"multi_select": [{"name": tags}]},
            "Type": {"select": {"name": event_type}},
            "Description": {"rich_text": [{"text": {"content": description}}]}
        }
    }

    response = requests.post(notion_url, headers=headers, data=json.dumps(data))
    print(response.status_code)  # Check the status code for successful submission

# Create a Tkinter window
root = tk.Tk()
root.geometry("400x500")
root.title("Data Entry Form")

# Entry fields
tk.Label(root, text="Name of the Event:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Status:").pack()
status_combo = ttk.Combobox(root, values=["To-Do", "In Progress", "Done", "Archive"])
status_combo.pack()

tk.Label(root, text="Assigned:").pack()
assigned_combo = ttk.Combobox(root, values=["Mr. Ahmad", "Mr. Eko", "Mr. Rifal", "Mr. Fauzan", "Ms. Sasha", "Ms. Rina", "Pak Suryadi"])
assigned_combo.pack()

# Date and time picker for start date
tk.Label(root, text="Start Date:").pack()
start_datetime_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_datetime_entry.pack(padx=10, pady=5)

start_time_entry = TimeEntry(root)
start_time_entry.pack(padx=10, pady=5)

# Date and time picker for end date
tk.Label(root, text="End Date:").pack()
end_datetime_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_datetime_entry.pack(padx=10, pady=5)

end_time_entry = TimeEntry(root)
end_time_entry.pack(padx=10, pady=5)

tk.Label(root, text="Person:").pack()
person_combo = ttk.Combobox(root, values=["Mr. Ahmad", "Mr. Eko", "Mr. Rifal", "Mr. Fauzan", "Ms. Sasha", "Ms. Rina", "Pak Suryadi"])
person_combo.pack()

tk.Label(root, text="Tags:").pack()
tags_combo = ttk.Combobox(root, values=["Koding Next", "ESDA", "PERSONAL"])
tags_combo.pack()

tk.Label(root, text="Type:").pack()
type_combo = ttk.Combobox(root, values=["To-do", "Trial KN", "Catch-up KN", "Agenda"])
type_combo.pack()

tk.Label(root, text="Description:").pack()
description_entry = tk.Text(root, height=5, width=30)
description_entry.pack()

# Button to submit data
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.pack(pady=10)

# Start the main loop
root.mainloop()
