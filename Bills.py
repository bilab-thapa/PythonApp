from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from server import *
from datetime import *



class Billing:
    def __init__(self):
        self.database = DataBase()

    def add_sale(self):

        self.window1 = Tk()
        self.window1.title("Sales Report")
        self.window1.state('zoomed')
        self.window1.configure(bg="#22516a")

        self.lbl = Label(self.window1, text="Sort by ", fg="black",
                         font=("arial", 10, "bold"))
        self.lbl.place(x=30, y=70)
        como = ["Registered Date", 'Return Date', 'Model']
        self.entry = ttk.Combobox(self.window1, values=como)
        self.entry.set('---sortby----')
        self.entry.place(x=100, y=70)

        self.lbl1 = Label(self.window1, text="Keyword ", fg="dark blue",
                          font=("arial", 10, "bold"))
        self.lbl1.place(x=30, y=110)
        self.entry2 = Entry(self.window1)
        self.entry2.place(x=100, y=110)

        self.sc_but = Button(self.window1, text="Search", font=("arial", 10, "bold"), command=self.search_button)
        self.sc_but.place(x=170, y=140)

        self.lbl = Label(self.window1, text="Brand ", fg="dark blue", width=15,
                         font=("arial", 10, "bold"))
        self.lbl.place(x=30, y=200)
        self.entry_ac = Entry(self.window1)
        self.entry_ac.place(x=190, y=200)

        self.p = Label(self.window1, text="Model ", fg="dark blue", width=15,
                       font=("arial", 10, "bold"))
        self.p.place(x=30, y=230)

        self.entry_p = Entry(self.window1)
        self.entry_p.place(x=190, y=230)

        self.b = Label(self.window1, text="Problem", fg="dark blue", width=15, font=("arial", 10, "bold"))
        self.b.place(x=30, y=260)
        self.combox = Entry(self.window1, width=30)
        self.combox.place(x=190, y=260)

        self.tc = Label(self.window1, text="Customer Name ", fg="dark blue",width=15, font=("arial", 10, "bold"))
        self.tc.place(x=30, y=290)
        self.entry_tc = Entry(self.window1, width=30)
        self.entry_tc.place(x=190, y=290)

        self.Ph = Label(self.window1, text="Bill Date", fg="dark blue",width=15, font=("arial", 10, "bold"))
        self.Ph.place(x=30, y=320)
        self.entry_st = Entry(self.window1,textvariable='d')
        self.entry_st.place(x=190, y=320)

        today = date.today()
        self.entry_st.insert(0, today)

        self.des = Label(self.window1, text="Cost Paid ",width=15, fg="dark blue",
                         font=("arial", 10, "bold"))
        self.des.place(x=30, y=350)
        self.entry_des = Entry(self.window1, textvariable='e')
        self.entry_des.place(x=190, y=350)

        self.submit = Button(self.window1, text="Store ", fg='black',bg='white', font=('Ariel', 12, 'bold'), command=self.store_details)
        self.submit.place(x=290, y=460)

        self.submit2 = Button(self.window1, text="Back ", bg='white', fg='black', font=('Ariel', 12, 'bold'), command=self.back12)
        self.submit2.place(x=1100, y=460)


        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("mystyle.Treeview", font=('Ariel', 9, 'bold'), background="grey", foreground="grey")
        self.style.configure("mystyle.Treeview.Heading", font=('Ariel', 10, 'bold'), background="white", fg='grey')

        self.aaa_tree = ttk.Treeview(self.window1, style='mystyle.Treeview',
                                     column=('a', 'b', 'c', 'd', 'e', 'o', 'f', 'g'), height=17)
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
        self.aaa_tree.heading('o', text='Fix Price')
        self.aaa_tree.heading('f', text='Registered Date')
        self.aaa_tree.heading('g', text='Return Date')
        self.showdata()

        self.window1.mainloop()

    def back12(self):
        self.window1.destroy()
        from MainApp import Main
        self.main=Main()
        self.main.dashboard()


    def showdata(self):
        self.db = DataBase()
        try:
            qry='''select * from reg_phone'''
            res=self.db.get_data(qry)

            self.aaa_tree.delete(*self.aaa_tree.get_children())
            for i in res:
                self.aaa_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[8],i[7],i[6]))
            self.aaa_tree.bind("<Double-1>", self.select_detail)
        except Exception as e:
            print(e)


    def search_button(self):
        self.database = DataBase()
        try:

            uinput = self.entry.get()
            keyword = self.entry2.get()

            if uinput == 'Registered Date':
                qry = "SELECT * FROM reg_phone WHERE regdate LIKE '" + keyword + "%'"
                win = self.database.get_data_p(qry, keyword)

                self.aaa_tree.delete(*self.aaa_tree.get_children())
                for i in win:
                    self.aaa_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6],i[7],i[8]))
                    self.aaa_tree.bind("<Double-1>", self.select_detail)

            elif uinput == 'Return Date':
                qry = "SELECT * FROM reg_phone WHERE returndate LIKE '" + keyword + "%' "
                win = self.database.get_data_p(qry, keyword)

                self.aaa_tree.delete(*self.aaa_tree.get_children())
                for i in win:
                    self.aaa_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6],i[7],i[8]))
                    self.aaa_tree.bind("<Double-1>", self.select_detail)

            elif uinput == 'Model':
                qry = "SELECT * FROM reg_phone WHERE model LIKE '" + keyword + "%'  "
                win = self.database.get_data_p(qry, keyword)

                self.aaa_tree.delete(*self.aaa_tree.get_children())
                for i in win:
                    self.aaa_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6],i[7],i[8]))
                    self.aaa_tree.bind("<Double-1>", self.select_detail)

        except Exception as e:
            print(e)


    def select_detail(self,event):
        sel_row = self.aaa_tree.selection()[0]
        self.autoindex = self.aaa_tree.item(sel_row, 'text')
        selected_data = self.aaa_tree.item(sel_row, 'values')
        self.entry_tc.delete(0, 'end')
        self.entry_tc.insert(0, selected_data[0])

        self.entry_ac.delete(0, 'end')
        self.entry_ac.insert(0, selected_data[2])

        self.entry_p.delete(0, 'end')
        self.entry_p.insert(0, selected_data[3])

        self.combox.delete(0, 'end')
        self.combox.insert(0, selected_data[4])


        self.entry_des.delete(0, 'end')
        self.entry_des.insert(0, selected_data[5])

    def store_details(self):
        self.database = DataBase()
        try:
            cusname=self.entry_tc.get()
            brand=self.entry_ac.get()
            model=self.entry_p.get()
            problem=self.entry_des.get()
            price=self.combox.get()
            billdate=self.entry_st.get()

            if cusname=='' or brand=='' or model=='' or problem=='' or price=='' or billdate=='':
                messagebox.showerror("Failed",'Enter all the entries!')

            else:
                qry='''insert into billing (customer, brand, model, problem, price, date) values(%s,%s,%s,%s,%s,%s)'''
                values=(cusname, brand, model, problem, price, billdate)
                self.database.iud(qry,values)
                messagebox.showinfo('Done','Bill stored')

        except Exception as e:
            print(e)







