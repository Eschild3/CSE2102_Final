import tkinter as tk
from tkinter import *
from tkinter import ttk

FONT = ("Times New Roman", 35)

# TODO: submit function
def submit()
#TODO

class orderTerminal(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Order Terminal")
        # create a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initialize frames to an empty array
        self.frames = {}

        for F in (WelcomePage, OrderPage, ConfirmPage):
            frame = F(container, self)

            # initialize the frames
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame welcomepage
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label for frame Layout 2
        label = ttk.Label(self, text="Welcome", font=FONT)

        # Place the label on the grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(OrderPage))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

    # second window frame page1


class OrderPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Place your order:", font=FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to go to back to welcome page
        button1 = ttk.Button(self, text="Previous",
                             command=lambda: controller.show_frame(WelcomePage))

        # place button1 in grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to go to next page
        button2 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(ConfirmPage))

        # place button on grid
        button2.grid(row=1, column=7, padx=10, pady=10)


#
class ConfirmPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select menu items", font=FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to take you back to page 1
        button1 = ttk.Button(self, text="Previous",
                             command=lambda: controller.show_frame(OrderPage))
        # Place button 1 on the grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to submit order
        button1 = ttk.Button(self, text="Submit",
                             command=submit)
        # Place submit button on the grid
        button1.grid(row=1, column=7, padx=10, pady=10)


    # Driver Code


app = orderTerminal()
app.mainloop()
