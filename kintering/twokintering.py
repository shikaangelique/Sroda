from tkinter import *
from tkinter import messagebox
import time


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1000x600+200+180")
        # self.root.resizable(False, False)
        # self.root.configure(bg='grey')  # background color

        # for background image file
        self.bg = PhotoImage(file='dreamthat.png')  # if file is .png
        # self.bg=ImageTkPhotoImage(file='filename') #if file is .jpg Import PIL required
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #login frame
        frame_login = Frame(self.root, bg="grey")
        frame_login.place(x=265, y =105, width=500, height=400)
        # frame_login.attributes('-alpha', 0.7)

        title = Label(frame_login, text="Enter Dets", font=("Impact", 35, "bold"), fg="white", bg="grey")
        title.place(x=170, y=30)

        subtitle = Label(frame_login, text="Verification for Locked Folder", font=("Impact", 20, "bold"), fg="white", bg="grey")
        subtitle.place(x=132, y=70)

        username_label = Label(frame_login, text="Username", font=("Impact", 20, "bold"), fg="white", bg="grey")
        username_label.place(x=15, y=115 )
        self.username = Entry(frame_login, bg="white")
        self.username.place(x=15, y=145, width=470, height=35)

        password_label = Label(frame_login, text="Password", font=("Impact", 20, "bold italic"), fg="white", bg="grey")
        password_label.place(x=15, y=195)
        self.password = Entry(frame_login, bg="white", show='*')
        self.password.place(x=15, y=225, width=470, height=35)

        spell_label = Label(frame_login, text="Nox", font=("Impact", 20, "bold italic"), fg="white", bg="grey")
        spell_label.place(x=15, y=275)
        self.spell = Entry(frame_login, bg="white")
        self.spell.place(x=15, y=305, width=470, height=35)

        # Forgot & Submit button
        forgot = Button(frame_login, command=self.forgot_password, bd=0, text="Can't Remember?", font=("Arial", 15), bg= "white", fg= "grey", cursor="hand2")
        forgot.place(x=65, y=360)  # width=150, height=25

        submit = Button(frame_login, command=self.check_function, text="Alohomora!", bd=0, font=("Arial", 15), bg="white", fg="grey", cursor="hand2")
        submit.place(x=285, y=360)  # width=150, height=25

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "" or self.spell.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() != "sheeks" or self.password.get() != "akpa" or self.spell.get() != "lumos":
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
            time.sleep(2)
            self.root.destroy()

    def forgot_password(self):
        # messagebox.showinfo("Weird", "Answer the secret question to review the password.")
        messagebox.showinfo("Weird", "Weird.\n Can't help you.")
        time.sleep(2)
        self.root.destroy()

        # bloop = Tk()
        # bloop.geometry("350x150")
        # bloop.title("Reset password?")
        #
        # messie = Label(bloop, text="Who went into the whomping willow first?")
        # messie.grid(row=9, column=1)
        #
        # reset_key = Entry(bloop, bg='grey')
        # reset_key.grid(row= 10, column=1)
        #
        # if reset_key.get() == 'Padfoot':
        #     messagebox.showinfo("Alrightie!", "Your password is: 'akpa'")
        # else:
        #     messagebox.showerror("Error", "Just stop :/")









    # def data_fields(self,*args):
    #     self.wee = Label(root, text="Wagymimi?")


root = Tk()
obj = Login(root)
root.mainloop()
