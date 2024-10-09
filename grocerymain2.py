from tkinter import *
import mysql.connector
import tkinter.messagebox
from tkinter import ttk
import datetime
import math
import os
import random
import subprocess
from PIL import Image, ImageTk
db = mysql.connector.connect(host="localhost",user="root",password="kushal11",db="grocery")
cursor = db.cursor()

date=datetime.datetime.now().date()
time=datetime.datetime.now().strftime("%H:%M:%S")



#tmp list
products_list=[]
product_price=[]
product_quantity=[]
product_id=[]
labels_list=[]




class Application:
    def __init__(self,master):
        self.master=master
        self.heading=Label(master,text=" Everyday Essentials ",font=('arial 100  bold'),bg="#9B59B6",fg="white")
        self.heading.pack()
        #frames
        self.left=Frame(master,width=1200,height=860,bg='white')
        self.left.pack(side=LEFT)
        #image_path = r"C:\Final Accemedic project\accedmic project\Grocery Store project\Admin3.jpg"
        
        image_path = r"C:\Final Accemedic project\accedmic project\Grocery Store project\frame.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = Label(self.left, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep a reference to the image to prevent garbage collection
        label.image = photo
        


        self.right=Frame(master,width=680,height=860,bg='lightblue')
        self.right.pack(side=RIGHT)

        #compnents
        
        
        #self.heading=Label(self.left,text=" Grocery Store",font=('arial 50 bold'),bg="pink")
        #self.heading.place(x=100,y=0)

        #self.date_l=Label(self.right,text="Today Date: "+ str(date),font=("arial 15 bold "),bg="orange",fg="lightgreen")
        #self.date_l.place(x=0,y=0)

        #self.time_l=Label(self.right,text="Today Time : "+ str(time),font=("arial 15 bold "),bg="pink")
        #self.time_l.place(x=250,y=0)

        
        

        

        self.enterid=Label(self.left,text="Enter Product ID ",font=('arial 20 bold '),bg='blue',fg="white")
        self.enterid.place(x=0,y=80)
        
        

        self.enteride=Entry(self.left,width=20,font=("arial 20 bold"),bg="white")
        self.enteride.place(x=230,y=80)#x=190,y=500
        self.enteride.focus()

        

        self.search_btn=Button(self.left,text="Search",width=20,height=2,bg='red',command=self.ajax)
        self.search_btn.place(x=350,y=120)

        self.productname=Label(self.left,text=" ",font=('arial 25 bold'),bg='white',fg='orange')
        self.productname.place(x=0,y=200)

        self.ppricename=Label(self.left,text=" ",font=('arial 25 bold'),bg='white',fg='orange')
        self.ppricename.place(x=0,y=240)


        self.pstock=Label(self.left,text=" ",font=('arial 25 bold'),bg='white',fg='orange')
        self.pstock.place(x=0,y=280)

        


        #Add to Database button
        #self.add_btn=Button(self.left,text="Add Stocks",width=25,height=2,bg="grey",command=self.run_script)
        #self.add_btn.place(x=0,y=600)

         #update button
        #self.upd_btn=Button(self.left,text="update",width=25,height=2,bg="red",command=self.updatefile)
        #self.upd_btn.place(x=350,y=600)

         #display transaction items or bill items
        self.trn_btn=Button(self.left,text="last purchased items ",width=25,height=2,bg="lightblue",command=self.transaction)
        self.trn_btn.place(x=800,y=0)

        #admin button
        self.admin_btn=Button(self.left,text="Admin only ",width=25,height=2,bg="lightblue",command=self.admin_login)
        self.admin_btn.place(x=0,y=0)

        #avalible stocks btuuon
        self.stc_btn=Button(self.left,text="Avalible stocks ",width=25,height=2,bg="grey",command=self.avalible)
        self.stc_btn.place(x=1020,y=0)
        
        

        
     #total labels
        self.total_l=Label(self.right,text=" ",font=('arial 40 bold'),bg='lightblue',fg='white')
        self.total_l.place(x=0,y=730)

        self.master.bind("<Return>",self.ajax)
        self.master.bind("<Up>",self.add_to_cart)
        self.master.bind("<space>",self.generatebill)
        self.master.bind("<Down>",self.run_script)
        self.master.bind("<Left>",self.updatefile)
        #self.master.bind("<Return>",self.admin_dashboard)
        
    def ajax(self,master=None,event=None):
        try:
            self.get_id = int(self.enteride.get())
            if self.get_id <0:
                tkinter.messagebox.showerror("Error","Please enter a valid / positive  product ID")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a valid product ID (integer only)")
        else:
    # If no exception is raised, execute this block
            pass
        
            
            
            
        #get products info with id 
        query="select *  from hitnalli where id= %s"
        cursor.execute(query,(self.get_id, ))
        result=cursor.fetchall()
        if  not result :
            tkinter.messagebox.showerror("Error ","there is no product  exist in databse ")
            return
        else:
            for self.r in result:
                self.get_id=self.r[0]
                self.get_name=self.r[1]
                self.get_price=self.r[4]
                self.get_stock=self.r[2]
        
        #self.quantity_value
        
            
        
            #self.right=Frame(master,width=680,height=860,bg='lightblue')
        #self.right.pack(side=RIGHT)

        
        
        
            self.productname.configure(text="Product Name: "+ str(self.get_name))
            self.ppricename.configure(text="Price: RS.  " +str(self.get_price))
            self.pstock.configure(text="Avalible stock: "+str(self.get_stock))
        
        

            self.quantity_l=Label(self.left,text="Enter Quantity",font=('arial 20 bold '),bg='blue',fg="white")
            self.quantity_l.place(x=0,y=370)

            self.quantity_e=Entry(self.left,width=15,font=('arial 20 bold'),bg="white")
            self.quantity_e.place(x=230,y=370)
            self.quantity_e.focus()

        #discount
            self.discount_l=Label(self.left,text="Enter Discount",font=('arial 20 bold '),bg='blue',fg="white")
            self.discount_l.place(x=0,y=410)
        

            self.discount_e=Entry(self.left,width=15,font=('arial 20 bold'),bg="white")
            self.discount_e.place(x=230,y=410)
            self.discount_e.insert(END,0)
        
        #cart button 
            self.cart_btn=Button(self.left,text="Add To Cart",width=20,height=2,bg='orange',command=self.add_to_cart)
            self.cart_btn.place(x=350,y=450)

        #generate bill and change
            self.change_l=Label(self.left,text="Given Amount",font=('arial 18 bold'),bg='blue',fg="white")
            self.change_l.place(x=0,y=500)

            self.change_e=Entry(self.left,width=15,font=('arial 20 bold'),bg="white")
            self.change_e.place(x=230,y=500)
       #change
            self.change_btn=Button(self.left,text="Calculate Change ",width=20,height=2,bg='pink',command=self.change)
            self.change_btn.place(x=350,y=550)

        #bill
            self.bill_btn=Button(self.left,text="Generate Bill",width=25,height=2,bg='green',command=self.generatebill)
            self.bill_btn.place(x=0,y=550)

    

    
    def avalible(self, master=None, event=None):
        sql3 = "select id ,sname , stock  from hitnalli"
        cursor.execute(sql3)
        results = cursor.fetchall()

    # Create a new Tkinter window
        self.new_window = Toplevel(self.master)
        self.new_window.title("Transaction Results")

    # Create a frame to hold the Treeview with a border
        frame = Frame(self.new_window, highlightbackground="black", highlightthickness=2)
        frame.pack(fill="both", expand=True)

    # Create a Treeview widget to display the results
        style = ttk.Style()
        style.configure("Treeview", borderwidth=0)  # Remove the default border
        self.treeview = ttk.Treeview(frame)

    # Define the columns
        columns = [desc[0] for desc in cursor.description]
        self.treeview['columns'] = columns

    # Format the columns
        for column in columns:
            self.treeview.column(column, anchor="w")
            self.treeview.heading(column, text=column, anchor='w')

    # Insert the results into the Treeview
        for row in results:
            self.treeview.insert('', 'end', values=list(row))

    # Pack the Treeview
        self.treeview.pack(fill="both", expand=True)    
    def admin_login(self,master=None, event=None):
        self.admin_login_window = Toplevel(self.master)
        self.admin_login_window.title("Admin Login")
        self.admin_login_window.geometry("1920x1080")
        # Load an image using PIL and convert it to a PhotoImage object
        image_path = r"C:\Final Accemedic project\accedmic project\Grocery Store project\admin3.jpg"
        pil_image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage( pil_image)

        # Create a Label widget and set its image option
        label = Label(self.admin_login_window, image=self.photo)  # Use self.admin_login_window instead of root
        label.image = self.photo  # Keep a reference to the image object
        label.place(relheight=1, relwidth=1)


        self.username_label = Label(self.admin_login_window, text="Username:",font=('arial 20 bold '),bg='#E2E2B6')
        self.username_label.place(x=700,y=180)

        self.username_entry = Entry(self.admin_login_window, width=20,font=('arial 20 bold'),bg='#7FA1C3')
        self.username_entry.place(x=900,y=180)
        self.username_entry.focus()
        

        self.password_label = Label(self.admin_login_window, text="Password:",font=('arial 20 bold '),bg='#E2E2B6')
        self.password_label.place(x=700,y=220)

        self.password_entry = Entry(self.admin_login_window, width=20, show="*",font=('arial 20 bold '),bg='#7FA1C3')
        self.password_entry.place(x=900,y=220)

        self.login_button = Button(self.admin_login_window, text="Get-In",bg="#88D66C",fg="#201E43",width=25,height=2,command=self.check_credentials)
        self.login_button.place(x=1005,y=270)

        self.admin_login_window.bind("<Return>",self.check_credentials)
        
    def check_credentials(self,master=None, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":  # Replace with your own credentials
            self.admin_login_window.destroy()
            self.admin_dashboard()
        else:
            tkinter.messagebox.showerror("Error", "Invalid username or password")
    def admin_dashboard(self, master=None, event=None):
        self.admin_dashboard_window = Toplevel(self.master)
        self.admin_dashboard_window.title("Admin Dashboard")
        self.admin_dashboard_window.geometry("1920x1080")
         # Load an image using PIL and convert it to a PhotoImage object
        image_path = r"C:\Final Accemedic project\accedmic project\Grocery Store project\dashboard.jpg"
        pil_image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage( pil_image)
        label = Label(self.admin_dashboard_window, image=self.photo)  # Use self.admin_login_window instead of root
        label.image = self.photo  # Keep a reference to the image object
        label.place(relheight=1, relwidth=1)

        label = Label(self.admin_dashboard_window, text="Welcome to the Admin Dashboard!",font=('arial 70 bold'),bg="pink")#text="Santosh Grocery Store",font=('arial 50 bold'),bg="pink"
        label.pack()
       
        self.add_btn=Button(self.admin_dashboard_window,text="ADD STOCKS",width=55,height=4,bg="grey",font=('arial', 10, 'bold'),command=self.run_script)
        self.add_btn.place(x=800,y=250)
        self.upd_btn=Button(self.admin_dashboard_window,text="UPDATE STOCKS ",width=55,height=4,bg="red",font=('arial', 10, 'bold'),command=self.updatefile)
        self.upd_btn.place(x=800,y=550)

        
    def transaction(self, master=None, event=None):
        sql3 = "select * from transaction"
        cursor.execute(sql3)
        results = cursor.fetchall()

    # Create a new Tkinter window
        self.new_window = Toplevel(self.master)
        self.new_window.title("Transaction Results")

    # Create a Treeview widget to display the results
        style = ttk.Style()
        style.configure("Treeview", borderwidth=2, relief="ridge")
        self.treeview = ttk.Treeview(self.new_window)

    # Define the columns
        columns = [desc[0] for desc in cursor.description]
        self.treeview['columns'] = columns

    # Format the columns
        for column in columns:
            self.treeview.column(column, anchor="w")
            self.treeview.heading(column, text=column, anchor='w')

    # Insert the results into the Treeview
        for row in results:
            self.treeview.insert('', 'end', values=list(row))

    # Pack the Treeview
        self.treeview.pack(fill="both", expand=True)
        
    def run_script(self,master=None, event=None):
        subprocess.call(["python","C:/Final Accemedic project/accedmic project/Grocery Store project/source code/grocery_add.py"])
    def updatefile(self,master=None,event=None):
        subprocess.call(["python","C:/Final Accemedic project/accedmic project/Grocery Store project/source code/grocery_update.py"])

    

    def add_to_cart(self, master=None, event=None):
        
        try: # get quantity from the database
            self.quantity_value = int(self.quantity_e.get())
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a valid quantity (integer only)")
            
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "OOPS Out of stocks Sorry")
        else:
            self.get_stock = int(self.get_stock) - self.quantity_value
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))

            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            #self.get_stock = int(self.get_stock) - self.quantity_value
            #self.pstock.configure(text="Avalible stock: "+str(self.get_stock))

            self.x_index = 0
            self.y_index = 100
            self.counter = 0

            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 20 bold'), bg='lightblue', fg='white')
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)
                self.tempname.bind("<Button-1>", lambda event, i=self.counter: self.delete_item(i))

                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 20 bold'), bg='lightblue', fg='white')
                self.tempqt.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt)
                self.tempqt.bind("<Button-1>", lambda event, i=self.counter: self.delete_item(i))

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 20 bold'), bg='lightblue', fg='white')
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)
                self.tempprice.bind("<Button-1>", lambda event, i=self.counter: self.delete_item(i))

                self.delete_btn = Button(self.right, text="Delete", font=('arial 10 bold'), bg='red', fg='white', command=lambda i=self.counter: self.delete_item(i))
                self.delete_btn.place(x=700, y=self.y_index)
                labels_list.append(self.delete_btn)

                self.y_index += 40
                self.counter += 1

                self.date_l=Label(self.right,text="Today Date: "+ str(date),font=("arial 15 bold "),bg="orange",fg="lightgreen")
                self.date_l.place(x=0,y=0)

                self.time_l=Label(self.right,text="Today Time : "+ str(time),font=("arial 15 bold "),bg="pink")
                self.time_l.place(x=250,y=0)

        #table
                self.tproduct=Label(self.right,text="Products",font=("arial 25 bold "),bg="lightblue",fg='white')
                self.tproduct.place(x=0,y=30)

                self.tquantity=Label(self.right,text="Quantity",font=("arial 25 bold "),bg="lightblue",fg='white')
                self.tquantity.place(x=300,y=30)

                self.tamount=Label(self.right,text="Amount",font=("arial 25 bold "),bg="lightblue",fg='white')
                self.tamount.place(x=500,y=30)

                # total configure
                self.total_l.configure(text="Total:Rs. " + str(sum(product_price)))

                # delete
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()

                self.productname.configure(text="")
                self.ppricename.configure(text="")
                self.pstock.configure(text="")
                self.cart_btn.destroy()

                # autofocus
                self.enteride.focus()
                self.enteride.delete(0, END)


    def delete_item(self, i):
        del products_list[i]
        del product_price[i]
        del product_quantity[i]
        del product_id[i]

        for widget in labels_list:
            widget.destroy()

        labels_list.clear()

        self.x_index = 0
        self.y_index = 100
        self.counter = 0

        for self.p in products_list:
            self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 20 bold'), bg='lightblue', fg='white')
            self.tempname.place(x=0, y=self.y_index)
            labels_list.append(self.tempname)
            self.tempname.bind("<Button-1>", lambda event, i=self.counter: self.delete_item(i))

            self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 20 bold'), bg='lightblue', fg='white')
            self.tempqt.place(x=300, y=self.y_index)
            labels_list.append(self.tempqt)
            self.tempqt.bind("<Button-1>", lambda event, i=self.counter: self.delete_item(i))

            self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 20 bold'), bg='lightblue', fg='white')
            self.tempprice.place(x=500, y=self.y_index)
            labels_list.append(self.tempprice)
            self.tempprice.bind("<Button-1>", lambda event, i=self.counter: self.delete_item(i))

            self.delete_btn = Button(self.right, text="Delete", font=('arial 10 bold'), bg='red', fg='white', command=lambda i=self.counter: self.delete_item(i))
            self.delete_btn.place(x=700, y=self.y_index)
            labels_list.append(self.delete_btn)

            self.y_index += 40
            self.counter += 1

        self.total_l.configure(text="Total:Rs. " + str(sum(product_price)))
        
                
                


                
    def change(self,master=None,event=None):
        #get amount given

        self.amount_given=float(self.change_e.get())
        self.our_total=float(sum(product_price))

        self.to_give=self.amount_given - self.our_total

        #label change

        self.c_amount=Label(self.left,text="Change:RS. " +str(self.to_give),font=('arial 20 bold '),fg='red')
        self.c_amount.place(x=550 , y=550)

    def generatebill(self,master=None,event=None):
        if not products_list:
            tkinter.messagebox.showerror("Error", "Bill is empty. Please add some products to generate the bill.")
        else:
        #create the bill before udpating
            date=datetime.datetime.now().date()
            time =datetime.datetime.now().strftime("%H-%M-%S").replace(":", "-")

            directory = "C:/Final Accemedic project/accedmic project/Grocery Store project/invoice/" + str(date) + str(time)+'/'
            if not os.path.exists(directory):
                os.makedirs(directory)

        #template for bill
            company="\t\t\t\t Santosh B. M PVT\n "
            address="\t\t\t\t Vijayapura\n "
            phonenum="\t\t\t\t8904912385\n"
            sample=  "\t\t\t\tINVOICE\n"#random
            time="\t\t\t\t\tTime: " + str(time)
            dt=   "\t\t\t\t Date: " +str(date)

            table_header='\n\n\t\t\t...............................................................................\n \t\t\t SN.\t\t\t Products\t\tQuntity\t\tAmount\n\t...............................................................................'
            final = company + address + phonenum +  sample +time + dt + '\n' + table_header

        #open file
            file_name=str(directory) + str(random.randrange(100 , 500))+ ".rtf"
            f=open(file_name, 'w')
            f.write(final)
        #fill dynamics
            r = 1
            for t in products_list:
                f.write('\n\t\t\t' + str(r)+'\t\t\t'+ str(t[:7])+'\t\t\t'+str(product_quantity[r-1])+'\t\t\t'+ str(product_price[r-1]))
                r += 1
            f.write('\n\n\t\t\tTotal:RS. '+str(sum(product_price)))
            f.write('\n\t\t\tTHANKS FOR VISITING ....')
        #os.startfile(file_name , "print",shell=True)
            subprocess.run(['print', file_name], shell=True)
            f.close()

            tkinter.messagebox.showinfo("Bill Created","Bill Created successfully")
        
        
        
            
##        #minus the stock
        self.x=0
        initial="select * from hitnalli where id= %s"
        cursor.execute(initial,(product_id[self.x], ))
        result=cursor.fetchall()
        
        for i in products_list:
            for r in result:
                self.old_stock=r[2]
            self.new_stock=int(self.old_stock)-int(product_quantity[self.x])

            sql="update hitnalli set stock= %s where id= %s"
            cursor.execute(sql,(self.new_stock,product_id[self.x]))
            db.commit()

            #transaction table insert
            sql2="insert into transaction(productname , quantity , amount , date)values(%s, %s, %s, %s)"
            cursor.execute(sql2,(products_list[self.x],product_quantity[self.x],product_price[self.x],date))
            db.commit()

            self.x +=1
            
        for a in labels_list:
            a.destroy()
        del(products_list[ : ])
        del(product_id[ : ])
        del(product_quantity[ : ])
        del(product_price[ : ])

        self.total_l.configure(text="")
        self.c_amount.configure(self,text="")
        self.change_e.delete(0,END)
        self.enteride.focus()

        tkinter.messagebox.showinfo("Sucess","Thankgod Everything is running sommthly")    

root=Tk()
b=Application(root)
root.geometry("1920x1080")
root.configure(bg="purple")
root.mainloop()


