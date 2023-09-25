#Author: Prisha

#imports
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import re
from tkcalendar import Calendar
from datetime import datetime
import atexit
import json


#Fonts and colours
BG_COLOR = "white" #background
FG_COLOR = "#19b092" #text colour (teal)
GREY_COLOR = "grey27"
HEADING_FONT = "Helvetica 25 bold"
SMALL_FONT = "Helvetica 15 bold"
MAIN_HEADING_FONT = "Helvetica 35 bold"
ALT_HEADING_FONT = "Raleway 35"
BUTTON_FONT = "Helvetica 35" 
DISCLAIMER_FONT = "Helvetica 17"
TITLE_FONT = "Helvetica 35 bold"
INPUT_BOX_FONT = "Helvetica 12" 
CAL_FONT = "Helvetica 60 bold" 


#Create class for app
class CrunchCounterApp: 
    def __init__(self, root):
        self.root = root
        self.root.title("Crunch Counter")
        self.root.config(bg=BG_COLOR)
        self.root.attributes("-fullscreen", True) #sets app to fit whole screen
        self.calorie_intake = 0
        self.user_data = {} #empty dictionary to store user data
        self.load_user_data()
        atexit.register(self.save_user_data) #saves user data upon exit
        self.create_frames()
        self.calorie_logs = []

    #Create all frames
    def create_frames(self): #creates frames, initialise and sets current frame
        self.current_frame = None #sets current frame to none
        self.home_frame = Frame(self.root, bg=BG_COLOR)
        self.user_info_frame = Frame(self.root, bg=BG_COLOR)
        self.get_started_frame = Frame(self.root, bg=BG_COLOR)
        self.create_home_frame() #starts up the home page

        self.current_frame = self.home_frame #sets current frame to home page
        self.current_frame.pack(fill="both", expand=True)

    #Sign up page (homepage) for user's to sign up or log in
    def create_home_frame(self): #page 1 (welcome, disclaimer & user inputs)

        #top line labels and buttons
        crunch_label = Label(fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.root, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)

        quit_button = Button(self.root, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.root.quit)
        quit_button.place(x=1200, y=15)


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

        disclaimer_label1 = Label(disclaimer_frame, fg="black", font=DISCLAIMER_FONT, bg=BG_COLOR, text="Our calorie counting app is designed\nfor informational purposes only and\nshould not be considered medical advice.\n\nFor personalised guidance, please consult a\nqualified healthcare professional or dietician.")
        disclaimer_label1.pack(pady=10)

        #Create the user input frame
        frame = Frame(self.root, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        frame.place(x=700, y=100, width=500, height= 600)
        user_info_label = Label(frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="User Info")
        user_info_label.place(x=150, y=5)
        
        labels = ["Name:", "Age:", "Gender:", "Height:", "Weight:", "Activity:", "Email:"] #displays labels next to entries
        for i, label_text in enumerate(labels):
            Label(frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text=label_text).place(x=15, y=90 + i * 47) 

        # Entries

        #Name Entry
        self.user_name_entry = EntryWithPlaceholder(frame, "Full Name", font=INPUT_BOX_FONT)
        self.user_name_entry.place(x=160, y=103)

        #Age Entry
        ages = [str(age) for age in range(15, 51)]
        self.age = StringVar()
        age_chosen = ttk.Combobox(frame, textvariable=self.age, values=ages, state="readonly", width=5, font=INPUT_BOX_FONT)
        age_chosen.place(x=160, y=147)

        #Gender Entry
        self.gender = StringVar()
        style = ttk.Style()
        style.configure("TRadiobutton", background=BG_COLOR, font="Helvetica 15")
        ttk.Radiobutton(frame, text="Male", value="Male", var=self.gender, state="readonly", width=6, style="TRadiobutton").place(x=160, y=194)
        ttk.Radiobutton(frame, text="Female", value="Female", var=self.gender, state="readonly", width=6, style="TRadiobutton").place(x=250, y=194)

        #Height Entry
        self.height_entry = EntryWithPlaceholder(frame, "cm", font=INPUT_BOX_FONT)
        self.height_entry.place(x=160, y=244)

        #Weight Entry
        self.weight_entry = EntryWithPlaceholder(frame, "kg", font=INPUT_BOX_FONT)
        self.weight_entry.place(x=160, y=291)

        #Activity Entry
        activity_amount = ["Sedentary: little or no exercise", "Light: exercise 1-3 times/week", "Moderate: exercise 4-5 times/week",
                        "Active: daily exercise or intense exercise 3-4 times/week", "Very Active: intense exercise 6-7 times/week",
                        "Extra Active: very intense exercise daily, or physical job"]
        self.activity = StringVar()
        activity_chosen = ttk.Combobox(frame, textvariable=self.activity, values=activity_amount, state="readonly", width=32, font=INPUT_BOX_FONT)
        activity_chosen.place(x=160, y=338)

        #Email entry
        self.email_entry = EntryWithPlaceholder(frame, "email address", font=INPUT_BOX_FONT)
        self.email_entry.place(x=160, y=385)

        #Calculate Calories Button
        calculate_button = Button(frame, text="Calculate !", font="Helvetica 20 bold", fg=FG_COLOR, bg=BG_COLOR, command=lambda: self.calculate())
        calculate_button.place(x=160, y=430)

        #Open Login Frame Button
        go_login_button = Button(frame, text="Login", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.create_login_frame)
        go_login_button.place(x=200, y=500)


    #For user to log into their "profile"
    def create_login_frame(self):

        #Create a frame for login
        login_frame = Frame(self.root, bg=BG_COLOR)
        login_frame.place(x=60, y=100, width=500, height=210)

        #Label above entry
        login_label = Label(login_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="User Login")
        login_label.pack(pady=20)

        #Entry for the user to enter their name
        self.login_entry = EntryWithPlaceholder(login_frame, "Full Name", font=input_box_font)
        self.login_entry.pack()

        #Allows them to login if user name exists
        def login():
            entered_name = self.login_entry.get().strip() #removes any whitespace

            if entered_name in self.user_data:
                print("Successful login", entered_name)
                user_data = self.user_data[entered_name] 
                self.switch_to_get_started(user_data)
            else:
                messagebox.showerror("Login Error", "User not found. Please enter a valid name. (CASE SENSITIVE)") #Displays error message

        #Login Button
        self.login_button = Button(login_frame, text="Login", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=login)
        self.login_button.pack(pady=10)

    #Page that shows user's recommended calorie intake
    def create_user_info_frame(self, name, calorie_intake):

        #Quit button and top line labels
        quit_button = Button(self.user_info_frame, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.root.quit)
        quit_button.place(x=1200, y=15)

        crunch_label = Label(self.user_info_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.user_info_frame, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)

        #Display user's name and recommended calorie intake outside the calorie frame
        result_label = Label(self.user_info_frame, text=f"{name}'s\nRecommended\nCalorie Intake\n(Per Day):", font=CAL_FONT, fg=FG_COLOR, bg=BG_COLOR)
        result_label.place(x=20, y=200)

        #Create a frame to display calorie intake number
        calorie_frame = Frame(self.user_info_frame, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=10)
        calorie_frame.place(x=700, y=200, width=550, height=320)

        #Display number
        calorie_number_label = Label(calorie_frame, text=f"{round(calorie_intake)}kcal", font=CAL_FONT, fg=FG_COLOR, bg=BG_COLOR)
        calorie_number_label.pack(padx=50, pady=100)

        #Get started button
        get_started_button = Button(self.user_info_frame, text="Get Started ➭", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.switch_to_get_started)
        get_started_button.place(x=1100, y=650)


    #Main page where user can go to logging page and view their calorie goal progress
    def create_get_started_frame(self, calorie_intake, user_data):

        #top line labels and buttons
        quit_button1 = Button(self.get_started_frame, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.root.quit)
        quit_button1.place(x=1200, y=15)

        crunch_label = Label(self.get_started_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.get_started_frame, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)

        #Create frame for logging buttons
        frame = Frame(self.get_started_frame, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=7)
        frame.place(x=20, y=100, width=450, height= 600)

        #Log Calories label
        log_cal_label = Label(frame, fg=GREY_COLOR, font=ALT_HEADING_FONT, bg=BG_COLOR, text="LOG CALORIES")
        log_cal_label.place(x=40, y=15)

        #Buttons configurations to position and change images and text name to match the meal
        button_configs = [
            {
                "image_path": "breakfast_button1.png",
                "width": 370,
                "height": 90,
                "y_position": 90,
                "meal_label_text": "Breakfast Log",
            },
            {
                "image_path": "lunch_button1.png",
                "width": 370,
                "height": 100,
                "y_position": 210,
                "meal_label_text": "Lunch Log",
            },
            {
                "image_path": "dinner_button1.png",
                "width": 370,
                "height": 100,
                "y_position": 330,
                "meal_label_text": "Dinner Log",
            },
            {
                "image_path": "snack_button1.png",
                "width": 370,
                "height": 100,
                "y_position": 450,
                "meal_label_text": "Snack Log",
            },
        ]

        for config in button_configs:
            image_path = config["image_path"]
            button_width = config["width"]
            button_height = config["height"]
            y_position = config["y_position"]
            
            image = PhotoImage(file=image_path)
            image = image.subsample(int(image.width() / button_width), int(image.height() / button_height))
            
            #Logging Button
            button = Button(frame, image=image, command=lambda text=config["meal_label_text"]: self.switch_to_logging(text), borderwidth=0)
            button.image = image
            button.place(x=30, y=y_position)

        #Frame for Calorie labels and log table
        widgets_frame = Frame(self.get_started_frame, bg=BG_COLOR, relief="groove", highlightbackground=FG_COLOR, highlightthickness=7)
        widgets_frame.place(x=500, y=100, width=750, height= 600)

        #Current Date Label
        current_date = datetime.now().strftime("%d-%m-%Y")
        today_date = Label(widgets_frame, text=f"Date: {current_date}", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        today_date.place(x=450, y=20)

        # Create labels to display calories eaten and calories left
        self.calories_eaten_label = Label(widgets_frame, text="Calories Eaten: 0", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        self.calories_eaten_label.place(x=30, y=20)

        self.calories_left_label = Label(widgets_frame, text=f"Calories Left: {calorie_intake}", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        self.calories_left_label.place(x=30, y=80)

        self.calories_goal_label = Label(widgets_frame, text=f"Calories Goal: {calorie_intake}", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        self.calories_goal_label.place(x=30, y=140)

        #Retrieves user data if available
        if user_data:
            self.user_name_entry.delete(0, END)
            self.user_name_entry.insert(0, user_data.get("Name", "")) #inserts user name into user_name_entry so that it can be passed later on
            name = self.user_name_entry.get()

            if user_data.get("calories_eaten", 0) != 0: #Checks if calories eaten is 0 and if so, sets calories left to calorie intake 
                self.calorie_intake = user_data.get("calorie_intake", self.calorie_intake)

            # Update labels to display calories eaten, calories left, and calories goal
            self.calories_eaten_label.config(text=f"Calories Eaten: {user_data.get('calories_eaten', 0)}")

            self.calories_left_label.config(text=f"Calories Left: {user_data.get('calories_left')}")

            self.calories_goal_label.config(text=f"Calories Goal: {user_data.get('calorie_intake')}")


        # Error Checking
            print("previous data entered")
        else:
            print("no data")
            name = self.user_name_entry.get()
    
        # User logged in Label
        user_logged_in = Label(widgets_frame, text=f"Logged in as:\n {name}", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        user_logged_in.place(x=450, y=80)

        #Calorie Reset Button
        reset_button = Button(widgets_frame, text="Reset Calories", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.reset_calories)
        reset_button.place(x=100, y=200)

        #Create table to display calorie logs
        self.calorie_log_tree = ttk.Treeview(widgets_frame, columns=("Date", "Calories Eaten", "Goal Achieved"), show="headings")
        self.calorie_log_tree.heading("Date", text="Date")
        self.calorie_log_tree.heading("Calories Eaten", text="Calories Eaten")
        self.calorie_log_tree.heading("Goal Achieved", text="Goal Achieved")
        self.calorie_log_tree.place(x=70, y=300)
        self.update_calorie_log_table(name)

        #Add scrollbar to table
        scrollbar = Scrollbar(widgets_frame, orient="vertical", command=self.calorie_log_tree.yview)
        scrollbar.place(x=653, y=302, height=223)
        self.calorie_log_tree.configure(yscrollcommand=scrollbar.set)

        # Disable editing of table
        self.calorie_log_tree.bind("<Button-1>", lambda event: "break")
        self.calorie_log_tree.bind("<Button-3>", lambda event: "break")

    #Inserts the existing calorie log data of user into the table
    def update_calorie_log_table(self, name):
        #Clear the existing rows in the Treeview widget
        for item in self.calorie_log_tree.get_children():
            self.calorie_log_tree.delete(item)

        #Retrieve the user's calorie logs
        if name in self.user_data and "calorie_logs" in self.user_data[name]:
            logs = self.user_data[name]["calorie_logs"]
            print(name, "update")
            for log in logs:
                current_date = log["Date"]
                calories_eaten = log["Calories Eaten"]
                goal_achieved = log["Goal Achieved"]
                self.calorie_log_tree.insert("", "end", values=(current_date, calories_eaten, "Yes" if goal_achieved else "No"))

    #Logs the current numbers in the table
    #Resets calories eaten to 0 and calories left to the user's calorie intake
    def reset_calories(self):
        name = self.user_name_entry.get()
        if name in self.user_data:
            current_date = datetime.now().strftime("%d-%m-%Y %H:%M") #Get the current date

            calories_eaten = self.user_data[name]["calories_eaten"] #Calculate calories eaten

            #Calculate whether the goal is achieved
            goal_achieved = calories_eaten >= self.user_data[name]["calorie_intake"]  # Check if calories eaten are greater than or equal to the goal

            self.user_data[name]["calories_eaten"] = 0 #Reset calories eaten to 0
            # Recalculate calories left based on calorie intake
            self.user_data[name]["calories_left"] = self.user_data[name]["calorie_intake"]# Adjust calories_left

            log_entry = {"Date": current_date, "Calories Eaten": calories_eaten, "Goal Achieved": goal_achieved} #Create a log dictionary

            self.calorie_log_tree.insert("", "end", values=(current_date, calories_eaten, "Yes" if goal_achieved else "No")) #Update table

            # Add the log to the user's calorie logs list
            if "calorie_logs" not in self.user_data[name]:
                self.user_data[name]["calorie_logs"] = []
            self.user_data[name]["calorie_logs"].insert(0, log_entry)

            #Save the updated user data to the JSON file
            self.save_user_data()

            # Update the get frame to reflect the changes
            self.switch_to_get_started(self.user_data.get(name, {}))
            print('reset calories')  # Error checking


    #Calorie Logging frame
    def create_logging_frame(self, meal_label_text): #logs meal
        
        #Labels, Lines and Buttons 
        quit_button = Button(self.logging_frame, text="Quit", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.root.quit)
        quit_button.place(x=1200, y=15)

        back_button = Button(self.logging_frame, text="Back", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.go_back)
        back_button.place(x=1100, y=15) #Lets user go back to get started frame without logging

        crunch_label = Label(self.logging_frame, fg=FG_COLOR, font=MAIN_HEADING_FONT, bg=BG_COLOR, text="Crunch Counter")
        crunch_label.place(x=5, y=5)

        line_canvas = Canvas(self.logging_frame, bg=BG_COLOR, highlightthickness=0)
        line_canvas.place(x=0, y=70, width=1400, height=5)
        line_canvas.create_line(0, 0, 1400, 0, fill=FG_COLOR, width=5)  

        #Meal Label that changes depending on what button was clicked
        meal_label = Label(self.logging_frame, fg=GREY_COLOR, font=TITLE_FONT, bg=BG_COLOR, text=meal_label_text)
        meal_label.place(x=20, y=100)

        #Icons that are placed next to meal label (also depending on what button was clicked)
        image_paths = {
            "Breakfast Log": "breakfast_image.png",
            "Lunch Log": "lunch_image.png",
            "Dinner Log": "dinner_image.png",
            "Snack Log": "snack_image.png",
        }

        if meal_label_text in image_paths:
            image_path = image_paths[meal_label_text]
            meal_image = PhotoImage(file=image_path)
            meal_image_label = Label(self.logging_frame, image=meal_image, bg=BG_COLOR)
            meal_image_label.image = meal_image

            #Placement of images
            if meal_label_text == "Breakfast Log":
                meal_image_label.place(x=360, y=90)
            elif meal_label_text == "Lunch Log":
                meal_image_label.place(x=290, y=90)
            elif meal_label_text == "Dinner Log":
                meal_image_label.place(x=290, y=90)
            elif meal_label_text == "Snack Log":
                meal_image_label.place(x=270, y=90)

        #Labels, Entries and Buttons

        #Date
        date_label = Label(self.logging_frame, text="Date", font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
        date_label.place(x=20, y=200)

        self.user_date_label = Label(text="", bg=BG_COLOR)
        self.user_date_label.place(x=240, y=213)

        #Food Name
        food_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Food Name: ")
        food_label.place(x=20 , y=250)

        self.food_entry = Entry(self.logging_frame, font=input_box_font)
        self.food_entry.place(x=240, y=263, width=240)

        #Calories
        caloriesint_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Calories: ")
        caloriesint_label.place(x=20 , y=300)

        self.caloriesint_entry = Entry(self.logging_frame, font=input_box_font)
        self.caloriesint_entry.place(x=240, y=313, width=240)

        #Quantity
        quantity_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Quantity: ")
        quantity_label.place(x=20 , y=350)

        self.quantity_entry = Entry(self.logging_frame, font=input_box_font)
        self.quantity_entry.place(x=240, y=363, width=240)

        #Save Meal
        save_label = Label(self.logging_frame, fg=FG_COLOR, font=HEADING_FONT, bg=BG_COLOR, text="Save Meal? ")
        save_label.place(x=20 , y=400)

        self.save_var = IntVar()
        self.save_checkbox = Checkbutton(self.logging_frame, fg=FG_COLOR, bg=BG_COLOR, variable=self.save_var)
        self.save_checkbox.place(x=240, y=413)

        #Save Log Button
        self.save_log_button = Button(self.logging_frame, text="SAVE LOG", font=SMALL_FONT, fg=FG_COLOR, bg=BG_COLOR, command=self.save_log)
        self.save_log_button.place(x=290, y=460)

        #Calender window that lets users set the date
        def open_calendar_popup():
            popup = Toplevel(self.root)  #Create a new popup window
            popup.title("Select Date")
            popup.geometry("300x250")  #Set the size of the popup window

            def confirm_date(): #Takes the selected date, formats and enters into date label
                selected_date_str = tkc.get_date()
                selected_date = datetime.strptime(selected_date_str, "%m/%d/%y").date()
                formatted_date = selected_date.strftime("%d/%m/%Y")
                self.user_date_label.config(text=f"{formatted_date}", bg=BG_COLOR, font="Helvetica 15")
                popup.destroy()

            #Makes the calender auto select the current date
            self.current_date = datetime.today().date()
            tkc = Calendar(popup, selectmode="day", year=self.current_date.year, month=self.current_date.month, day=self.current_date.day)
            tkc.pack(pady=10)

            #Confirm Button
            confirm_button = Button(popup, text="Confirm", font=SMALL_FONT, fg="black", command=confirm_date)
            confirm_button.pack()

        #Open Calender Button
        open_calendar_button = Button(self.logging_frame, text="📆", font="Helvetica 16", fg="black", bg=BG_COLOR, command=open_calendar_popup)
        open_calendar_button.place(x=105, y=200)


        #Common Foods table
        #Label     
        self.food_table_label = Label(self.logging_frame, text="Common Foods", font=TITLE_FONT, fg=GREY_COLOR, bg=BG_COLOR,)
        self.food_table_label.place(x=720, y=100)

        #Creates table
        self.food_table = ttk.Treeview(self.logging_frame, columns=("Food", "Calories"), show="headings", height=21)
        self.food_table.heading("Food", text="Food (1 serving)")
        self.food_table.heading("Calories", text="Calories (kcal)")
        self.food_table.place(x=700, y=200)

        #Add Scrollbar
        scrollbar = Scrollbar(self.logging_frame, orient="vertical", command=self.food_table.yview)
        scrollbar.place(x=1083, y=202, height=443)
        self.food_table.configure(yscrollcommand=scrollbar.set)

        #Disable editing of table
        self.food_table.bind("<Button-1>", lambda event: "break")
        self.food_table.bind("<Button-3>", lambda event: "break") 
      
        #Displays all items from food list
        for food, calories in food_data.items():
            self.food_table.insert("", "end", values=(food, calories))

    #Saves the calories that user logs and updates/passes it to get started frame where labels are updated
    def save_log(self):
        food_name = self.food_entry.get()
        calories_log = self.caloriesint_entry.get()
        quantity = self.quantity_entry.get()
        save_meal = self.save_var.get()
        selected_date = self.user_date_label["text"]

        error_message = ""

        if selected_date.strip() == "":
            error_message += "Please select a date.\n"

        if not food_name or not re.match(r"^[A-Za-z0-9\s&'-]+$", food_name): #allows letters, ampersands (&), single quotes ('), and hyphens (-), numbers and spaces
            error_message += "Please fill in a valid food name.\n"

        if not quantity or not re.match(r"^\d{1,3}$", quantity): # only allows 3 digits
            error_message += "Please enter a valid number for quantity.\n"


        if not calories_log or not re.match(r"^\d{1,3}$", calories_log): #only allows 3 digits
            error_message += "Please enter a valid number for calories.\n"

        if error_message:
            messagebox.showerror("Input Error", error_message) # display error message
            return
        
        #Calculates calories eaten and left
        calories_eaten = int(calories_log) * int(quantity)
        calories_left = int(self.calorie_intake) - calories_eaten
        name = self.user_name_entry.get() #Define user name
        
        self.update_user_data(name, calories_eaten, calories_left) #Update the users data with calories eaten and calories left
        self.switch_to_get_started(self.user_data.get(name, {})) #Pass user's name to get started

    #Back button for logging frame
    def go_back(self):

        name = self.user_name_entry.get()
        self.switch_to_get_started(self.user_data.get(name, {}))

    #Updates the user data json file
    def update_user_data(self, name, calories_eaten, calories_left):
        if name in self.user_data:
            self.user_data[name]["calories_eaten"] = self.user_data[name].get("calories_eaten", 0) + calories_eaten
            self.user_data[name]["calories_left"] = self.user_data[name]["calorie_intake"] - self.user_data[name]["calories_eaten"]
            self.save_user_data()
            print("saved user data (logging)") #Error checking
        
        #Checks if calories left is below 0 and sets it to 0
        if self.user_data[name]["calories_left"] < 0:
            self.user_data[name]["calories_left"] = 0
            print('calorie left = 0') #Error checking
        

    #Used to switch to all frames
    def switch_to_frame(self, new_frame):
        if self.current_frame:
            self.current_frame.destroy()  #Destroy the current frame
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    #User info
    def switch_to_user_info(self, name, calorie_intake):
        if self.current_frame:
            self.current_frame.destroy()
        self.calorie_intake = calorie_intake
        self.user_info_frame = Frame(self.root, bg=BG_COLOR)
        self.create_user_info_frame(name, calorie_intake)
        self.switch_to_frame(self.user_info_frame)

    #Get started
    def switch_to_get_started(self, user_data=None):
        if self.current_frame:
            self.current_frame.destroy()  #Destroy the current frame if it exists

        if hasattr(self, 'get_started_frame'):
            self.get_started_frame.destroy()  #Destroy the previous get_started_frame if it exists

        self.get_started_frame = Frame(self.root, bg=BG_COLOR)
        self.create_get_started_frame(self.calorie_intake, user_data)  #Pass the stored calorie_intake
        self.current_frame = self.get_started_frame
        self.current_frame.pack(fill="both", expand=True)

    #Logging
    def switch_to_logging(self, meal_label_text):
        self.logging_frame = Frame(self.root, bg=BG_COLOR) #Creates logging frame
        self.create_logging_frame(meal_label_text)
        self.switch_to_frame(self.logging_frame)

    #Calculates the user's recommended calorie intake
    def calculate(self):
        print("calculate check") #Error checking

        error_message = self.error_check()
        if error_message:
            messagebox.showerror("Input Error", error_message)
            return

        # Get user inputs
        name = self.user_name_entry.get().strip() #removes any whitespace at the start and end
        age = int(self.age.get())
        gender = self.gender.get()
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())
        activity_level = self.activity.get()
        email = self.email_entry.get()
        
        #Do calculations based of male or female
        if gender == "Male":
            calorie_intake = (13.75 * weight) + (5.003 * height) - (6.75 * age) + 66.5
        else:
            calorie_intake = (9.563 * weight) + (1.850 * height) - (4.676 * age) + 655.1

        #Multiply by activity factor
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
            calorie_intake = round(calorie_intake)
            
        '''
        User data will update NOT create a new profile if user signs up again with the same name
        '''

        #Creates user data dictionary
        user_data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Height": height,
            "Weight": weight,
            "Activity": activity_level,
            "Email": email,
            "calorie_intake": calorie_intake,
            "calories_eaten": 0, #Initially set to 0
            "calories_left": calorie_intake, #Initially set to calorie intake
    
        }
        self.user_data[name] = user_data  # save user data in the dictionary
        self.save_user_data() #save updated user data
        self.switch_to_user_info(name, calorie_intake) #switch to user info page

    #Error checks the user sign up inputs and displays an error message
    def error_check(self):
        print("error check") #Error checking

        name = self.user_name_entry.get()
        age = self.age.get()
        gender = self.gender.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        activity_level = self.activity.get()
        email = self.email_entry.get()
        
        error_message = ""

        if not name or not re.match(r"^[A-Za-z\s]+$", name) or name == "Full Name":
            error_message += "Invalid name format. Please enter a valid name.\n"

        if not age or not age.isdigit() or not (15 <= int(age) <= 50):
            error_message += "Invalid age. Please enter an age between 15 and 50.\n"

        if not gender:
            error_message += "Please select a gender.\n"

        if not height or not re.match(r"^\d{1,3}(\.\d{1,2})?$", height):
            error_message += "Invalid height format. Please enter a valid height.\n"

        if not weight or not re.match(r"^\d{1,3}(\.\d{1,2})?$", weight):
            error_message += "Invalid weight format. Please enter a valid weight.\n"

        if not activity_level:
            error_message += "Please select an activity level.\n"

        if not email or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) or email == "email address":
            error_message += "Invalid email. Please enter a valid email address\n"

        return error_message

    #Saves new user data to json file
    def save_user_data(self): 
        with open("user_data.json", "w") as file:
            json.dump(self.user_data, file)

    #Loads all data on initialisation
    def load_user_data(self):
        try:
            with open("user_data.json", "r") as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {}

#Allows text to delete when user clicks on Entry boxes
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

#Food data to go into common foods table in logging frame
food_data = {
        "Oatmeal": 150,
        "Scrambled Eggs": 140,
        "Whole Wheat Toast": 70,
        "Greek Yogurt": 100,
        "Milk (1 cup)": 120,
        "Pancakes": 210,
        "Bacon (2 slices)": 86,
        "Grilled Chicken Sandwich": 350,
        "Caesar Salad": 200,
        "Turkey and Avocado Wrap": 400,
        "Vegetable Soup": 120,
        "Tuna Salad": 180,
        "BLT Sandwich": 450,
        "Salmon Fillet": 367,
        "Steak (6 oz)": 420,
        "Grilled Vegetables": 100,
        "Baked Potato": 150,
        "Spaghetti with Marinara Sauce": 200,
        "Sushi (8 pieces)": 320,
        "Almonds (1 oz)": 160,
        "Carrot Sticks": 30,
        "Hummus (2 tbsp)": 70,
        "Apple": 72,
        "Banana": 105,
        "Popcorn (1 cup air-popped)": 31,
        "Chocolate Bar": 210,
 
}
#Define main to run CrunchCounterApp
def main():
    root = Tk()
    app = CrunchCounterApp(root)
    root.resizable(False, False) #makes window size uneditable by user
    root.mainloop()

if __name__ == "__main__":
    main() #Call main to start app