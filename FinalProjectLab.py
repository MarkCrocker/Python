from tkinter import *
from tkinter import messagebox, simpledialog
from matplotlib import pyplot as plt

def x_range(start, end, inc):#defining a function to populate a list of x values to be used in later math functions
    '''
Description: defines a range of x values with inc being the increment of the range
Parameters:
start = x_min the lowest value on the x-axis
End = x_max the highest number on the x-axis
Returns:
A list of x values.
    '''
    l = []
    while start < end:
        l.append(start)
        start += inc
    return l

def confirm():
    if ID_var.get() and bact_var.get() and med_var.get() and morn_var.get() and even_var.get() != "":
        try:
            calcroc = ((even_var.get() / morn_var.get()) - 1)
            id = ID_var.get()
            bact_type = bact_var.get()
            med_type = med_var.get()
            morn = morn_var.get()
            evening = even_var.get()
            format = "{} - {} - {} - {} - {} - {:.2f}".format(id, bact_type, med_type, morn, evening, calcroc)
            data_listbox.insert(END, format)
        except:
            messagebox.showerror("Error","Division by zero is impossible.")
    else:
        messagebox.showerror("Error","You must enter all inputs.")

def save():
        filename = simpledialog.askstring("Save Dialog", "Please enter the name of the file:")
        if filename == None:
            return  # the user hit cancel so nothing happens
        else:
            f = open(filename, "w")
            for entry in data_listbox.get(0, END):
                f.write(entry + "\n")
            f.close()

def linear(a,x,b):
    return a * x + b

def project():
    if ID_var.get() and bact_var.get() and med_var.get() and morn_var.get() and even_var.get() != "":
        rangemin = simpledialog.askfloat("Minimum Range","Please enter starting X value for plot")
        rangemax = simpledialog.askfloat("Maximum Range","Please enter ending X value for plot")
        xrange = x_range(rangemin,rangemax,0.1)
        ys = []
        b = morn_var.get()
        a = (even_var.get() - morn_var.get()) / 12
        for x in xrange:
            ys.append(linear(a, x, b))

        plt.plot(xrange,ys)
        plt.title("Bacterial Culture " + str(ID_var.get()) + " Projection")
        plt.show()
    else:
        messagebox.showerror("Error","Please fill out all inputs to do a projection!")





#window

window = Tk()
title = window.title("Bacterial Culture Research")
window.geometry("775x220")
window.configure(bg="light grey")

#lists

bacterias = []
medicines = []

with open("bacteria.dat") as x:
    for item in x:
        item = item.replace("\n","")
        bacterias.append(item)

with open("medicine.dat") as y:
    for item in y:
        item = item.replace("\n","")
        medicines.append(item)

#variables
ID_var = IntVar()
bact_var = StringVar()
med_var = StringVar()
morn_var = IntVar()
even_var = IntVar()

#Frames
info = Frame(window)
info.grid(row=0,column=0,padx=5,pady=12,sticky="N")
info = LabelFrame(info,text="Inputs")
info.grid(row=0,column=0)
info.configure(bg="light grey")

buttonframe = Frame(window)
buttonframe.grid(row=0,column=0,padx=50,pady=165,sticky="NW")
buttonframe = LabelFrame(buttonframe,text="Controls")
buttonframe.grid(row=0,column=0)
buttonframe.configure(bg="light grey")

#Labels
ID_label = Label(info,text="ID Number:")
ID_label.grid(row=0,column=0)
ID_label.configure(bg="light grey")

bact_label = Label(info,text="Bacteria:")
bact_label.grid(row=1,column=0)
bact_label.configure(bg="light grey")

med_label = Label(info,text="Medicine:")
med_label.grid(row=2,column=0)
med_label.configure(bg="light grey")

morn_count = Label(info,text="Morning Count(6am):")
morn_count.grid(row=3,column=0)
morn_count.configure(bg="light grey")

even_count = Label(info,text="Evening Count(6pm):")
even_count.grid(row=4,column=0)
even_count.configure(bg="light grey")

data_label = Label(window,text="DATA")
data_label.grid(row=0,column=1,sticky="N")
data_label.configure(bg="light grey")

#Listbox
data_listbox = Listbox(window,width=45)
data_listbox.grid(row=0,column=1,sticky="N",pady=20)



#Entries
ID_entry = Entry(info,textvariable=ID_var)
ID_entry.grid(row=0,column=1)
ID_entry.configure(highlightbackground="light grey")

morn_entry = Entry(info,textvariable=morn_var)
morn_entry.grid(row=3,column=1)
morn_entry.configure(highlightbackground="light grey")

even_entry = Entry(info,textvariable=even_var)
even_entry.grid(row=4,column=1)
even_entry.configure(highlightbackground="light grey")

#option menus
bacteriadropdown = OptionMenu(info,bact_var,*bacterias)
bacteriadropdown.grid(row=1,column=1)
bacteriadropdown.configure(bg="light grey",highlightbackground="light grey")

medicinedropdown = OptionMenu(info,med_var,*medicines)
medicinedropdown.grid(row=2,column=1)
medicinedropdown.configure(bg="light grey",highlightbackground="light grey")

#buttons
confirm = Button(buttonframe,text="Confirm",command=confirm)
confirm.grid(row=0,column=0)
confirm.configure(highlightbackground="light grey")

save = Button(buttonframe,text="Save",command=save)
save.grid(row=0,column=1)
save.configure(highlightbackground="light grey")

projection = Button(buttonframe,text="Linear Projection",command=project)
projection.grid(row=0,column=2)
projection.configure(highlightbackground="light grey")

exit_button = Button(buttonframe,text="Exit",command=window.destroy)
exit_button.grid(row=0,column=3)
exit_button.configure(highlightbackground="light grey")




window.mainloop()