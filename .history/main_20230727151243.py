#Author: Prisha
#Date: 24/07/23

from tkinter import *
from tkinter import ttk
from PIL import ImageTk

# GUI fonts and colors (so that it can be changed easily in the future or if I wanted to try out a new style)
BG_COLOR = "white"
HEADING_FONT = "Helvetica 15 bold"  # font size and type for headings
MAIN_HEADING_FONT = "Helvetica 35 bold"  # font size and type for headings
FG_COLOR = "#19b092"


class CrunchCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crunch Counter")  # giving root a title
        self.root.attributes("-fullscreen", True)
        self.create_widgets()
        self.photo=PhotoImage(file="./Final (Refined) Design - CSC3.png")  # background image 
        canvas1 = Canvas( root, width = 400,
                 height = 400)
        canvas1.grid(row=0, column= 0) #fill = "both", expand = True
        canvas1.create_image( 0, 0, image = bg, 
        anchor = "nw")

    def create_widgets(self):
        ttk.Button(self.root, text="Quit", command=self.quit).grid(row=13, column=5)

        labels = ["Name:", "Age:", "Gender:", "Height:", "Weight:", "Activity:", "Email:"]
        for i, label_text in enumerate(labels):
            Label(self.root, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text=label_text).grid(row=i+35, column=35)

        Label(self.root, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Welcome to Crunch Counter").grid(row=1, column=1)

        self.user_name_entry = EntryWithPlaceholder(self.root, "Full Name")
        self.user_name_entry.grid(row=4, column=3)

        self.age_entry = EntryWithPlaceholder(self.root, "15-80")
        self.age_entry.grid(row=5, column=3)

        gender_names = [("Female"), ("Male")]
        self.gender = StringVar()
        ttk.Radiobutton(self.root, text="Female", value="Female", var=self.gender, state="readonly", width=17).grid(row=6, column=3)
        ttk.Radiobutton(self.root, text="Male", value="Male", var=self.gender, state="readonly", width=17).grid(row=6, column=4)

        self.height_entry = EntryWithPlaceholder(self.root, "cm")
        self.height_entry.grid(row=7, column=3)

        self.weight_entry = EntryWithPlaceholder(self.root, "kg")
        self.weight_entry.grid(row=8, column=3)

        activity_amount = ["Sedentary: little or no exercise", "Light: exercise 1-3 times/week",
                           "Moderate: exercise 4-5 times/week",
                           "Active: daily exercise or intense exercise 3-4 times/week",
                           "Very Active: intense exercise 6-7 times/week",
                           "Extra Active: very intense exercise daily, or physical job"]
        self.activity = StringVar()
        activity_chosen = ttk.Combobox(self.root, textvariable=self.activity, values=activity_amount,
                                       state="readonly", width=25)  # readonly, so that it is uneditable
        activity_chosen.grid(row=9, column=3)

        self.email_entry = EntryWithPlaceholder(self.root, "email address")
        self.email_entry.grid(row=10, column=3)
        
    def quit(self):
        self.root.destroy()  # destroys the window

class EntryWithPlaceholder(Entry):
    def __init__(self, master, placeholder, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.insert(0, placeholder)
        self.bind("<FocusIn>", self.clear_placeholder)
        self.bind("<FocusOut>", self.restore_placeholder)

    def clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, END)

    def restore_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)


def main():
    root = Tk()
    app = CrunchCounterApp(root)
    root.resizable(False, False)  # stops window from being resized
    root.mainloop()

if __name__ == "__main__":
    main()