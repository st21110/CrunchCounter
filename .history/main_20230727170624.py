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
        self.root.config(bg=BG_COLOR)
        self.root.attributes("-fullscreen", True)
        self.create_widgets()

    def create_widgets(self):
        welcome_label = Label(self.root, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Welcome to Crunch Counter")
        welcome_label.grid(row=0, column=1, pady=20)

        frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        frame.grid(row=1, column=1, padx=20, pady=20)

        user_info_label = Label(frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="User Info")
        user_info_label.grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(frame, text="Quit", command=self.quit).grid(row=14, column=5, columnspan=2)

        labels = ["Name:", "Age:", "Gender:", "Height:", "Weight:", "Activity:", "Email:"]
        for i, label_text in enumerate(labels):
            Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text=label_text).grid(row=i+1, column=0, sticky="w")

        self.user_name_entry = EntryWithPlaceholder(frame, "Full Name")
        self.user_name_entry.grid(row=1, column=1)

        self.age_entry = EntryWithPlaceholder(frame, "15-80")
        self.age_entry.grid(row=2, column=1)

        gender_names = [("Female"), ("Male")]
        self.gender = StringVar()
        ttk.Radiobutton(frame, text="Female", value="Female", var=self.gender, state="readonly", width=17).grid(row=3, column=1, sticky="w")
        ttk.Radiobutton(frame, text="Male", value="Male", var=self.gender, state="readonly", width=17).grid(row=3, column=2, sticky="w")

        self.height_entry = EntryWithPlaceholder(frame, "cm")
        self.height_entry.grid(row=4, column=1)

        self.weight_entry = EntryWithPlaceholder(frame, "kg")
        self.weight_entry.grid(row=5, column=1)

        activity_amount = ["Sedentary: little or no exercise", "Light: exercise 1-3 times/week",
                           "Moderate: exercise 4-5 times/week",
                           "Active: daily exercise or intense exercise 3-4 times/week",
                           "Very Active: intense exercise 6-7 times/week",
                           "Extra Active: very intense exercise daily, or physical job"]
        self.activity = StringVar()
        activity_chosen = ttk.Combobox(frame, textvariable=self.activity, values=activity_amount,
                                       state="readonly", width=30)  # readonly, so that it is uneditable
        activity_chosen.grid(row=6, column=1, columnspan=2, sticky="w")

        self.email_entry = EntryWithPlaceholder(frame, "email address")
        self.email_entry.grid(row=7, column=1, columnspan=2, sticky="w")

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
