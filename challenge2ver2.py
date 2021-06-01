import matplotlib.pyplot as plt
import numpy as np
from math import log, cos, sin, sqrt



a = 0
b = 0
c = 0
d = 0
e = 0



def menu():
    
    """Allows user to choose which function they would like to see from the menu.
    Can make their selection by entering number.
    Also allows user to quit, and end the program"""
    
    print('''
    ---------------------------
    WELCOME TO OUR MATH PROGRAM
      Please Choose A Number
    ---------------------------''')
    print("1. Linear")
    print("2. Quadratic")
    print("3. Cubic")
    print("4. Quartic")
    print("5. Exponential")
    print("6. Logarithmic")
    print("7. Sine")
    print("8. Cos")
    print("9. Square Root")
    print("10. Cube Root")
    print("Press q to quit the program. \n")
    return input("What would you like to do? \n")

#Def to load menu
run = menu()

#Allows the saving of graphs.
fig = plt.figure()

while True:
    #Linear Input
    if run == "1":
        #Enter values for each coefficient
        print("Linear graphs are in the form of f(x) = a*x + b")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        
        #Enter a starting and ending range for graph
        range_start = float(input("Please enter the start of range: "))
        range_end = float(input("Please enter the end of range: "))
        x = np.linspace(range_start, range_end, 100)
        y = a * x + b
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*x + b')
        plt.title('Graph of y=a*x + b')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the main menu for selection
        run = menu()
    
    # Quadratic Input
    elif run == "2":
        #Enter values for each coefficient
        print("Quadratic graphs are in the form of f(x) = a*x^2 + b*x + c")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        
        #Enter a starting and ending range for graph
        range_start = float(input("Please enter the start of range: "))
        range_end = float(input("Please enter the end of range: "))
        x = np.linspace(range_start, range_end, 100)
        y = a*x**2 + b*x + c
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*x^2 + b*x + c')
        plt.title('Graph of y=a*x^2 + b*x + c')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the main menu for selection
        run = menu()
    
    #Cubic Input:
    elif run == "3":
        print("Cubic graphs are in the form of f(x) = a*x^3 + b*x^2 + c*x + d")
        
        #Enter values for each coefficient
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        d = float(input("Please enter a value for d: "))
        
        #Enter a starting and ending range for graph
        range_start = float(input("Please enter the start of range: "))
        range_end = float(input("Please enter the end of range: "))
        x = np.linspace(range_start, range_end, 100)
        y = a*x**3 + b*x**2 + c*x + d
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*x^3 + b*x^2 + c*x + d')
        plt.title('Graph of y=a*x^3 + b*x^2 + c*x + d')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
    
    #Quartic Input:
    elif run == "4":
        #Enter values for each coefficient
        print("Quartic graphs are in the form of f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        d = float(input("Please enter a value for d: "))
        e = float(input("Please enter a value for e: "))
        
        #Enter a starting and ending range for graph
        range_start = float(input("Please enter the start of range: "))
        range_end = float(input("Please enter the end of range: "))
        x = np.linspace(range_start, range_end, 100)
        y = a*x**4 + b*x**3 + c*x**2 + d*x + e
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*x^4 + b*x^3 + c*x^2 + d*x + e')
        plt.title('Graph of y=a*x^4 + b*x^3 + c*x^2 + d*x + e')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
        
    #Exponential Input:
    elif run == "5":
        #Enter values for each coefficient
        print("Exponential graphs are in the form of f(x) = a*b^(c*x + d)")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        d = float(input("Please enter a value for d: "))
        
        #Enter a starting and ending range for graph
        range_start = float(input("Please enter the start of range: "))
        range_end = float(input("Please enter the end of range: "))
        x = np.linspace(range_start, range_end, 100)
        y = a*b**(c*x + d)
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*b^(c*x + d)')
        plt.title('Graph of y=a*b^(c*x + d)')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
    
    #Logarithmic Input
    elif run == "6":
        #Enter values for each coefficient
        print("Logarithmic graphs are in the form of f(x) = a*log(b*x + c)")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        
        #Enter a starting and ending range for graph
        #Added a validation to make range = positive input so function will work
        while True:
            range_start = float(input("Please enter the start of range: "))
            if range_start < 0:
                print("please enter a positive range.")
            else:
                break
        
        while True:           
            range_end = float(input("Please enter the end of range: "))
            if range_end < 0:
                print("please enter a positive range.")
            else:
                break
            
        x = np.linspace(range_start, range_end, 100)
        y = a*np.log(b*x + c)
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*log(b*x + c)')
        plt.title('Graph of y=a*log(b*x + c)')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
        
    #Sine Input:
    elif run == "7":
        #Enter values for each coefficient
        print("Sine graphs are in the form of f(x) = a*sin(b*x + c)")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        
        #Enter a starting and ending range for graph
        #Added a validation to make range = positive input so function will work
        while True:
            range_start = float(input("Please enter the start of range: "))
            if range_start < 0:
                print("please enter a positive range.")
            else:
                break
        
        while True:           
            range_end = float(input("Please enter the end of range: "))
            if range_end < 0:
                print("please enter a positive range.")
            else:
                break
            
        x = np.linspace(range_start, range_end, 100)
        y = a*np.sin(b*x + c)
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*sin(b*x + c)')
        plt.title('Graph of y=a*sin(b*x + c)')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
        
    #Cos Input:
    elif run == "8":
        #Enter values for each coefficient
        print("Cosine graphs are in the form of f(x) = a*cos(b*x + c)")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        
        #Enter a starting and ending range for graph
        #Added a validation to make range = positive input so function will work
        while True:
            range_start = float(input("Please enter the start of range: "))
            if range_start < 0:
                print("please enter a positive range.")
            else:
                break
        
        while True:           
            range_end = float(input("Please enter the end of range: "))
            if range_end < 0:
                print("please enter a positive range.")
            else:
                break
            
        x = np.linspace(range_start, range_end, 100)
        y = a*np.cos(b*x + c)
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*cos(b*x + c)')
        plt.title('Graph of y=a*cos(b*x + c)')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
    
    #Square Root Input:
    elif run == "9":
        #Enter values for each coefficient
        print("Square Root graphs are in the form of f(x) = a*sqrt(b*x + c)")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        
        #Enter a starting and ending range for graph
        #Added a validation to make range = positive input so function will work
        while True:
            range_start = float(input("Please enter the start of range: "))
            if range_start < 0:
                print("please enter a positive range.")
            else:
                break
        
        while True:           
            range_end = float(input("Please enter the end of range: "))
            if range_end < 0:
                print("please enter a positive range.")
            else:
                break
            
        x = np.linspace(range_start, range_end, 100)
        y = a*np.sqrt(b*x + c)
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*sqrt(b*x + c)')
        plt.title('Graph of y=a*sqrt(b*x + c)')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
    
    #Cube Root Input:
    elif run == "10":
        #Enter values for each coefficient
        print("Cube Root graphs are in the form of f(x) = a*(b*x + c)^(1/3))")
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))
        
        #Enter a starting and ending range for graph
        #Added a validation to make range = positive input so function will work
        while True:
            range_start = float(input("Please enter the start of range: "))
            if range_start < 0:
                print("please enter a positive range.")
            else:
                break
        
        while True:           
            range_end = float(input("Please enter the end of range: "))
            if range_end < 0:
                print("please enter a positive range.")
            else:
                break
            
        x = np.linspace(range_start, range_end, 100)
        y = (a*(b*x + c))**(1/3)
        
        #Plot the graph, allow user to display the graph, or save the graph
        plt.plot(x, y, '-r', label='y=a*(b*x + c)^(1/3)')
        plt.title('Graph of y=a*(b*x + c)^(1/3)')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        
        #Allow the user to see the graph or save the file under a name.
        view = input("Would you like to view the graph or save it? V or S: ")
        if view.lower() == "v":
            plt.show()
        elif view.lower() == "s":
            save = input("Please enter name for file in the form [file].png : ")
            plt.savefig(f"{save}", dpi=150)
        
        #Run the menu for selection
        run = menu()
    
    #Break statement in menu Def that will end the program when q is selected.    
    elif run.lower() == "q":
            break

#Ending statement when loop is exited.        
print("Thank you for using our program!")