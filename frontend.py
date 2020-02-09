from tkinter import *

from backend import Database

database = Database('books.db')

class Window(object):

    def __init__(self, window):

        self.window = window
        self.window.wm_title("Bookstore")

        #Label objects
        l1 = Label(window, text="Title")
        l1.grid(row= 0, column= 0)

        l2 = Label(window, text="Author")
        l2.grid(row= 0, column= 2)

        l3 = Label(window, text="Year")
        l3.grid(row= 1, column= 0)

        l4 = Label(window, text="ISBN")
        l4.grid(row= 1, column= 2)

        #entry objects
        self.title_value= StringVar()
        self.e1= Entry(window, textvariable=self.title_value)
        self.e1.grid(row=0, column=1)

        self.author_value= StringVar()
        self.e2= Entry(window, textvariable=self.author_value)
        self.e2.grid(row=0, column=3)

        self.year_value= StringVar()
        self.e3= Entry(window, textvariable=self.year_value)
        self.e3.grid(row=1, column=1)

        self.isbn_value= StringVar()
        self.e4= Entry(window, textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height= 6, width= 35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        #
        #
        b1= Button(window, text= 'View all', width=12,command=self.view_command) #command= from_kg
        b1.grid(row= 2, column=3) #more control on the position #, rowspan=2
        # b1.pack()
        b2= Button(window, text= 'Search entry', width=12, command=self.search_command) #command= from_kg
        b2.grid(row= 3, column=3) #more control on the position #, rowspan=2

        b3= Button(window, text= 'Add entry', width=12, command=self.add_entry) #command= from_kg
        b3.grid(row= 4, column=3) #more control on the position #, rowspan=2

        b4= Button(window, text= 'Update selected', width=12,command=self.update_entry) #command= from_kg
        b4.grid(row= 5, column=3) #more control on the position #, rowspan=2

        b5= Button(window, text= 'Delete selected', width=12, command=self.delete_entry) #command= from_kg
        b5.grid(row= 6, column=3) #more control on the position #, rowspan=2

        b6= Button(window, text= 'Close', width=12,command=window.destroy) #command= from_kg
        b6.grid(row= 7, column=3) #more control on the position #, rowspan=2


    def get_selected_row(self,event):
        try:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)

            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])

            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])

            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])

            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])

        except IndexError:
            print('List is empty, add entries')
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.list1.insert(END,row)

    def add_entry(self):
        database.insert(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))

    def delete_entry(self):
        database.delete(self.selected_tuple[0])

    def update_entry(self):
        database.update(self.selected_tuple[0],self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())


window = Tk()
Window(window)
window.mainloop()

