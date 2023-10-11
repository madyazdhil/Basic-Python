import tkinter as tk
from tkinter import messagebox

# Sample data for the menu with random prices
menu_items = {
    'Drinks': {
        'Water': 1.50,
        'Soda': 2.00,
        'Tea': 2.50,
        'Coffee': 2.00,
    },
    'Main Course': {
        'Pizza': 10.00,
        'Pasta': 12.00,
        'Lasagna': 15.00,
        'Ravioli': 14.50,
    },
    'Dessert': {
        'Tiramisu': 7.50,
        'Cheesecake': 6.50,
        'Gelato': 5.00,
        'Cannoli': 4.50,
    }
}

def calculate_total():
    total = 0
    for item, qty in selected_items_qty.items():
        if item in selected_items:
            total += selected_items[item] * qty
    messagebox.showinfo("Total Bill", f"Total: ${total:.2f}")

def show_invoice():
    invoice = "Invoice:\n"
    for item, qty in selected_items_qty.items():
        if item in selected_items:
            invoice += f"{item} x{qty}\n"
    if not invoice.endswith('\n'):
        invoice += "\n"
    messagebox.showinfo("Invoice", invoice)

def submit_order():
    global selected_items
    selected_items.clear()
    for category, items in menu_items.items():
        for item, var in menu_vars[category].items():
            if var.get():
                selected_items[item] = items[item]

    selected_items_qty.clear()
    for item, qty in selected_items_qty_tmp.items():
        if item in selected_items:
            selected_items_qty[item] = qty

    if not selected_items:
        messagebox.showwarning("Error", "Please select at least one item.")
        return

    calculate_total()
    show_invoice()

def main():
    global selected_items
    selected_items = {}
    global menu_vars
    menu_vars = {}
    global selected_items_qty
    selected_items_qty = {}

    root = tk.Tk()
    root.title("Restaurant Order")


    # Customer Name Entry
    name_label = tk.Label(root, text="Enter Customer Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    # Customer Table Selection using Radio Buttons
    table_label = tk.Label(root, text="Select Customer Table:")
    table_label.pack()
    table_var = tk.StringVar()
    table_var.set("Table 1")
    for table in ["Table 1", "Table 2", "Table 3"]:
        table_radio = tk.Radiobutton(root, text=table, variable=table_var, value=table)
        table_radio.pack()

    # Restaurant Menu with Checkboxes
    menu_frame = tk.Frame(root)
    menu_frame.pack()

    menu_vars = {}
    for category, items in menu_items.items():
        category_label = tk.Label(menu_frame, text=category)
        category_label.pack()
        category_vars = {}
        for item, price in items.items():
            var = tk.IntVar()
            category_vars[item] = var
            checkbox = tk.Checkbutton(menu_frame, text=f"{item} (${price:.2f})", variable=var)
            checkbox.pack()
        menu_vars[category] = category_vars

    # Order Quantity Entry
    qty_label = tk.Label(root, text="Enter Quantity:")
    qty_label.pack()
    qty_entry = tk.Entry(root)
    qty_entry.pack()

    def add_to_order():
        qty = int(qty_entry.get())
        selected_item = menu_listbox.get(tk.ACTIVE)
        selected_items_qty_tmp[selected_item.lower()] = qty  # Convert to lowercase
        order_listbox.insert(tk.END, f"{selected_item} x{qty}")

    # Order List and Add to Order Button
    selected_items_qty = {}
    order_frame = tk.Frame(root)
    order_frame.pack()

    menu_listbox = tk.Listbox(order_frame, selectmode=tk.SINGLE)
    menu_listbox.pack(side=tk.LEFT)

    order_listbox = tk.Listbox(order_frame)
    order_listbox.pack(side=tk.LEFT)

    add_button = tk.Button(order_frame, text="Add to Order", command=add_to_order)
    add_button.pack(side=tk.LEFT)

    # Submit Order Button
    submit_button = tk.Button(root, text="Submit Order", command=submit_order)
    submit_button.pack()

    root.mainloop()


if __name__ == "__main__":
    global selected_items_qty_tmp
    selected_items_qty_tmp = {}
    main()