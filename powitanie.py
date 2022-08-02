from tkinter import *
# from tkinter import messagebox
import sys

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.inst_lbl = Label(self, text='Jak masz na imię?')
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.imie_entry = Entry(self)
        self.imie_entry.grid(row=0, column=3, columnspan=2, sticky=W)
        self.imie_bttn = Button(self, text='Wprowadź', command=self.get_imie)
        self.imie_bttn.grid(row=1, column=1, columnspan=1, sticky=W)
        self.imie_txt = Text(self, relief = FLAT, width = 20, height = 1)
        self.imie_txt.grid(row=2, column=1, columnspan=1, sticky=W)
        self.end_bttn = Button(self, text='Zakończ', command=self.koniec)
        self.end_bttn.grid(row=4, column=4, columnspan=1, sticky=E)
        self.help_bttn = Button(self, text='?', command=self.help)
        self.help_bttn.grid(row=5, column=4, columnspan=1, sticky=E)
        
    def get_imie(self):
        contents = self.imie_entry.get() # pobranie wartości z widgetu Entry
        message = "Witaj " + contents +"!"

        self.imie_txt.delete(0.0, END)
        self.imie_txt.insert(0.0, message)
        
    def koniec(self):      # funkcja zakończenia programu
        messagebox.askquestion("Confirm","Are you sure?")
        if 'yes':
            sys.exit()
        
        
        
    def help(self):
#         top = Tk()  
#         top.geometry("100x100")
        messagebox.showinfo("information","Information")
#         top.mainloop()  

root = Tk()
root.title('Powitanie')
root.geometry('300x200')

app = Application(root)

root.mainloop()

