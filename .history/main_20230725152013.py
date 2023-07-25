#Author: Prisha
#Date: 24/07/23

from tkinter import *
from tkinter import ttk

#GUI fonts and colours (so that it can be changed easily in the future or if I wanted to try out a new style)
bg_colour = "White" #background colour
heading_font = "Helvetica 10 bold" #font size and type for headings
fg_colour = "aquamarine"

#Root settings
root = Tk() #naming root
root.title("Crunch Counter") #giving root a title
root.config(bg=bg_colour) #background colour of window

#Labels for entries
Label(root, fg=(fg_colour), font=(heading_font), text="Name:",bg=bg_colour).grid(row=4,column=2)
Label(root, fg=(fg_colour), font=(heading_font), text="Age:",bg=bg_colour).grid(row=5,column=2)
Label(root, fg=(fg_colour), font=(heading_font), text="Gender:",bg=bg_colour).grid(row=6,column=2)
Label(root, fg=(fg_colour), font=(heading_font), text="Height:",bg=bg_colour).grid(row=7,column=2)
Label(root, fg=(fg_colour), font=(heading_font), text="Weight:",bg=bg_colour).grid(row=8,column=2)
Label(root, fg=(fg_colour), font=(heading_font), text="Activity:",bg=bg_colour).grid(row=9,column=2)
Label(root, fg=(fg_colour), font=(heading_font), text="Email:",bg=bg_colour).grid(row=10,column=2)

#Entries
#User Name
user_name = ttk.Entry(root)
user_name.grid(row=4,column=3) #placement

#Age
age = ttk.Entry(root)
age.grid(row=5,column=3) #placement

#Gender
gender_names = [("Female"),("Male")]
gender=StringVar()
gender_chosen = ttk.Radiobutton(root, text="Female", value="Female",var=gender,state = "readonly",width=17).grid(row=6, column=3)
ttk.Radiobutton(root, text="Male", value="Male",var=gender,state = "readonly",width=17).grid(row=6, column=4) #readonly, so that it is uneditable

#Height
height = ttk.Entry(root)
height.grid(row=7,column=3) #placement

#Weight
weight = ttk.Entry(root)
weight.grid(row=8,column=3) #placement

#Activity
activity_amount = ["Sedentary: little or no exercise","Light: exercise 1-3 times/week",
                   "Moderate: exercise 4-5 times/week",
                   "Active: daily exercise or intense exercise 3-4 times/week",
                   "Very Active: intense exercise 6-7 times/week",
                   "Extra Active: very intense exercise daily, or physical job"]
activity=StringVar()
activity_chosen = ttk.Combobox(root, textvariable = activity, values =(activity_amount), #comobobox that has values with a list
state = "readonly",width=25) #readonly, so that it is uneditable
activity_chosen.grid(row=9, column=3) #placement

#Email
email = ttk.Entry(root)
email.grid(row=10,column=3) #placement


def entrybox_text():

    user_name.insert(0, "Full Name") #text inside entry box
    def temp_text(e): #function to delete text in entry box
        (user_name).delete(0,END)
    user_name.bind("<FocusIn>", temp_text) #deletes the temporary text once clicked on

    age.insert(0, "15-80") #text inside entry box
    def temp_text2(e): #function to delete text in entry box
        (age).delete(0,END)
    age.bind("<FocusIn>", temp_text2) #deletes the temporary text once clicked on

    height.insert(0, "cm") #text inside entry box
    def temp_text3(e): #function to delete text in entry box
        (height).delete(0,END)
    height.bind("<FocusIn>", temp_text3) #deletes the temporary text once clicked on

    weight.insert(0, "kg") #text inside entry box
    def temp_text4(e): #function to delete text in entry box
        (weight).delete(0,END)
    weight.bind("<FocusIn>", temp_text4) #deletes the temporary text once clicked on

    email.insert(0, "email address") #text inside entry box
    def temp_text4(e): #function to delete text in entry box
        (weight).delete(0,END)
    weight.bind("<FocusIn>", temp_text4) #deletes the temporary text once clicked on


def main():
    global root #global variables used
    entrybox_text() #inserts entrybox text on startup
    customer_details = [] #creates empty list for customer details and empty variable for entries in the list
    total_entries = 0
    root.resizable(False, False) #stops window from being resized
    root.mainloop()
main()
