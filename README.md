# Grocery-Store-Application
This project is a graphical user interface (GUI) for a grocery store management system. It is built using Python and Tkinter for the GUI, and MySQL for the database. The system allows users to search for products by ID, view product details, add products to a cart, and generate a bill. The bill can then be printed or saved as an RTF file.
Brief Introduction
This project is a graphical user interface (GUI) for a grocery store management system. It is built using Python and Tkinter for the GUI, and MySQL for the database. The system allows users to search for products by ID, view product details, add products to a cart, and generate a bill. The bill can then be printed or saved as an RTF file. The system also includes an admin dashboard for adding and updating stocks, as well as viewing transaction history. The system keeps track of the available stock for each product and updates it after each transaction. The system also calculates the total cost of the products in the cart and the change due to the customer. The system also displays the current date and time on the bill. Overall, this project provides a user-friendly and efficient way to manage a grocery store.

Existing System:
 The existing system is a grocery store management system built using Python, Tkinter, and MySQL.
 The system allows Employee to search for products by ID, view product details, add products to a cart, and generate a bill.
 The bill can then be printed or saved as an RTF file. The system also includes an admin dashboard for adding and updating stocks, as well as viewing transaction history.
 The system keeps track of the available stock for each product and updates it after each transaction.
 The system also calculates the total cost of the products in the cart and the change due to the customer. The system also displays the current date and time on the bill.
Proposed System:
The proposed system is an enhanced version of the existing system, with the following proposed features:
 Implementing a login system for users to securely access their accounts and personalized features.
 Implementing a search bar for users to easily find products by name or category.
 Implementing a shopping cart system for users to save products they are interested in purchasing.
 Implementing a checkout system for users to securely enter their payment information and complete their purchase.
 Implementing a notification system for users to receive updates on sales, promotions, and other relevant information.
 Implementing a review system for users to leave feedback on products and services.  

System Analysis
This project is a Grocery Store Management System designed to manage grocery store operations such as searching for products, adding products to the cart, generating bills, and managing stock. It also includes an admin dashboard for administrative tasks like adding and updating stock.
Functional Requirements
User Management
 Admin login and authentication
 Admin dashboard with options to add and update stock Product Management
 Search for products by ID
 Display product details: name, price, and available stock
 Add products to the cart Cart Management
 Add items to the cart
 Remove items from the cart
 Calculate total price and change
 Generate bills Transaction Management
 Display last purchased items
 Record transactions in a database


Methodology Adopted
The methodologies adopted in this project are:
 Agile Development: The project follows an agile development approach, where the code is written in small increments, and each increment is tested and refined before moving on to the next one
 Object-Oriented Programming (OOP): The code uses OOP principles to define a class Application that encapsulates the GUI components and their behavior.
 Event-Driven Programming: The GUI is designed to respond to user events, such as button clicks, key presses, and mouse clicks, using event handlers.
 Database Integration: The project uses a MySQL database to store and retrieve data. The mysql-connector-python library is used to interact with the database.
 Separation of Concerns: The code separates the GUI logic from the database logic, making it easier to maintain and update the system.
 Modular Design: The code is organized into separate functions and methods, each with a specific responsibility, making it easier to understand and modify.
 Error Handling: The code includes error handling mechanisms, such as try-except blocks, to handle unexpected errors and provide user-friendly error messages.
 User-Friendly Interface: The GUI is designed to be user-friendly, with clear labels, buttons, and input fields, making it easy for users to interact with the system.
 Data Validation: The code includes data validation checks, such as checking for valid product IDs and quantities, to ensure that the system operates correctly.
 Transaction Management: The system implements transaction management, where multiple operations are grouped together as a single unit of work, ensuring data consistency and integrity.

Coding Examples
1. Application Initialization and GUI Setup
class Application:
def init (self, master):
self.master = master
# Frames
self.left = Frame(master, width=850, height=860, bg='white')
self.left.pack(side=LEFT)
self.right = Frame(master, width=680, height=860, bg='lightblue')
self.right.pack(side=RIGHT) # Components
self.heading = Label(self.left, text="Santosh Grocery Store", font=('arial 50 bold'), bg="pink")
self.heading.place(x=100, y=0)
self.enterid = Label(self.left, text="Enter Product ID", font=('arial 20 bold'), bg='white')
self.enterid.place(x=0, y=80)
self.enteride = Entry(self.left, width=20, font=("arial 20 bold"), bg="lightblue")
self.enteride.place(x=190, y=80) self.enteride.focus()
GROCERY STORE APPLICATION 50
CHETANA BCA COLLEGE
self.search_btn = Button(self.left, text="Search", width=20, height=2, bg='red', command=self.ajax)
self.search_btn.place(x=350, y=120) # Product Details
self.productname = Label(self.left, text=" ", font=('arial 25 bold'), bg='white', fg='orange')
self.productname.place(x=0, y=200)
self.ppricename = Label(self.left, text=" ", font=('arial 25 bold'), bg='white', fg='orange')
self.ppricename.place(x=0, y=240)
self.pstock = Label(self.left, text=" ", font=('arial
25 bold'), bg='white', fg='orange') self.pstock.place(x=0, y=280)
2. Handling Product Search
def ajax(self, master=None, event=None): try:
self.get_id = int(self.enteride.get()) if self.get_id < 0:
tkinter.messagebox.showerror("Error", "Please enter a valid / positive product ID")
except ValueError:
tkinter.messagebox.showerror("Error", "Please enter a valid product ID (integer only)")


 
