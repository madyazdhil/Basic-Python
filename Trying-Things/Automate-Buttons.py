import webbrowser
import tkinter as tk

# Define the links for each lesson
lessons = {
    1: ['http://www.lesson1link1.com', 'http://www.lesson1link2.com', 'http://www.lesson1link3.com'],
    2: ['http://www.lesson2link1.com', 'http://www.lesson2link2.com', 'http://www.lesson2link3.com'],
    # Add links for other lessons similarly
    # ...
}

def open_links(links):
    for link in links:
        webbrowser.open_new_tab(link)

def create_button(root, lesson_num, links):
    def callback():
        open_links(links)

    button = tk.Button(root, text=f"Lesson {lesson_num}", command=callback)
    button.pack(padx=10, pady=5)

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Lesson Automation App")

# Create buttons for each lesson
for i in range(1, 21):
    if i in lessons:
        create_button(root, i, lessons[i])

# Start the main loop
root.mainloop()
