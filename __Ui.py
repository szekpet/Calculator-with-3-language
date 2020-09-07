from tkinter import Tk, W, E, StringVar
from tkinter.ttk import Frame, Button, Entry, Style, OptionMenu
from .__Config import Config


class UI(Frame):

    def __init__(self):
        self.lang = Config()
        self.tk = Tk()
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title(self.lang.GetValueByLanguage('cim'))
        style = Style()
        style.configure('TButton', padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.entry1 = Entry(self)  
        self.entry1.grid(row=0, columnspan=4, sticky=W)
        self.entry = Entry(self)  # BEVITELI MEZO
        self.entry.grid(row=1, columnspan=4, sticky=W + E)
        

        self.c = Button(self, text=self.lang.GetValueByLanguage('cls'),
                        command=lambda: self.makeOperation('cls'))
        self.c.grid(row=2, column=0)
        self.bck = Button(self, text=self.lang.GetValueByLanguage('back'),
                          command=lambda: self.makeOperation('back'))
        self.bck.grid(row=2, column=1)
        lbl = Button(self, text='%',
                     command=self.percent)
        lbl.grid(row=2, column=2)
        self.close = Button(self, text=self.lang.GetValueByLanguage('close'),
                            command=quit)
        self.close.grid(row=2, column=3)

        het = Button(self, text='7',
                     command=lambda: self.makeOperation(7))
        het.grid(row=3, column=0)
        nyolc = Button(
            self, text='8', command=lambda: self.makeOperation(8))
        nyolc.grid(row=3, column=1)
        kilenc = Button(
            self, text='9', command=lambda: self.makeOperation(9))
        kilenc.grid(row=3, column=2)
        per = Button(self, text='/',
                     command=self.div)
        per.grid(row=3, column=3)

        negy = Button(self, text='4',
                      command=lambda: self.makeOperation(4))
        negy.grid(row=4, column=0)
        ot = Button(self, text='5',
                    command=lambda: self.makeOperation(5))
        ot.grid(row=4, column=1)
        hat = Button(self, text='6',
                     command=lambda: self.makeOperation(6))
        hat.grid(row=4, column=2)
        szor = Button(self, text='*',
                      command=self.dupl)
        szor.grid(row=4, column=3)

        egy = Button(self, text='1',
                     command=lambda: self.makeOperation(1))
        egy.grid(row=5, column=0)
        ketto = Button(
            self, text='2', command=lambda: self.makeOperation(2))
        ketto.grid(row=5, column=1)
        harom = Button(
            self, text='3', command=lambda: self.makeOperation(3))
        harom.grid(row=5, column=2)
        minusz = Button(
            self, text='-', command=self.minus)
        minusz.grid(row=5, column=3)

        potty = Button(
            self, text='.', command=self.floating)
        potty.grid(row=6, column=0)
        nulla = Button(
            self, text='0', command=lambda: self.makeOperation(0))
        nulla.grid(row=6, column=1)
        egyenlo = Button(
            self, text='=', command=self.equal)
        egyenlo.grid(row=6, column=2)
        plusz = Button(
            self, text='+', command=self.plus)
        plusz.grid(row=6, column=3)

        alap = StringVar()
        alap.set(self.lang.user)
        nyelv = OptionMenu(self, alap,
                           *(self.lang.GetAvailabeLanguages()), command=self.GetSelectedLanguage)
        nyelv.grid(row=7, columnspan=4, sticky=W + E)

        self.pack()
    def plus(self):
        first_num=self.entry.get()
        c_req=self.entry1.get()
        global e_num
        global enumerate
        e_num=float(first_num)
        enumerate='+'
        self.entry.delete(0, len(first_num))
        self.entry1.delete(0, len(c_req))
        deq=[e_num,'+']
        self.entry1.insert(0,deq)
        return
    
    def minus(self):
        first_num=self.entry.get()
        c_req=self.entry1.get()
        global e_num
        global enumerate
        e_num=float(first_num)
        enumerate='-'
        self.entry.delete(0, len(first_num))
        self.entry1.delete(0, len(c_req))
        deq=[e_num,'-']
        self.entry1.insert(0,deq)
        return

    def dupl(self):
        first_num=self.entry.get()
        c_req=self.entry1.get()
        global e_num
        global enumerate
        e_num=float(first_num)
        enumerate='*'
        self.entry.delete(0, len(first_num))
        self.entry1.delete(0, len(c_req))
        deq=[e_num,'x']
        self.entry1.insert(0,deq)
        return
    
    def div(self):
        first_num=self.entry.get()
        c_req=self.entry1.get()
        global e_num
        global enumerate
        e_num=float(first_num)
        enumerate='/'
        self.entry.delete(0, len(first_num))
        self.entry1.delete(0, len(c_req))
        deq=[e_num,'/']
        self.entry1.insert(0,deq)
        return

    def percent(self):
        c_req=self.entry1.get()
        first_num=self.entry.get()
        global e_num
        global enumerate
        e_num=float(first_num)
        enumerate='%'
        self.entry.delete(0, len(first_num))
        self.entry1.delete(0, len(c_req))
        deq=[e_num,'%']
        self.entry1.insert(0,deq)
        return
    def floating(self):
        first_num=self.entry.get()
        self.entry.delete(0, len(first_num))
        self.entry.insert(0,first_num+'.')
        return
    
    def equal(self):
        s_num=self.entry.get()
        s_num1=self.entry1.get()
        sec_num=float(s_num)
        self.entry.delete(0, len(s_num))
        self.entry1.delete(0, len(s_num1))
        if enumerate=='/':
            eq=e_num/sec_num
            
        elif enumerate=='+':
            eq=e_num+sec_num
            
        elif enumerate=='-':
            eq=e_num-sec_num
            
        elif enumerate=='*':
            eq=e_num*sec_num
        
        elif enumerate=='%':
            eq=(e_num*sec_num)/100
        res=[e_num, enumerate,sec_num]
        self.entry1.insert(0,res)
        self.entry.insert(0,eq)
    

        

    def GetSelectedLanguage(self, value):
        self.lang.setValue('user', value)
        self.master.title(self.lang.GetValueByLanguage('cim'))
        self.c.configure(text=self.lang.GetValueByLanguage('cls'))
        self.bck.configure(text=self.lang.GetValueByLanguage('back'))
        self.close.configure(text=self.lang.GetValueByLanguage('close'))
        return

    def makeOperation(self, operation):
        print(operation)
        if type(operation) is int:  
            benne_van = self.entry.get().strip()
            self.entry.delete(0, len(benne_van))
            self.entry.insert(0, benne_van+str(operation))
        elif type(operation) is str:
            if operation == 'back': 
                self.entry.delete(
                    len(self.entry.get()) - 1,
                    len(self.entry.get())
                )
            if operation == 'cls': 
                self.entry.delete(
                    self.entry.delete(0, len(self.entry.get()))
                )
        return

    def runUI(self):
        self.mainloop()
