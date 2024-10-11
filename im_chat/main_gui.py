import tkinter as tk
from tkinter import StringVar, ttk
from client import send, client_rec
import random

#fucns

def submit_msg():
    try:
        msg = input1.get()
        input1.delete(0, tk.END)
        send(msg)
        reply = client_rec()
        v.set(reply)
        my_tree.insert(parent="", index="end", iid=random.randrange(start=1, stop=3000), text="", values=(reply,))
    except:
        pass


    



root = tk.Tk()
root.geometry("600x600")

frame1 = tk.Frame(root)

my_tree = ttk.Treeview(frame1)

my_tree["columns"] = ("msg")

my_tree.column("#0", width=0, stretch="no")
my_tree.column("msg", anchor="w", minwidth=25,  width=120)

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("msg", text="Messages", anchor="w")

my_tree.pack()


v = StringVar()
l = tk.Label(frame1, textvariable=v).pack()
v.set("Server Msg")


input1 = tk.Entry(frame1, width=20)
input1.pack()
btn = tk.Button(frame1, text="Send", command=submit_msg).pack()

frame1.pack(anchor="center")






root.mainloop()