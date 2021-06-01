import tkinter as tk


#window now has all the properties of tkinter
window = tk.Tk()

# title of label
window.title("My APP")

# size of window
window.geometry("400x350")

# LABELS
title = tk.Label(text="Hello world. \nWelcome to my app", font=("Garamond", 20))
title.grid()

# Entry field
entry_field = tk.Entry()
entry_field.grid()

# BUTTON
button1 = tk.Button(text="Click me!", bg="blue")
button1.grid()

# Text fields
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

# mainloop runs everything inside the window.
window.mainloop()


