import tkinter as tk
from tkinter import StringVar
from client import send, client_rec

#fucns

def submit_msg():
    msg = input1.get()
    input1.delete(0, tk.END)
    send(msg)
    v.set(client_rec())


    



root = tk.Tk()
root.geometry("600x600")

frame1 = tk.Frame(root)


v = StringVar()
l = tk.Label(frame1, textvariable=v).pack()
v.set("Server Msg")


input1 = tk.Entry(frame1, width=20)
input1.pack()
btn = tk.Button(frame1, text="Send", command=submit_msg).pack()

frame1.pack()






root.mainloop()