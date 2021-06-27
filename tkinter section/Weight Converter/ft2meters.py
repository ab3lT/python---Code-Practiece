from tkinter import *
from tkinter import ttk

"""
The first line:-<<'from tkinter import *'>> - Imports all modules in the Tkinter library -- This is a standard binding to TK which when loaded also causes existing TK library on you system to be loaded.
The second module, which is 'ttk', is pythons binding to the newer themed widgets that were added on Tkinter version 8.5.
The difference between the two is that with tkinter(first line), you can configure the widgets almost as you like whereas the second one, ttk, is more of locked down but its more professional.
So if you want a more professional looking widget or theme and you don't want to configure it down, then TTK is the way to go. But if you want to have more control when configuring your widget then use the widget
with in the tkinter module. 
Notice that everything is imported from Tkinter module on the first line so that we can call the tkinter functions and every other thing that is related to that module. So you can call them without prefixing them
which is the practice for the standard tkinter library. However, because we have imported ttk itself, we will need to prefix anything inside that ttk module. So for example,if we are using like an Entry module and
that Entry module is from the ttk library, then we need to invoke the function from the ttk library by specifying/calling it as >>>ttk.entry(arg1,arg2))

"""


def calculate(*args):  # The value "*args" is used when you are not sure the number of arguments that will pass through the function
    """ The calculate() method does the conversion from meter
    to feet when the user hit the Calculate button or ['ValueError'] hit enter
    or else hit the return key."""
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
# We are setting up the main window for the application
root.title("Feet to Meters")
# We are assigning a title to the created main window.
mainframe = ttk.Frame(root, padding="3 3 12 12")
# ttk.Frame is the frame widget and it will hold all the contents of our user interface.
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
"""The sticky option determines how to distribute any extra space within the cell that is not taken up by the widget. If you do not provide
a sticky attribute, the default behaviour of the sticky attribute will center the widget in the cell. You can position the widget in a corner
of the cell by using the sticky word and it has certain values. These values of the sticky attribute refers to the way you make the widget stick in the cell.
   That is in a way such as:
    > The sticky values N,W refers to Top-Left of the screen or the window i.e. N and W stands for North and W stands for West respectively.
    > E refers to the right corner of the widget i.e. E stands for East
    > S will stretch the widget down in the vertical position and that S stands for South.
So that's what these Geometric Values stands for and they are all parts of the grid method. """
mainframe.columnconfigure(0, weight=1)
# The 'columnconfigure()' tells tk that if main window resized, the frame should expand to take up the extra space.
mainframe.rowconfigure(0, weight=1)
"""The 'rowconfigure()' it will configure the row into which you want to configure. The row number is basically the row into which you want to insert your widget. Default counting starts from 0 default is the
next higher value for the unoccupied value."""

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  # This is where the number of feet will be entered.
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))  # A Label where we will put the resulting number of feet
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)  # This is where we will do the calculation to change feet in to meters.

# When we create widgets they do not show up automatically on the screen. Because TK doesn't know how you want them placed in relative to other methods. This is where the grid method comes up.

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)  # A Label where we will put the resulting number of feet
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)  # A Label where we will put the resulting number of feet
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)  # A Label where we will put the resulting number of feet

for child in mainframe.winfo_children():  # This for loop walks through all the widgets that are children of our content frame ...
    child.grid_configure(padx=5, pady=5)  # ... and then adds a little bit of padding so those widgets will not squashed up together.

feet_entry.focus()  # This line of code basically tells tk to put the focus on our entry widget that way the cursor will start in that field. Best to do it this way so the user doesn't have to click it to start typing
root.bind('<Return>', calculate)  # If the user presses the Return key anyway with in the root window that should call our calculate routine

root.mainloop()  # This mainloop() event is what keeps the application running until the application is closed. It is what controls the events that occur within the application.
