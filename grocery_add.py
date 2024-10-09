from tkinter import *
import mysql.connector
import tkinter.messagebox
db = mysql.connector.connect(host="localhost",user="root",password="kushal11",db="grocery")
cursor = db.cursor()
cursor.execute("SELECT max(id) FROM hitnalli")
result = cursor.fetchall()
if result is not None:
    for r in result:
        id = r[0]
        if id is None:
            id=1
        else:
            id=id + 1
else:
    print("No results found")
class Database:
    def __init__(self ,master):
        self.master=master
        self.heading=Label(master,text="Add Stocks",font=('arial 50 bold'),fg='green')
        self.heading.place(x=500 , y=0)

        self.i=Label(master, text="ID Has reached upto: "+str(id),font=('arial 18 bold'))
        self.i.place(x=0,y=40)
        
        self.name=Label(master,text="Enter Product Name",font=('arial 18 bold'))
        self.name.place(x=0,y=80)
        
        self.stock=Label(master,text="Enter Stocks",font=('arial 18 bold'))
        self.stock.place(x=0,y=120)

        self.cost_price=Label(master,text=" Enter Cost price",font=('arial 18 bold'))
        self.cost_price.place(x=0,y=160)

        self.sell_price=Label(master,text="Enter Selling price",font=('arial 18 bold'))
        self.sell_price.place(x=0,y=200)

        self.vendor=Label(master,text=" EnterVendor name ",font=('arial 18 bold'))
        self.vendor.place(x=0,y=240)

        self.vendor_mobile_number=Label(master,text=" EnterMobile number",font=('arial 18 bold'))
        self.vendor_mobile_number.place(x=0,y=280)

        self.id_l=Label(master,text="Product ID ",font=('arial 18 bold'))
        self.id_l.place(x=0,y=320)

        self.name_a=Entry(master,width=30,font=('arial 18 bold'))
        self.name_a.place(x=250 ,y = 80)
        self.name_a.focus()

        self.name_b=Entry(master,width=30,font=('arial 18 bold'))
        self.name_b.place(x=250 ,y = 120)
        

        self.name_c=Entry(master,width=30,font=('arial 18 bold'))
        self.name_c.place(x=250 ,y = 160)
        

        self.name_d=Entry(master,width=30,font=('arial 18 bold'))
        self.name_d.place(x=250 ,y = 200)
        

        self.name_e=Entry(master,width=30,font=('arial 18 bold'))
        self.name_e.place(x=250 ,y = 240)
        

        self.name_f=Entry(master,width=30,font=('arial 18 bold'))
        self.name_f.place(x=250 ,y = 280)

        self.id_g=Entry(master,width=25,font=('arial 18 bold'))
        self.id_g.place(x=250,y=320)

        self.button=Button(master,text="Add to Database",width=25,height=4,bg="steelblue",fg="pink",font=('arial 18 bold'),command=self.get_items)
        self.button.place(x=360,y=380)

        



        self.textbox=Text(master,width=80,height=18)
        self.textbox.place(x=650,y=80)
        self.textbox.insert(END,"Product has reached upto: " +str(id))
        self.master.bind("<Return>",self.get_items)
        #self.master.bind("<Delete>",self.clear_all)

    
    def get_items(self,master=None,event=None):
        self.name = self.name_a.get()
        self.stock = self.name_b.get()
        self.costprice = self.name_c.get()
        self.sellprice = self.name_d.get()
        self.vendor = self.name_e.get()
        self.vendor_phone = self.name_f.get()

        if (self.name == "" or self.stock == '' or self.costprice == '' or 
            self.sellprice == '' or self.vendor == '' or self.vendor_phone == ''):
            tkinter.messagebox.showinfo("Error", "Please fill all the Entries")
            return  # Return from the function if any field is empty

        try:
            self.stock = int(self.stock)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Stock must be an integer value.")
            return
        
        try:
            self.costprice = int(self.costprice)
        except ValueError:
            tkinter.messagebox.showerror("Error", "price  must be an integer value.")
            return
        try:
            self.sellprice = int(self.sellprice)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Selling price  must be an integer value.")
            return
        try:
            self.costprice = float(self.costprice)
            self.sellprice = float(self.sellprice)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Cost Price and Sell Price must be valid numbers.")
            return

        if self.stock <= 0 or self.costprice <= 0 or self.sellprice <= 0:
            tkinter.messagebox.showinfo("Error", "Stock, Cost Price and Sell Price must be greater than zero")
            return

        self.totalcostprice = self.costprice * self.stock
        self.totalsellprice = self.sellprice * self.stock
        self.assumed_profit = self.totalsellprice - self.totalcostprice

        sql = "insert into hitnalli (sname, stock, costprice, sellprice, totalcostprice, totalsellprice, assumed_profit, vendor, vendor_phone_number) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.name, self.stock, self.costprice, self.sellprice, self.totalcostprice, self.totalsellprice, self.assumed_profit, self.vendor, self.vendor_phone))
        db.commit()
        self.textbox.insert(END, "\n\nInserted " + str(self.name) + " into the database.")
        tkinter.messagebox.showinfo("Success", "Successfully Stock added ")

        # Clear the entries
        self.name_a.delete(0, END)
        self.name_b.delete(0, END)
        self.name_c.delete(0, END)
        self.name_d.delete(0, END)
        self.name_e.delete(0, END)
        self.name_f.delete(0, END)
        self.id_g.delete(0,END)

        self.name_a.focus_set()
    
    




root = Tk()
b=Database(root)
root.geometry("1920x1080")
root.title("add Stockks")
#root.configure(bg="#8E3E63")
root.mainloop()
