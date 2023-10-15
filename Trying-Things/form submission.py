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
        date_start = datetime.strptime(start_date_entry.get(), '%m/%d/%y')
        date_end = datetime.strptime(end_date_entry.get(), '%m/%d/%y')
        person = person_combo.get()
        tags = tags_combo.get()
        event_type = type_combo.get()
        description = description_entry.get("1.0", "end-1c")
        date_start_formatted = date_start.strftime('%A, %B %d, %Y')
        date_end_formatted = date_end.strftime('%A, %B %d, %Y')
        start_date_notion = convert_to_notion_datetime(date_start, start_time_entry.get_time())
        end_date_notion = convert_to_notion_datetime(date_end, end_time_entry.get_time())

        data = {
            "parent": {"database_id": "40d0c5e5d4874c3696d0b24cbfc27db3"},
            "properties": {
                "Name": {"title": [{"text": {"content": name}}]},
                "Status": {"select": {"name": status}},
                "Assigned": {"select": {"name": assigned}},
                "Date Start": {"date": {"start": date_start_formatted}},
                "Date End": {"date": {"end": date_end_formatted}},
                "Person": {"select": {"name": person}},
                "Tags": {"multi_select": [{"name": tags}]},
                "Type": {"select": {"name": event_type}},
                "Description": {"rich_text": [{"text": {"content": description}}],
                "Start Time": {"rich_text": [{"text": {"content": start_date_notion}}],
                "End Time": {"rich_text": [{"text": {"content": end_date_notion}}]
            }
        }}}}

        response = requests.post(notion_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            mg.showinfo("Success", "Data submitted successfully!")
        else:
            mg.showwarning("Error", f"Failed with status code {response.status_code}")
    except Exception as e:
        mg.showerror("Error", f"An error occurred: {e}")


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
assigned_combo = ttk.Combobox(root, values=["Mr. Ahmad", "Mr. Eko", "Mr. Rifal", "Mr. Fauzan", "Ms. Sasha", "Ms. Rina", "Pak Suryadi"])
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
