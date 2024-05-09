from tkinter import *
import tkinter as tk    
from PIL import Image
from tkinter import ttk
import importlib
from API import responseList



query = []

#Adds input(s) to query
def addQuery():
    print(entry.get())
    query.append(entry_text.get())
    output_string.set(query)
#Window
window = tk.Tk()
window.title("VirusTotal Native")
window.geometry('800x500')
window.config(bg= '#5a45ff')
#----------------Title----------------
title_label = ttk.Label(master= window, text = 'VirusTotal Native Application', font = 'Calibri 34 bold')
title_label.pack(pady= 10)
#----------------Input field----------------
input_frame = ttk.Frame(master= window)
entry_text = tk.StringVar()
entry = ttk.Entry(master= input_frame, textvariable=entry_text)
button = ttk.Button(master= input_frame, text= 'Upload', command= addQuery) # Dont place () after since the function is called via the button
side_text = ttk.Label(master=input_frame, text= 'Insert Link')
side_text.pack(side= 'left', padx= 5)
entry.pack(side= 'left', padx= 10)
button.pack(side= 'left', pady= 20)
input_frame.pack()
#----------------Output field----------------
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text= 'Output', 
    font= 'Calibri 12 bold', 
    textvariable= output_string)
output_label.pack()
#run
window.mainloop()


x = responseList



