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
     