""" Using Tkinter to create a US pound -> kilograms, tons,and ounces calculator """

from tkinter import *

""" Open a Tkinter GUI window """
window = Tk()


""" Defining Calculator program """
def pound_to():

    try:

        kilograms = float(e1_value.get()) * .453592
        tons = float(e1_value.get()) * .0005
        ounces = float(e1_value.get()) * 16

        t1.delete("1.0", END)
        t1.insert(END, str(round(kilograms, 2)) + ' kilograms')
        t2.delete("1.0", END)
        t2.insert(END, str(round(tons,5)) + ' tons')
        t3.delete("1.0", END)
        t3.insert(END, str(round(ounces, 2)) + ' ounces')

    except ValueError:
        pass


""" Setting window placement and defining properties of each window """

l1 = Label(window, text='Input pounds to convert')
l1.grid(row=0, column=0)

""" Input Window """
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

""" Button """
b1 =  Button(window, text = 'Convert', command=pound_to)
b1.grid(row=0, column=2)

""" Conversion Windows """
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
