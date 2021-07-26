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