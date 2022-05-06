import time
from tkinter import *
from tkinter import messagebox
from datetime import datetime

from streak_database import StreakDatabase
streak_database = StreakDatabase()

streak = streak_database.get_streak_number()


class streak_counter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("480x185")
        self.root.title("Streak Counter")
        self.new_streak = streak
        self.root.configure(bg="grey")

        today = datetime.now()
        self.todate = today.strftime("%B %d %Y")
        date_label = Label(self.root, text=f"{self.todate}", font=("Impact", 15, "bold"), bg="grey", fg="black")
        date_label.place(x=5, y=5)
        self.totime = today.strftime("%H:%M:%S")
        date_label = Label(self.root, text=f"{self.totime}", font=("Impact", 15, "bold"), bg="grey", fg="black")
        date_label.place(x=420, y=5)

        enquiry_label = Label(self.root, text="DID YOU PRACTICE YOUR PYTHON TODAY?", font=("Impact", 25, "bold"), bg="grey", fg="black")
        enquiry_label.place(x=35, y=50)
        # self.enquiry = Entry(root, bg="grey")
        # self.enquiry.place(segment=15, y=45, width=470, height=35)
        # checkvalue = IntVar()

        # self.yes_check_button = Checkbutton(text="YES", variable=checkvalue, font=("Arial", 15), onvalue=True,
        # offvalue=False,  command=self.check_function) self.yes_check_button.place(segment=155, y=40)
        #
        # self.no_check_button = Checkbutton(text="NO", variable=checkvalue, font=("Arial", 15), onvalue=False,
        # offvalue=True) self.no_check_button.place(segment=255, y=40)

        yes_button = Button(self.root, command=self.yes_button_function, bd=0, text=" YESS! ", font=("Arial", 20), bg="grey", fg="black")
        yes_button.place(x=105, y=100)  # width=150, height=25

        no_button = Button(self.root, command=self.no_button_function, text=" NO :( ", bd=0, font=("Arial", 20), bg="grey", fg="black")
        no_button.place(x=285, y=100)

    def yes_button_function(self):
        if True:
            self.new_streak = streak_database.add_to_streak(self.todate, self.totime)
            messagebox.showinfo("Congratulations!", f"Congratulations!\n Your streak is {self.new_streak} DAYS!")
            time.sleep(3)
            self.root.destroy()

    def no_button_function(self):
        if True:
            self.new_streak = streak_database.streak_killed(self.todate, self.totime)
            messagebox.showinfo("Oh no!", f"Oh no!\n Your streak is {self.new_streak} days")
            time.sleep(3)
            self.root.destroy()


# an app that asks you if you've trained python today and then returns your daily python streak
# step further 1: the app runs daily at a specific time
# step further 2: the app detects when the app (python) has been opened and updates the streak counter
if __name__ == '__main__':
    root = Tk()
    obj = streak_counter(root)
    root.mainloop()
