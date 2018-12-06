# import sys
# import os
# from tkinter import *
#
# window=Tk()
#
# window.title("Running Python Script")
# window.geometry('550x200')
#
# def run():
#     os.system('python Server.py')
#
# btn = Button(window, text="Run Server", bg="black", fg="white",command=run)
# btn.grid(column=0, row=0)
#
# window.mainloop()

# import tkinter
# from tkinter import messagebox
#
# top = tkinter.Tk()
#
# def helloCallBack():
#    messagebox.showinfo( "Hello Python", "Hello World")
#
# B = tkinter.Button(top, text ="Hello", command = helloCallBack)
#
# B.pack()
# top.mainloop()

# import tkinter as tk
#
# def write_slogan():
#     print("Tkinter is easy to use!")
#
# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()
#
# button = tk.Button(frame,
#                    text="QUIT",
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Hello",
#                    command=write_slogan)
# slogan.pack(side=tk.LEFT)
#
# root.mainloop()

#!/usr/bin/python
#!/usr/bin/env python
import sys
import os
import tkinter as tk

root = tk.Tk()

def helloServer():
    os.system(r'C:\Users\okyereforsonr\Desktop\Server.py')

def helloClient():
    os.system(r'C:\Users\okyereforsonr\Desktop\Client.py')

#Keep_both_files_in_the_same_Folder
b1=tk.Button(root, text="SERVER",bg="white",command=helloServer)
b2=tk.Button(root, text="CLIENT",bg="white",command=helloClient)
b1.pack()
b2.pack()
root.mainloop()
