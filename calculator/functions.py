import tkinter as t
import re


class MyApp(t.Frame):
    def __init__(self, master):
        t.Frame.__init__(self, master)
        master.title("Calculator")
        master.geometry("120x175")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.text = t.Entry(self, state='disabled')
        self.text.grid(row=0, column=0, columnspan=4)
        self.b1 = t.Button(self, command=self.one, text='1')
        self.b1.grid(row=1, column=0, columnspan=1)
        self.b2 = t.Button(self, command=self.two, text='2')
        self.b2.grid(row=1, column=1, columnspan=1)
        self.b3 = t.Button(self, command=self.three, text='3')
        self.b3.grid(row=1, column=2, columnspan=1)
        self.b16 = t.Button(self, command=self.add, text='+')
        self.b16.grid(row=1, column=3, columnspan=1)
        self.b4 = t.Button(self, command=self.four, text='4')
        self.b4.grid(row=2, column=0, columnspan=1)
        self.b5 = t.Button(self, command=self.five, text='5')
        self.b5.grid(row=2, column=1, columnspan=1)
        self.b6 = t.Button(self, command=self.six, text='6')
        self.b6.grid(row=2, column=2, columnspan=1)
        self.b17 = t.Button(self, command=self.minus, text='-')
        self.b17.grid(row=2, column=3, columnspan=1)
        self.b7 = t.Button(self, command=self.seven, text='7')
        self.b7.grid(row=3, column=0, columnspan=1)
        self.b8 = t.Button(self, command=self.eight, text='8')
        self.b8.grid(row=3, column=1, columnspan=1)
        self.b9 = t.Button(self, command=self.nine, text='9')
        self.b9.grid(row=3, column=2, columnspan=1)
        self.b18 = t.Button(self, command=self.mul, text='*')
        self.b18.grid(row=3, column=3, columnspan=1)
        self.b10 = t.Button(self, command=self.exp, text='^')
        self.b10.grid(row=4, column=0, columnspan=1)
        self.b11 = t.Button(self, command=self.zero, text='0')
        self.b11.grid(row=4, column=1, columnspan=1)
        self.b12 = t.Button(self, command=self.mod, text='%')
        self.b12.grid(row=4, column=2, columnspan=1)
        self.b13 = t.Button(self, command=self.dot, text='.')
        self.b13.grid(row=5, column=0, columnspan=1)
        self.b14 = t.Button(self, command=self.equals, text='=')
        self.b14.grid(row=5, column=1, columnspan=1)
        self.b15 = t.Button(self, command=self.can, text='C')
        self.b15.grid(row=5, column=2, columnspan=1)
        self.b19 = t.Button(self, command=self.div, text='/')
        self.b19.grid(row=5, column=3, columnspan=1)
        self.b20 = t.Button(self, command=self.history, text='History')
        self.b20.grid(row=6, column=0, columnspan=4)

    def one(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '1')
        self.text.configure(state='disabled')

    def two(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '2')
        self.text.configure(state='disabled')

    def three(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '3')
        self.text.configure(state='disabled')

    def add(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '+')
        self.text.configure(state='disabled')

    def four(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '4')
        self.text.configure(state='disabled')

    def five(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '5')
        self.text.configure(state='disabled')

    def six(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '6')
        self.text.configure(state='disabled')

    def minus(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '-')
        self.text.configure(state='disabled')

    def seven(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '7')
        self.text.configure(state='disabled')

    def eight(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '8')
        self.text.configure(state='disabled')

    def nine(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '9')
        self.text.configure(state='disabled')

    def mul(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '*')
        self.text.configure(state='disabled')

    def exp(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '^')
        self.text.configure(state='disabled')

    def zero(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '0')
        self.text.configure(state='disabled')

    def mod(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '%')
        self.text.configure(state='disabled')

    def dot(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '.')
        self.text.configure(state='disabled')

    def equals(self):
        self.text.configure(state='normal')
        n = re.findall(r"(\d\.\d)|(\d)", self.text.get())
        if len(n) > 1:
            op = re.findall(r"[^a-zA-Z0-9.]", self.text.get())
            s = str()
            i = 0
            for num in n:
                try:
                    if op[i]:
                        s += num[0] if not num[0] == '' else num[1]
                        s += ' '
                        s += op[i] if not op[i] == '^' else '**'
                        s += ' '
                        i += 1
                except IndexError:
                    s += num[0] if not num[0] == '' else num[1]
                    break
            self.text.delete(0, 'end')
            self.text.insert(0, eval(s))
            with open("history.txt", "a") as f:
                f.write(s + " = " + self.text.get() + '\n')
        else:
            self.text.delete(0, 'end')
        self.text.configure(state='disabled')

    def can(self):
        self.text.configure(state='normal')
        self.text.delete(0, 'end')
        self.text.configure(state='disabled')

    def div(self):
        self.text.configure(state='normal')
        self.text.insert(len(self.text.get()), '/')
        self.text.configure(state='disabled')

    def history(self):
        win = t.Toplevel(self)
        win.title('History')
        i = 1
        s = ''
        try:
            with open("history.txt", "r") as f:
                for line in f:
                    s += str(i) + ". " + line + '\n'
                    i += 1
        except FileNotFoundError:
            s = 'Nothing Calculated Thus Far!...'
        text = t.Text(win)
        text.insert(0.0, s)
        text.configure(state='disabled')
        text.pack()
