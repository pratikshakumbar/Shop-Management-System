import tkinter as tk

def animate_text(): 
    global i
    if i < len(welcome_text):
        canvas.itemconfig(text_id, text=welcome_text[i])
        i += 1
        canvas.after(1000, animate_text)
    else:
        start_button = tk.Button(canvas, text="Get Started!", command=open_main_window, font=("Helvetica", 24), bg="#4CAF50", fg="white", padx=20, pady=10)
        start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def open_main_window():
    # You can replace this with code to open your project's main window
    root.destroy()
    # Add your code to open the main window of your project here

root = tk.Tk()
root.title("Welcome Page Animation")
root.attributes("-fullscreen", True)  # Show window in full screen

welcome_text = [">>>>>>>> WELCOME <<<<<<<<", "TO!", "! RED CHIEF !"]
i = 0

canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
canvas.pack()

text_id = canvas.create_text(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2, text="", font=("Helvetica", 24), fill="white")

animate_text()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Dummy authentication - Replace this with your actual authentication logic
    if username == "customer" and password == "pass":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Hide login window
        root.withdraw()
        # Open new window
        open_main_window()
        # Close login window
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_main_window():
    # Create main window
    main_window = tk.Toplevel()
    main_window.title("Main Window")
    # Add widgets to the main window...
    # Example: main_window_label = tk.Label(main_window, text="Welcome to the main window")
    #          main_window_label.pack()

# Create main login window
root = tk.Tk()
root.title("Login Form")

# Set window to full screen
root.attributes('-fullscreen', True)

# Configure grid to center elements
root.grid_rowconfigure(0, weight=10)
root.grid_rowconfigure(5, weight=10)
root.grid_columnconfigure(0, weight=10)
root.grid_columnconfigure(5, weight=10)

# Create heading label
heading_label = tk.Label(root, text="Admin Login", font=("Helvetica", 32, "bold","underline"))
heading_label.grid(row=0, column=1, columnspan=2, padx=40, pady=20)

# Create username label and entry
username_label = tk.Label(root, text="Username:", font=("Helvetica", 26))
username_label.grid(row=1, column=1, padx=40, pady=10, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=2, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:", font=("Helvetica", 26))
password_label.grid(row=2, column=1, padx=40, pady=10, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=2, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login,width=15, height=2)
login_button.grid(row=3, column=1, columnspan=2, padx=40, pady=40)

root.mainloop()

# import modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

f=open("Proj_Database",'a+')

root = Tk()
root.title("Shop Managment System")
root.configure(width=1000,height=500,bg="#e3f4f1")

# Set full screen
root.attributes('-fullscreen', True)

var=-1

# function to add items
def Add_Items():
    global var
    num_lines = 0
    with open("Proj_Database", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    E1= Entry_1.get()
    E2=Entry_2.get()
    E3=Entry_3.get()
    E4=Entry_4.get()
    # E5=Entry_5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(E1),E2,E3,str(E4),E5))
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    
    messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!!!")

# function to delete items
def Delete_Items():
    E1=Entry_1.get()
    with open(r"Proj_Database") as f, open(r"Proj_Database1", "w") as working:
        for line in f:
            if str(E1) not in line:
                working.write(line)
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    
    os.remove(r"Proj_Database")
    os.rename(r"Proj_Database1", r"Proj_Database")
    messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY....!!!!!")
    f.close()
    working.close()

def list():
    global var
    var=0
    f.seek(var)
    root_1 = Tk()
    root_1.configure(bg="Gray")
    root_1.title("Stationary Store Database")
    scroll = Scrollbar(root_1)  
    scroll.pack( side = RIGHT, fill = Y)
    My_text = Text(root_1, yscrollcommand = scroll.set ,width=100,height= 50,bg= "gray",fg="black", font=("Times", 16))
    string = f.read()
    My_text.insert(END,string)
    My_text.pack( side = LEFT, fill = BOTH )
    scroll.config( command = My_text.yview )
    root.attributes('-fullscreen', True)

def Next():
    Next= messagebox.askyesno ("Next page","Do you want to move to next page(y/n)?")
    if Next > 0:
     root.destroy()
     return
    global i
    if i < len(Next):t
    canvas.itemconfig(text_id, text=Next[i])
    i += 1
    canvas.after(1000, animate_text)
    start_button = tk.Button(canvas, text="Next!", command=open_main_window, font=("Helvetica", 24), bg="#4CAF50", fg="white", padx=20, pady=10)
    start_button.place(relx=0.5, rely=0.5, anchor=tk.RIGHT)

# All labels Entrys Button grid place
Label_0= Label(root,text="****CUSTOMER DETAILS**** ",fg="black",font=("Times new roman", 30, 'bold','underline'),width=50)
Label_0.grid(columnspan=5, pady=50)  # Added pady=50 to add space at the top

Label_1=Label(root, text="CUSTOMER NAME",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=30)
Label_1.grid(row=1,column=0)
Entry_1= Entry(root, font=("Times new roman", 14),bd=25,width=40)
Entry_1.grid(row=1,column=1)

Label_2=Label(root, text="CUSTOMER CONTACT NO..",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=30)
Label_2.grid(row=2,column=0)
Entry_2= Entry(root, font=("Times new roman", 14),bd=25,width=40)
Entry_2.grid(row=2,column=1)

Label_3=Label(root,text="CUSTOMER E-MAIL ID",bg="#e8c1c7",fg="black",bd=8,font=("Times new roman", 12, 'bold'),width=30)
Label_3.grid(row=3,column=0)
Entry_3=Entry(root, font=("Times new roman", 14),bd=25,width=40)
Entry_3.grid(row=3,column=1)

Label_4=Label(root, text="CUSTOMER ADDRESS",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=30)
Label_4.grid(row=4,column=0)
Entry_4= Entry(root, font=("Times new roman", 14),bd=25,width=40)
Entry_4.grid(row=4,column=1)

Button_1= Button(root,highlightcolor="blue",activebackground="red", text="Next",bd=6, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 30),command=Next)
Button_1.place(x=835,y=537,height= 100,width=200)

root.mainloop()

import tkinter as tk
from tkinter import ttk
import sqlite3

def add_item():
    name = name_entry.get()
    price = price_entry.get()

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO items (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

    update_table()

def remove_item():
    selected_item = table.selection()[0]
    item_id = table.item(selected_item)['text']

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM items WHERE id=?', (item_id,))
    conn.commit()
    conn.close()

    update_table()

def view_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    data = c.fetchall()
    conn.close()

    # Clear the table
    for item in table.get_children():
        table.delete(item)

    # Insert new data into the table
    for row in data:
        table.insert('', 'end', text=row[0], values=(row[1], row[2]))

def clear_screen():
    for item in table.get_children():
        table.delete(item)

# def Next():
#     for item in table.get_children():
#         table.next(item)

def update_table():
    view_database()

# Create the database table if it doesn't exist
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS items
             (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
conn.commit()
conn.close()

# Create the main window
root = tk.Tk()
root.title("PRODUCT DETAILS")

# Set full screen
root.attributes('-fullscreen', True)

label = tk.Label(root, text="PRODUCT DETAILS", font=("Arial", 20, 'bold', 'underline'))
label.pack(side=tk.TOP, fill=tk.X)


# Create a table
table = ttk.Treeview(root)
table['columns'] = ('Id','Name', 'Price')

# Define column headings
table.heading('#0', text='ID')
table.column('#0', width=50)
table.heading('#1', text='Name')
table.column('#1', width=150)
table.heading('#2', text='Price')
table.column('#2', width=100)

table.pack()
# Enter the fields

name_label = tk.Label(root, text="Name:",font=("Arial", 24))
name_label.pack()
name_entry = tk.Entry(root,width=50)
name_entry.pack()

price_label = tk.Label(root, text="Price:",font=("Arial", 24))
price_label.pack()
price_entry = tk.Entry(root,width=50)
price_entry.pack()


# Buttons for adding, removing, viewing, and clearing
add_button = tk.Button(root, text="Add Item", command=add_item,width=25, height=3,bg="mint cream", fg="black")
add_button.pack()

remove_button = tk.Button(root, text="Remove Item", command=remove_item,width=25, height=3,bg="old lace", fg="black")
remove_button.pack()

view_button = tk.Button(root, text="View Database", command=view_database,width=25, height=3,bg="lightblue", fg="black")
view_button.pack()

clear_button = tk.Button(root, text="Clear Screen", command=clear_screen,width=25, height=3, bg="mint cream", fg="black")
clear_button.pack()

# Next button
next_button = tk.Button(root, text="Next", command=root.destroy, width=20, height=3,bg="lightcoral", fg="black")
next_button.pack(side=tk.RIGHT)


# Run the Tkinter event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

class BillGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Bill Generator")
        self.master.configure(bg="lightblue")  # Set background color for the window
        self.master.attributes("-fullscreen", True)  # Set full screen

        self.items = []
        self.total_cost = 0

        # Shop details
        self.shop_name = "RED CHIEF"
        self.shop_address = "Shop No-1957,Lingad Gudi Rd,Bangaramma Sajjan Campus,Vijaypura"
        self.shop_contact = "089801-56159"
        self.shop_="Thank you for shopping with us!"
        # Heading
        heading_label = tk.Label(master, text=f"  .......{self.shop_name} BILL GENERATOR SYSTEM.......  ", bg="lightblue", font=('Helvetica', 40, 'bold', 'underline'))
        heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Labels
        tk.Label(master, text="Item Name:", bg="lightblue", font=('Helvetica', 20, 'bold')).grid(row=1, column=0, padx=10, pady=10)
        tk.Label(master, text="Price:", bg="lightblue", font=('Helvetica', 20, 'bold')).grid(row=2, column=0, padx=10, pady=10)
        tk.Label(master, text="Quantity:", bg="lightblue", font=('Helvetica', 20, 'bold')).grid(row=3, column=0, padx=10, pady=10)

        # Entry fields
        self.item_name_entry = tk.Entry(master, font=('Helvetica', 20))
        self.item_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.price_entry = tk.Entry(master, font=('Helvetica', 20))
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)
        self.quantity_entry = tk.Entry(master, font=('Helvetica', 20))
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(master, text="Generate Bill", command=self.add_item, bg="green", fg="white", font=('Helvetica', 15, 'bold')).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(master, text="Print Bill", command=self.generate_bill, bg="blue", fg="white", font=('Helvetica', 15, 'bold')).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(master, text="Next", command=self.close_app, bg="red", fg="white", font=('Helvetica', 15, 'bold')).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Display area for bill
        self.bill_display = tk.Text(master, height=10, width=70, bg="white", font=('Helvetica', 15))
        self.bill_display.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add_item(self):
        try:
            item_name = self.item_name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            self.items.append((item_name, price, quantity))
            messagebox.showinfo("Bill Generated Successfully", f"{quantity} {item_name}(s) added to the bill.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price and quantity.")


    def generate_bill(self):
        self.bill_display.delete(1.0, tk.END)
        self.total_cost = 0

        self.bill_display.insert(tk.END, f"Shop Name: {self.shop_name}\n")
        self.bill_display.insert(tk.END, f"Shop Address: {self.shop_address}\n")
        self.bill_display.insert(tk.END, f"Shop Contact: {self.shop_contact}\n\n")
        self.bill_display.insert(tk.END, f" {self.shop_}\n\n.")
        self.bill_display.insert(tk.END, "Bill:\n\n")
        for item in self.items:
            item_name, price, quantity = item
            total_item_cost = price * quantity
            self.bill_display.insert(tk.END, f"{item_name}: ₹{price} x {quantity} = ₹{total_item_cost}\n")
            self.total_cost += total_item_cost

        self.bill_display.insert(tk.END, f"\nTotal Cost: ₹{self.total_cost}\n")
        self.items = []  # Reset items list

    def close_app(self):
        self.master.destroy()

root=tk.Tk()
app = BillGenerator(root)
root.mainloop()


import tkinter as tk

def animate_text():
    global i
    if i < len(thankyou_text):
        canvas.itemconfig(text_id, text=thankyou_text[i])
        i += 1
        canvas.after(1000, animate_text)
    else:
        start_button = tk.Button(canvas, text="Close", command=open_main_window, font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=20, pady=10)
        start_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

def open_main_window():
    # You can replace this with code to open your project's main window
    root.destroy()
    
# Add your code to open the main window of your project here

root = tk.Tk()
root.title("Thank you Page Animation")
root.attributes("-fullscreen", True)  # Show window in full screen

thankyou_text = ["THANK YOU ☺!"]
i = 0

canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
canvas.pack()

text_id = canvas.create_text(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2, text="", font=("Helvetica", 54), fill="white")

animate_text()

root.mainloop()
    