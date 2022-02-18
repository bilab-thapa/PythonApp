from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from server import *
from Add import *
from Bills import *


class Main:
    def __init__(self):
        self.db=DataBase()
        self.customer=Customer()
        self.bill=Billing()


    def root(self):
        self.window = Tk()
        self.window.state('zoomed')
        self.window.title('Raju Electronics')
        self.window.configure(bg='purple4')
        self.main = Label(self.window, text="Login or Register", bg='dark orange', fg='black', font=('Ariel',28, 'bold'))
        self.main.place(x=550, y=20)
        self.main.pack(fill=X, pady=20)

        self.sab1 = Button(self.window, text= 'Login', font=('Ariel', 18, 'bold'), bg='white', command=self.logwindow)
        self.sab1.place(x=610, y=150)


        self.sab = Button(self.window, text='Register', font=('Ariel', 18, 'bold'), bg='white', command=self.regwindow)
        self.sab.place(x=600, y=250)

        self.window.mainloop()

    def register(self):
        self.window1 = Tk()
        self.window1.state('zoomed')
        self.window1.title(' Staff Registration')
        self.window1.configure(bg='orangered3')

        self.name = Label(self.window1, text="First Name", bg='orangered3', fg='white', font=('Ariel', 12, 'bold'))
        self.name.place(x=100, y=40)

        self.name_ent = Entry(self.window1, font=('Ariel', 12, 'bold'))
        self.name_ent.place(x=220, y=40)

        self.lname = Label(self.window1, text="Last Name", bg='orangered3', fg='white', font=('Ariel', 12, 'bold'))
        self.lname.place(x=100, y=100)
        self.lname = Entry(self.window1, font=('Ariel', 12, 'bold'))
        self.lname.place(x=220, y=100)


        self.contact = Label(self.window1, text="Contact", bg='orangered3', fg='white', font=('Ariel', 12, 'bold'))
        self.contact.place(x=100, y=150)
        self.contact_ent = Entry(self.window1, font=('Ariel', 12, 'bold'))
        self.contact_ent.place(x=220, y=150)

        self.address = Label(self.window1, text="Address", bg='orangered3', fg='white', font=('Ariel', 12, 'bold'))
        self.address.place(x=100, y=200)
        self.address_ent = Entry(self.window1, font=('Ariel', 12, 'bold'))
        self.address_ent.place(x=220, y=200)

        self.user_name = Label(self.window1, text="User Name", bg='orangered3', fg='white', font=('Ariel', 12, 'bold'))
        self.user_name.place(x=100, y=250)
        self.user_name_ent = Entry(self.window1, font=('Ariel', 12, 'bold'))
        self.user_name_ent.place(x=220, y=250)
        self.password = Label(self.window1, text="Password", bg='orangered3', fg='white', font=('Ariel', 12, 'bold'))
        self.password.place(x=100, y=300)
        self.password_ent = Entry(self.window1, font=('Ariel', 12, 'bold'))
        self.password_ent.place(x=220, y=300)
        self.sam = Button(self.window1, text='Save', font=('Ariel', 12, 'bold'), command=self.register_user)

        self.sam.place(x=250, y=350)

        self.sam1 = Button(self.window1, text='Back', font=('Ariel', 12, 'bold'), command=self.back)

        self.sam1.place(x=350, y=350)
        self.window1.mainloop()


    def back(self):
        self.window1.destroy()
        self.root()

    def register_user(self):

        self.db=DataBase()
        fname = self.name_ent.get()
        lname = self.lname.get()
        address = self.address_ent.get()
        contact = self.contact_ent.get()
        un = self.user_name_ent.get()
        pw = self.password_ent.get()
        if fname == '' or lname == '' or contact == '' or un == '' or pw == '' or address == '':
            messagebox.showerror('Error', 'Fill up all entries!')
        else:
            qry = '''insert into user_reg (username, password, first_name, last_name, address, phone) values(%s,%s,%s,%s,%s,%s)'''
            vals = (un, pw, fname, lname ,address, contact )
            self.db.iud(qry, vals)
            messagebox.showinfo('Done', 'Register Successful!')



    def login(self):
        self.window2 = Tk()
        self.window2.state('zoomed')
        self.window2.title('log-in')
        self.window2.configure(bg='#833AB4')

        self.name = Label(self.window2, text="Enter Username and Password  ", bg='#F56040', fg='white',
                          font=('Ariel', 17, 'bold'))
        self.name.pack(pady=20, fill=X)
        self.user_name = Label(self.window2, text="Username", bg='#833AB4', fg='white', font=('Ariel', 14, 'bold'))
        self.user_name.pack(pady=20)
        self.user_name_ent = Entry(self.window2, font=('Ariel', 14, 'bold'))
        self.user_name_ent.pack(pady=5)
        self.password = Label(self.window2, text="Password", bg='#833AB4', fg='white', font=('Ariel', 14, 'bold'))
        self.password.pack(pady=20)
        self.password_ent = Entry(self.window2, show='*', font=('Ariel', 14, 'bold'))
        self.password_ent.pack(pady=5)
        self.submit = Button(self.window2, text='Login', fg='black', bg='white', font=('Ariel', 14, 'bold'),
                             command=self.login_user)
        self.submit.pack(pady=20)


    def login_user(self):
        self.db = DataBase()
        username1 = self.user_name_ent.get()
        password1 = self.password_ent.get()
        if username1 == '' or password1 == '':
            messagebox.showerror('Error', 'Enter username or password')
        else:

            qry = '''select * from user_reg where username=%s and password=%s'''
            vals = (username1, password1)
            data_return = self.db.get_data_p(qry, vals)
            print(len(data_return))
            print(data_return)

            if len(data_return) == 0:
                messagebox.showerror('Error', 'Wrong username or password')
            else:
                messagebox.showinfo('Done', 'Login Successful')
                self.aftlogin()


    def dashboard(self):

        self.window3 = Tk()
        self.window3.state('zoomed')
        self.window3.title('Dashboard')
        self.window3.configure(bg='#FCAF45')

        self.Dashboard = Label(self.window3, text="Select for New Client or Sales Report", font=('Ariel', 14, 'bold'))
        self.Dashboard.pack( pady=30, fill=X)
        self.sale = Button(self.window3, text="Sales", bg='white', fg='black', font=('Ariel', 14),command=self.sales)
        self.sale.pack(padx=10, pady=20)
        self.product = Button(self.window3, text="Client Registration", bg='white', fg='black', font=('Ariel', 14), command=self.regclient)
        self.product.pack(padx=10, pady=20)

        self.window3.mainloop()


    def regwindow(self):
        self.window.destroy()
        self.register()

    def logwindow(self):
        self.window.destroy()
        self.login()

    def aftlogin(self):
        self.window2.destroy()
        self.dashboard()

    def regclient(self):
        self.window3.destroy()
        self.customer = Customer()
        self.customer.add_product()

    def sales(self):
        self.window3.destroy()
        self.bill = Billing()
        self.bill.add_sale()




aa=Main()
aa.root()