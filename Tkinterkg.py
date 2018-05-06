""" Using Tkinter to create a kg -> grams, US pounds,and ounces calculator """

from tkinter import *

""" Open a Tkinter GUI window """
window = Tk()


""" Defining Calculator program """
def kg_to():

    try:

        grams = float(e1_value.get()) * 1000
        pounds = float(e1_value.get()) * 2.20462
        ounces = float(e1_value.get()) * 35.274

        t1.delete("1.0", END)
        t1.insert(END,str(round(grams,2)) + ' grams')
        t2.delete("1.0", END)
        t2.insert(END,str(round(pounds,2)) + ' pounds')
        t3.delete("1.0", END)
        t3.insert(END,str(round(ounces,2)) + ' ounces')

    except ValueError:
        pass


""" Setting window placement and defining properties of each window """

l1 = Label(window, text='Input kg to convert')
l1.grid(row=0, column=0)

""" Input Window """
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

""" Button """
b1 =  Button(window, text = 'Convert', command=kg_to)
b1.grid(row=0, column=2)

""" Conversion Windows """
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
