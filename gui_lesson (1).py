import tkinter

window = tkinter.Tk()
window.title("Greeting App")

input_text_var = tkinter.StringVar()
output_text_var = tkinter.StringVar()

def generate_greeting():
    name = input_text_var.get()
    output_text_var.set("Hello {}!".format(name)) 


label = tkinter.Label(window, text="Please enter your name in the textbox below:")
label.grid(row=0, column=0)

text_input = tkinter.Entry(window, textvariable=input_text_var) #This will force any text entered into the textbox to be assigned to text_var.
text_input.grid(row=1, column=0)

button = tkinter.Button(window, text="Generate Greeting!", command=generate_greeting) #This will cause the generate_greeting function to be run when the button is clicked!
button.grid(row=2, column=0)

output_label = tkinter.Label(window, textvariable=output_text_var) #When we call output_text_var.set() it will automatically update the label text!
output_label.grid(row=4, column=0)

window.mainloop()