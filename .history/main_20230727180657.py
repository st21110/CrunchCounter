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
        # Create a frame for the welcome label with the same color and borders as the user input frame
        welcome_frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        welcome_frame.place(x=100, y=50, width=500, height=210)

        welcome_label = Label(welcome_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Welcome\nto\nCrunch Counter")
        welcome_label.pack(pady=20)

        #Create frame for disclaimer
        disclaimer_frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        disclaimer_frame.place(x=100, y=300, width=500, height=410)

        disclaimer_label = Label(disclaimer_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Welcome\nto\nCrunch Counter")
        disclaimer_label.pack(pady=20)

        # Create the user input frame
        frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        frame.place(x=700, y=250)  # Adjust the x and y coordinates to position the frame

        user_info_label = Label(frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="User Info")
        user_info_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        labels = ["Name:", "Age:", "Gender:", "Height:", "Weight:", "Activity:", "Email:"]
        for i, label_text in enumerate(labels):
            Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text=label_text).grid(row=i+1, column=0, sticky="w")

        self.user_name_entry = EntryWithPlaceholder(frame, "Full Name")
        self.user_name_entry.grid(row=1, column=1, sticky="w")

        ages = [str(age) for age in range(15, 81)]
        self.age = StringVar()
        age_chosen = ttk.Combobox(frame, textvariable=self.age, values=ages, state="readonly", width=5)  # readonly, so that it is uneditable
        age_chosen.grid(row=2, column=1, sticky="w")

        gender_names = [("Female"), ("Male")]
        self.gender = StringVar()
        style = ttk.Style()
        style.configure("TRadiobutton", background=BG_COLOR)
        ttk.Radiobutton(frame, text="Female", value="Female", var=self.gender, state="readonly", width=17, style="TRadiobutton").grid(row=3, column=1, sticky="w")
        ttk.Radiobutton(frame, text="Male", value="Male", var=self.gender, state="readonly", width=17, style="TRadiobutton").grid(row=3, column=2, sticky="w")

        self.height_entry = EntryWithPlaceholder(frame, "cm")
        self.height_entry.grid(row=4, column=1, sticky="w")

        self.weight_entry = EntryWithPlaceholder(frame, "kg")
        self.weight_entry.grid(row=5, column=1, sticky="w")

        activity_amount = ["Sedentary: little or no exercise", "Light: exercise 1-3 times/week",
                           "Moderate: exercise 4-5 times/week",
                           "Active: daily exercise or intense exercise 3-4 times/week",
                           "Very Active: intense exercise 6-7 times/week",
                           "Extra Active: very intense exercise daily, or physical job"]
        self.activity = StringVar()
        activity_chosen = ttk.Combobox(frame, textvariable=self.activity, values=activity_amount,
                                       state="readonly", width=47)  # Adjust the width to fit the text
        activity_chosen.grid(row=6, column=1, columnspan=2, sticky="w")

        self.email_entry = EntryWithPlaceholder(frame, "email address")
        self.email_entry.grid(row=7, column=1, columnspan=2, sticky="w")

        calculate_button = Button(frame, text="Calculate", font=HEADING_FONT, fg=FG_COLOR, bg="white", command=self.calculate)
        calculate_button.grid(row=8, column=0, columnspan=2, pady=10, sticky="e")

        quit_button = Button(self.root, text="Quit", font=HEADING_FONT, fg=FG_COLOR, bg="white", command=self.quit)
        quit_button.place(x=1200, y=20)

    def calculate(self):
        # Add your calculation logic here (to be implemented)
        pass

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