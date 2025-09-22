from tkinter import *

root = Tk()
root.geometry("450x300")
root.title("Login")

user_name = Label(root, text="Username: ").place(x=40, y=60)

user_password = Label(root, text="PassWord: ").place(x=40, y=100)

user_name_entry = Entry(root)
user_name_entry(x=150, y=60)

user_password_entry = Entry(root)
user_password_entry(x=150, y=100)

root.mainloop()