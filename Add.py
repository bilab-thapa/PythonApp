from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from server import *
from datetime import *

class Customer:
    def __init__(self):
        self.db = DataBase()
        self.autoindex=''

    def add_product(self):
        self.window5 = Tk()
        self.window5.state('zoomed')
        self.window5.title('Raju Electronics')
        self.window5.configure(bg='#22516a')
        self.Dashboard = Label(self.window5, text="Registered details", font=('Ariel', 14, 'bold'),bg = '#cfcfc9')
        self.Dashboard.pack(pady=15, fill=X)


        self.lbl1 = Label(self.window5, text="Customer name", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl1.place(x=100, y=50)
        self.ent1 = Entry(self.window5, font=('Ariel', 12, 'bold'))
        self.ent1.place(x=250, y=50)
        self.lbl2 = Label(self.window5, text="Contact no.", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl2.place(x=100, y=100)
        self.ent2 = Entry(self.window5, font=('Ariel', 12, 'bold'))
        self.ent2.place(x=250, y=100)
        self.lbl3 = Label(self.window5, text="Brand", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl3.place(x=100, y=150)
        self.values1 = ['Samsung', 'Mi', 'OnePlus', 'Apple', 'Oppo', 'Huawei', 'HTC','Google']
        self.ent3 = ttk.Combobox(self.window5, values=self.values1, font=('Ariel', 12, 'bold'))
        self.ent3.set('---select brand--')
        self.ent3.place(x=250, y=150)
        self.lbl4 = Label(self.window5, text="Model", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl4.place(x=100, y=200)

        self.ent4 = Entry(self.window5, font=('Ariel', 12, 'bold'))
        self.ent4.place(x=250, y=200)

        self.lbl5 = Label(self.window5, text="Problem", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl5.place(x=100, y=250)
        self.values = ['Battery', 'iCloud_lock', 'Display','chip','Touch_panel','Heating','sensors']
        self.ent5 = ttk.Combobox(self.window5, values=self.values,font=('Ariel', 12, 'bold'))
        self.ent5.set('---select problem--')
        self.ent5.place(x=250, y=250)

        self.lbl61 = Label(self.window5, text="Registered date", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl61.place(x=100, y=350)
        self.ent7 = Entry(self.window5, font=('Ariel', 12, 'bold'))
        self.ent7.place(x=250, y=350)
        today = date.today()
        self.ent7.insert(0, today)

        self.lbl6 = Label(self.window5, text="Return date", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl6.place(x=100, y=400)
        self.ent6 = Entry(self.window5, font=('Ariel', 12, 'bold'))
        self.ent6.place(x=250, y=400)

        self.lbl8 = Label(self.window5, text="Total cost", bg='#22516a', fg='white', font=('Ariel', 12, 'bold'))
        self.lbl8.place(x=100, y=300)
        self.ent8 = Entry(self.window5, font=('Ariel', 12, 'bold'))
        self.ent8.place(x=250, y=300)

        self.submit = Button(self.window5, text="Register ", bg='#768997', fg='white', font=('Ariel', 12, 'bold'), command=self.register_phone)
        self.submit.place(x=110, y=500)
        self.submit = Button(self.window5, text="Update ", bg='#768997', fg='white', font=('Ariel', 12, 'bold'), command=self.update_phone)
        self.submit.place(x=210, y=500)
        self.submit = Button(self.window5, text="Delete ", bg='#768997', fg='white', font=('Ariel', 12, 'bold'), command=self.delete_detail)
        self.submit.place(x=310, y=500)
        self.submit = Button(self.window5, text="Back ", bg='#768997', fg='white', font=('Ariel', 12, 'bold'),command=self.back1)
        self.submit.place(x=1100, y=500)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("mystyle.Treeview", font=('Ariel', 9, 'bold'), background="grey", foreground="grey")
        self.style.configure("mystyle.Treeview.Heading", font=('Ariel', 10, 'bold'), background="white", fg='grey')

        self.aaa_tree = ttk.Treeview(self.window5, style='mystyle.Treeview', column=('a', 'b', 'c', 'd', 'e','o', 'f','g'), height=17)
        self.aaa_tree.place(x=500, y=70)
        self.aaa_tree['show'] = 'headings'
        self.aaa_tree.column('a', width=100)
        self.aaa_tree.column('b', width=100)
        self.aaa_tree.column('c', width=100)
        self.aaa_tree.column('d', width=100)
        self.aaa_tree.column('e', width=100)
        self.aaa_tree.column('o', width=100)
        self.aaa_tree.column('f', width=100)
        self.aaa_tree.column('g', width=100)

        self.aaa_tree.heading('a', text='Customer')
        self.aaa_tree.heading('b', text='Contact')
        self.aaa_tree.heading('c', text='Brand')
        self.aaa_tree.heading('d', text='Model')
        self.aaa_tree.heading('e', text='Problem')
        self.aaa_tree.heading('o', text='Total cost')
        self.aaa_tree.heading('f', text='Registered Date')
        self.aaa_tree.heading('g', text='Return Date')
        self.showdata()

        self.window5.mainloop()

    def back1(self):
        self.window5.destroy()
        from MainApp import Main
        self.main=Main()
        self.main.dashboard()

    def register_phone(self):
        self.db = DataBase()
        try:
            customer= self.ent1.get()
            contact=self.ent2.get()
            brand= self.ent3.get()
            model=self.ent4.get()
            problem=self.ent5.get()
            returndate=self.ent6.get()
            regdate=self.ent7.get()
            fixprice=self.ent8.get()

            if customer == "" or contact == '' or brand == '' or fixprice == '' or regdate == '':
                messagebox.showerror('Error', "Fill up all the entries")
                return False

            else:
                qry = '''insert into reg_phone (customer, contact, brand, model, problem, returndate,regdate, fixprice ) values (%s,%s,%s,%s,%s,%s,%s,%s)'''
                vals = (customer, contact, brand, model, problem, returndate,regdate, fixprice )
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Registered successfully!')
                self.showdata()
                return True
        except Exception as e:
            print(e)




    def showdata(self):
        self.db = DataBase()
        try:
            qry='''select * from reg_phone'''
            res=self.db.get_data(qry)

            self.aaa_tree.delete(*self.aaa_tree.get_children())
            for i in res:
                self.aaa_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[8],i[7],i[6]))
            self.aaa_tree.bind("<Double-1>", self.select_details)
        except Exception as e:
            print(e)

    def select_details(self,event):
        sel_row = self.aaa_tree.selection()[0]
        self.autoindex = self.aaa_tree.item(sel_row, 'text')
        selected_data = self.aaa_tree.item(sel_row, 'values')
        self.ent1.delete(0, 'end')
        self.ent1.insert(0, selected_data[0])
        self.ent2.delete(0, 'end')
        self.ent2.insert(0, selected_data[1])
        self.ent3.delete(0, 'end')
        self.ent3.insert(0, selected_data[2])
        self.ent4.delete(0, 'end')
        self.ent4.insert(0, selected_data[3])
        self.ent5.delete(0, 'end')
        self.ent5.insert(0, selected_data[4])
        self.ent6.delete(0, 'end')
        self.ent6.insert(0, selected_data[7])
        self.ent7.delete(0, 'end')
        self.ent7.insert(0, selected_data[6])
        self.ent8.delete(0, 'end')
        self.ent8.insert(0, selected_data[5])

    def update_phone(self):
        self.db = DataBase()
        try:

            customer = self.ent1.get()
            contact = self.ent2.get()
            brand = self.ent3.get()
            model = self.ent4.get()
            problem = self.ent5.get()
            returndate = self.ent6.get()
            regdate = self.ent7.get()
            fixprice = self.ent8.get()
            index = self.autoindex

            if self.autoindex == "":
                messagebox.showerror("Error", "Select something first")

            else:

                qry = "UPDATE reg_phone SET customer=%s, contact=%s, brand=%s, model=%s, problem=%s, returndate=%s,regdate=%s, fixprice=%s  WHERE id = %s"
                values = (customer, contact, brand, model, problem, returndate,regdate, fixprice,index)
                self.db.iud(qry, values)
                messagebox.showinfo("Success", "Details Updated")
                self.showdata()

        except Exception as e:
            print(e)


    def delete_detail(self):
        self.db = DataBase()
        try:
            index = [self.autoindex]
            if index == "":
                messagebox.showerror("Error", "Select detail first")
                return False
            else:
                qry = "DELETE FROM reg_phone  WHERE id=%s"
                values = (index)
                self.db.iud(qry, values)
                messagebox.showinfo("Done", "Details removed")
                self.showdata()
                return True
        except Exception as e:
            print(e)










