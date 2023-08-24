#Author: Prisha


#imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
from datetime import datetime

#Fonts and colours
BG_COLOR = "white" #background
HEADING_FONT = "Helvetica 25 bold"
SMALL_FONT = "Helvetica 15 bold"
MAIN_HEADING_FONT = "Helvetica 35 bold"  
input_box_font = "Helvetica 12" 
CAL_FONT = "Helvetica 60 bold" 
FG_COLOR = "#19b092" #text colour (teal)

class CrunchCounterApp: #create class for app
    def __init__(self, root):
        self.root = root
        self.root.title("Crunch Counter")
        self.root.config(bg=BG_COLOR)
        self.root.attributes("-fullscreen", True)
        self.create_frames()

    def create_frames(self):
        self.current_frame = None
        self.home_frame = Frame(self.root, bg=BG_COLOR)
        self.user_info_frame = Frame(self.root, bg=BG_COLOR)
        self.get_started_frame = Frame(self.root, bg=BG_COLOR)

        self.create_home_frame()

        self.current_frame = self.home_frame
        self.current_frame.pack(fill="both", expand=True)

    def create_home_frame(self): #page 1 (welcome, disclaimer & user inputs)

        #top line labels
        crunch_label = Label(fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.root, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)

        # Create a frame for the welcome label with the same color and borders as the user input frame
        welcome_frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        welcome_frame.place(x=60, y=100, width=500, height=210)

        welcome_label = Label(welcome_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Welcome\nto\nCrunch Counter")
        welcome_label.pack(pady=20)

        #Create frame for disclaimer
        disclaimer_frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        disclaimer_frame.place(x=60, y=350, width=500, height=350)

        disclaimer_label = Label(disclaimer_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Disclaimer")
        disclaimer_label.pack(pady=20)

        disclaimer_label1 = Label(disclaimer_frame, fg=FG_COLOR, font=SMALL_FONT, bg=BG_COLOR, text="Our calorie counting app is designed\nfor informational purposes only and\nshould not be considered medical advice.\n\nFor personalised guidance, please consult a\nqualified healthcare professional or dietician.")
        disclaimer_label1.pack(pady=30)

        # Create the user input frame
        frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        frame.place(x=700, y=100, width=500, height= 600) # Adjust the x and y coordinates to position the frame

        user_info_label = Label(frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="User Info")
        user_info_label.place(x=150, y=5)
        
        #space holding labels
        Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="").grid(row=1, column=1, sticky="w")
        Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="").grid(row=2, column=2, sticky="w")
        Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="").grid(row=4, column=3, sticky="w")

        #prints labels
        labels = ["Name:", "Age:", "Gender:", "Height:", "Weight:", "Activity:", "Email:"]
        for i, label_text in enumerate(labels):
            Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text=label_text).grid(row=i+4, column=0, sticky="w")

        #Entries
        self.user_name_entry = EntryWithPlaceholder(frame, "Full Name", font=input_box_font)
        self.user_name_entry.grid(row=4, column=1, sticky="w")

        ages = [str(age) for age in range(15, 81)]
        self.age = StringVar()
        age_chosen = ttk.Combobox(frame, textvariable=self.age, values=ages, state="readonly", width=5, font=input_box_font)  # readonly, so that it is uneditable
        age_chosen.grid(row=5, column=1, sticky="w")

        gender_names = [("Male"), ("Female")]
        self.gender = StringVar()
        style = ttk.Style()
        style.configure("TRadiobutton", background=BG_COLOR, font="Helvetica 15")
        ttk.Radiobutton(frame, text="Male", value="Male", var=self.gender, state="readonly", width=6, style="TRadiobutton").grid(row=6, column=1, sticky="w")
        ttk.Radiobutton(frame, text="Female", value="Female", var=self.gender, state="readonly", width=6, style="TRadiobutton").place(x = 250, y = 184)

        self.height_entry = EntryWithPlaceholder(frame, "cm", font=input_box_font)
        self.height_entry.grid(row=7, column=1, sticky="w")

        self.weight_entry = EntryWithPlaceholder(frame, "kg", font=input_box_font)
        self.weight_entry.grid(row=8, column=1, sticky="w")

        activity_amount = ["Sedentary: little or no exercise", "Light: exercise 1-3 times/week",
                           "Moderate: exercise 4-5 times/week",
                           "Active: daily exercise or intense exercise 3-4 times/week",
                           "Very Active: intense exercise 6-7 times/week",
                           "Extra Active: very intense exercise daily, or physical job"]
        self.activity = StringVar()
        activity_chosen = ttk.Combobox(frame, textvariable=self.activity, values=activity_amount,
                                       state="readonly", width=32, font=input_box_font)
        activity_chosen.grid(row=9, column=1, columnspan=2, sticky="w")

        self.email_entry = EntryWithPlaceholder(frame, "email address", font=input_box_font)
        self.email_entry.grid(row=10, column=1, columnspan=2, sticky="w")

        self.result_label = Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="")
        self.result_label.grid(row=14, column=0, columnspan=2, pady=10, sticky="e")

        calculate_button = Button(frame, text="Calculate !", font="Helvetica 20 bold", fg=FG_COLOR, bg=BG_COLOR, command=lambda: self.calculate())
        calculate_button.grid(row=11, column=1, sticky="w", pady=10)

        quit_button = Button(self.root, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.root.quit)
        quit_button.place(x=1200, y=15)


    def create_user_info_frame(self, name, calorie_intake):

        #quit button and top line labels
        quit_button = Button(self.user_info_frame, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.user_info_frame.destroy)
        quit_button.place(x=1200, y=15)

        crunch_label = Label(self.user_info_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.user_info_frame, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)

        # Create a frame to display calorie intake number
        calorie_frame = Frame(self.user_info_frame, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        calorie_frame.place(x=700, y=200, width=550, height=320)

        # Display user's name and recommended calorie intake outside the calorie frame

        result_label = Label(self.user_info_frame, text=f"{name}'s\nRecommended\nCalorie Intake\n(Per Day):", font=CAL_FONT, fg=FG_COLOR, bg=BG_COLOR)
        result_label.place(x=20, y=200)

        calorie_number_label = Label(calorie_frame, text=f"{round(calorie_intake)}kcal", font=CAL_FONT, fg=FG_COLOR, bg=BG_COLOR)
        calorie_number_label.pack(padx=50, pady=100)

        get_started_button = Button(self.user_info_frame, text="Get Started ➭", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.switch_to_get_started)
        get_started_button.place(x=1100, y=650)


    def create_get_started_frame(self):
       
        #quit button and top line labels
        quit_button = Button(self.get_started_frame, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.get_started_frame.destroy)
        quit_button.place(x=1200, y=15)

        crunch_label = Label(self.get_started_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.get_started_frame, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)

        logging_button = Button(self.get_started_frame, text="Logging", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.switch_to_logging)
        logging_button.place(x=1100, y=650)

        # Create and position the donut graph
        fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figsize as needed
        fig.patch.set_facecolor("none")  # Set the figure background to transparent
        ax.set_facecolor("none")  # Set the axes background to transparent
        data = [30, 70]  # Example data
        labels = ["CALS EATEN", "CALS LEFT"]  # Example labels
        wedges, texts, autotexts = ax.pie(data, labels=labels, autopct="%1.1f", startangle=90, colors=[FG_COLOR, "yellow"])
        plt.setp(autotexts, size=6, weight="bold")  # Adjust the text size

        # Add the donut center circle to create a donut chart
        center_circle = plt.Circle((0, 0), 0.70, fc="white")
        ax.add_artist(center_circle)

        ax.axis("equal")  # Equal aspect ratio ensures that the pie is drawn as a circle
        ax.set_title("Donut Chart Example")  # Set the title of the graph

        canvas = FigureCanvasTkAgg(fig, master=self.get_started_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=400, y=100)


    def create_logging_frame(self): #logs meal
        
        quit_button = Button(self.logging_frame, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.logging_frame.destroy)
        quit_button.place(x=1200, y=15)

        crunch_label = Label(self.logging_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.logging_frame, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)  

        meal_label = Label(self.logging_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Lunch Log")
        meal_label.place(x=20 , y=100)

        date_label = Label(self.logging_frame, text="Date:", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        date_label.place(x=20, y=170)

        food_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Food Name: ")
        food_label.place(x=20 , y=210)

        food_entry = Entry(self.logging_frame, font=input_box_font)
        food_entry.place(x=240, y=210, width=240)

        caloriesint_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Calories: ")
        caloriesint_label.place(x=20 , y=250)

        caloriesint_entry = Entry(self.logging_frame, font=input_box_font)
        caloriesint_entry.place(x=240, y=250, width=240)

        quantity_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Quantity: ")
        quantity_label.place(x=20 , y=290)

        quantity_entry = Entry(self.logging_frame, font=input_box_font)
        quantity_entry.place(x=240, y=290, width=240)

        save_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Save Meal? ")
        save_label.place(x=20 , y=330)

        save_var = IntVar()
        save_checkbox = Checkbutton(self.logging_frame, font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR, variable=save_var)
        save_checkbox.place(x=240, y=330)



        def open_calendar_popup():
            popup = Toplevel(self.root)  # Create a new popup window
            popup.title("Select Date")
            popup.geometry("300x250")  # Set the size of the popup window

            def confirm_date():
                selected_date_str = tkc.get_date()
                selected_date = datetime.strptime(selected_date_str, "%m/%d/%y").date()
                formatted_date = selected_date.strftime("%d/%m/%Y")
                date_label.config(text=f"Date: {formatted_date}")
                popup.destroy()

            current_date = datetime.today().date()
            tkc = Calendar(popup, selectmode="day", year=current_date.year, month=current_date.month, day=current_date.day)
            tkc.pack(pady=10)

            confirm_button = Button(popup, text="Confirm", font=SMALL_FONT, fg="black", command=confirm_date)
            confirm_button.pack()

        open_calendar_button = Button(self.logging_frame, text="Select Date", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=open_calendar_popup)
        open_calendar_button.place(x=285, y=170)



    def switch_to_frame(self, frame):
        self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def switch_to_home(self):
        self.switch_to_frame(self.home_frame)

    def switch_to_user_info(self, name, calorie_intake):
        self.user_info_frame.destroy()  # Destroy the previous user info frame if it exists
        self.user_info_frame = Frame(self.root, bg=BG_COLOR)  # Create a new user info frame
        self.create_user_info_frame(name, calorie_intake)  # Create the user info frame
        self.switch_to_frame(self.user_info_frame)

    def switch_to_get_started(self):
        self.get_started_frame.destroy()  # Destroy the previous user info frame if it exists
        self.get_started_frame = Frame(self.root, bg=BG_COLOR)  # Create a new user info frame
        self.create_get_started_frame()
        self.switch_to_frame(self.get_started_frame)

    def switch_to_logging(self):
        self.logging_frame = Frame(self.root, bg=BG_COLOR)  # Create a new user info frame
        self.create_logging_frame()
        self.switch_to_frame(self.logging_frame)
        print("switching to logging frame")

    def calculate(self):
        print("calculate check")

        error_message = self.error_check()
        if error_message:
            messagebox.showerror("Input Error", error_message)
            return

        # Get user inputs
        name = self.user_name_entry.get()
        age = int(self.age.get())
        gender = self.gender.get()
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())
        activity_level = self.activity.get()
        email = self.email_entry.get()
        
        if gender == "Male":
            calorie_intake = (13.75 * weight) + (5.003 * height) - (6.75 * age) + 66.5
        else:
            calorie_intake = (9.563 * weight) + (1.850 * height) - (4.676 * age) + 655.1

        activity_factors = {
            "Sedentary: little or no exercise": 1.2,
            "Light: exercise 1-3 times/week": 1.375,
            "Moderate: exercise 4-5 times/week": 1.55,
            "Active: daily exercise or intense exercise 3-4 times/week": 1.725,
            "Very Active: intense exercise 6-7 times/week": 1.9,
            "Extra Active: very intense exercise daily, or physical job": 2.0
        }
        if activity_level in activity_factors:
            calorie_intake *= activity_factors[activity_level]

        self.switch_to_user_info(name, calorie_intake)

    
    def error_check(self):
        print("error check")

        name = self.user_name_entry.get()
        age = self.age.get()
        gender = self.gender.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        activity_level = self.activity.get()
        email = self.email_entry.get()
        
        error_message = ""

        if not name or not re.match(r"^[A-Za-z\s]+$", name):
            error_message += "Invalid name format. Please enter a valid name.\n"

        if not age or not age.isdigit() or not (15 <= int(age) <= 80):
            error_message += "Invalid age. Please enter an age between 15 and 80.\n"

        if not gender:
            error_message += "Please select a gender.\n"

        if not height or not re.match(r"^\d+(\.\d{1,2})?$", height):
            error_message += "Invalid height format. Please enter a valid height.\n"

        if not weight or not re.match(r"^\d+(\.\d{1,2})?$", weight):
            error_message += "Invalid weight format. Please enter a valid weight.\n"

        if not activity_level:
            error_message += "Please select an activity level.\n"

        return error_message

    
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
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
