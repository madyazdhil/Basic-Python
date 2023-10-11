import tkinter as tk
from tkinter import messagebox

def generate_invoice():
    customer_name = nameI.get().strip()
    if not customer_name:
        messagebox.showerror("Error", "Please enter the customer's name.")
        return

    total_amount = 0
    ordered_items = []

    for item, (name, price, check_var, spinbox_var) in menu_choices.items():
        quantity = spinbox_var.get()  # Get the selected quantity from the Spinbox
        if check_var.get() and quantity > 0:  # Check if the item is checked and quantity is greater than 0
            item_total = price * quantity
            total_amount += item_total
            ordered_items.append(f"{name} - Quantity: {quantity} - Total: ${item_total:.2f}")

    if not ordered_items:
        messagebox.showerror("Error", "Please select at least one item.")
        return

    invoice_text = f"Customer Name: {customer_name}\n\nOrdered Items:\n"
    invoice_text += "\n".join(ordered_items)
    invoice_text += f"\n\nTotal Amount: ${total_amount:.2f}"

    show_invoice(customer_name, invoice_text)

def show_invoice(customer_name, invoice_text):
    invoice_window = tk.Toplevel(main_window)
    invoice_window.title(f"Invoice for {customer_name}")

    invoice_label = tk.Label(invoice_window, text=invoice_text, font=("Helvetica", 12))
    invoice_label.pack(padx=10, pady=10)

main_window = tk.Tk()
main_window.geometry("600x870")
main_window.title("Restaurant France")

menu_items = {
    "Main Course": {
        "Pizza": 12.50,
        "Pasta": 10.00,
        "Lasagna": 13.00,
        # Add more main course items here
    },
    "Dessert": {
        "Tiramisu": 6.00,
        "Cannoli": 5.50,
        "Gelato": 4.00,
        # Add more dessert items here
    },
    "Wine": {
        "Chianti": 25.00,
        "Pinot Grigio": 22.50,
        "Barolo": 30.00,
        # Add more wine items here
    }
}

menu_choices = {}
spinbox_vars = {}  # Dictionary to store Spinbox variables for each item

welcome = tk.Label(main_window, text="Welcome to Restaurant France", font=("Gill Sans", 25))
nameL = tk.Label(main_window, text="Customer's name: ")
nameI = tk.Entry(main_window, width=24, justify="center")

welcome.grid(row=0, column=0, columnspan=2, pady=25)
nameL.grid(row=1, column=0, padx=5, pady=15)
nameI.grid(row=1, column=1, padx=5, pady=15)

frame_menu = tk.Frame(main_window)
frame_menu.grid(row=2, column=0, columnspan=2, pady=15)

row_counter = 0
for course, items in menu_items.items():
    tk.Label(frame_menu, text=course, font=("Helvetica", 14, "bold")).grid(row=row_counter, column=0, columnspan=2)
    row_counter += 1
    for idx, (item, price) in enumerate(items.items()):
        item_check_var = tk.IntVar()  # Create a separate IntVar for the Checkbutton
        tk.Checkbutton(frame_menu, text=f"{item} - ${price:.2f}", variable=item_check_var).grid(row=row_counter,
                                                                                                column=0, sticky="w")

        item_spinbox_var = tk.IntVar()  # Create a separate IntVar for the Spinbox
        spinbox = tk.Spinbox(frame_menu, from_=0, to=10, width=2,
                             textvariable=item_spinbox_var)  # Use the IntVar for the Spinbox
        spinbox.grid(row=row_counter, column=1, padx=5, sticky="e")
        spinbox_vars[item] = spinbox  # Store the Spinbox variable in the dictionary

        menu_choices[item] = (item, price, item_check_var, item_spinbox_var)  # Store all variables in the dictionary
        row_counter += 1

button_invoice = tk.Button(main_window, text="Generate Invoice", command=generate_invoice)
button_invoice.grid(row=3, column=0, columnspan=2, pady=15)

main_window.mainloop()
1