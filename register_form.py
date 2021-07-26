import tkinter as tk
from tkinter import *
import random
import tkinter.ttk

#import mysql connector
import mysql.connector 
db_connection = mysql.connector.connect(
    host-"localhost",
    user="root",
    password=""
)
db_cursor= db_connection.ursor(buffered=True)
#define login class
class LoginApp(tk.Tk):
    def__init__(self):
     super().__init__()
     self.title("Login")
     self.geometry("600*450+351+174")
     self.configure(bg="#000000")
     #define the elements of GUI
     self.lblHeading = tk.Label(self,text="welcome to login psge", font=("Helvetica", 16),bg="black",fg="white")
     self.lbluname = tk.Label(self,tect="Enter Username:", font=("Helvetica", 10),bg="black",fg="white")
     self.lblpasswd = tk.Label(self,text="Enter Password:", font=("Helvetica", 11),bg="black",fg="white")
     self.txtuname = tk.Entry(self,width=60)
     self.txtpasswd = tk.Entry(self,width=60, show="*")
     #define the buttons and dimensions of the elements
     self.btn_login = tk.Button(self, text="Login",font=("Helvetica", 11),bg="black",fg="white",command=self.login)
     self.btn_clear = tk.Button(self, text="Clear",font-("Helvetica",11),bg="black",fg="white",command=self.clear_form)
     self.btn_register = tk.Button(self, text="Not Member ? Register", font=("Helvetica",11),bg="black",fg="red",command=self.open_registration_window)
     self.btn_exit = tk.Button(self, text="Exit",font=("Helvetica",20),bg="black,fg="red,command=self.exit)
     self.lblHeading.place(relx=0.35, rely=0.089, height=50, width=250)
     self.lbluname.place(relx=0.235, rely=0.289, height=21, width=106)
     self.lblpasswd.place(relx=0.242, rely=0.378, height=21, width=102)
     self.txtuname.place(relx=0.417, rely=0.289, height=20, relwidth=0.273)
     self.txtpasswd.place(relx=0.417, rely=0.378, height=20, relwidth=0.273)
     self.btn_login.place(relx=0.45, rely=0.489, height=24, width=52)
     self.btn_clear.place(relx=0.54, rely=0.489, height=24, width=72)
     self.btn_register.place(relx=0.695, rely=0.489, height=24, width=175)
     self.btn_exit.place(relx=0.75, rely=0.911, height=24, width=61)


