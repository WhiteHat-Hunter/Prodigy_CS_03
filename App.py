# Password Complexity Checker Application using Python By ~ Siddhesh Surve
# An Internship Based Task_3

import tkinter
import customtkinter
from PIL import ImageTk, Image
import re
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("740x700")
app.title("Secure IT")

# Add Fonts
my_font1 = customtkinter.CTkFont(family="bahnschrift", size=20, weight="bold")
my_font2 = customtkinter.CTkFont(family="Cascadia Code", size=15, weight="bold")
my_font3 = customtkinter.CTkFont(family="Century Gothic", size=16, weight="bold")
my_font4 = customtkinter.CTkFont(family="Cascadia Code", size=14, weight="bold")
my_font5 = customtkinter.CTkFont(family="bahnschrift", size=15, weight="bold")

# Load the common passwords from a file
def load_common_passwords(filename):
    with open(filename, 'r') as file:
        return set(file.read().splitlines())

# Function to check if the password contains personal information
def contains_personal_info(password, first_name, last_name, birthdate):
    # Convert birthdate to different possible segments (year, month, day)
    year = birthdate[:4]
    month = birthdate[4:6]
    day = birthdate[6:]
    
    # Check if the password contains the first name, last name, or any part of the birthdate
    if (first_name.lower() in password.lower() or 
        last_name.lower() in password.lower() or 
        year in password or 
        month in password or 
        day in password):
        return True
    return False

# Function to check password complexity
def check_password_complexity(password, common_passwords, first_name, last_name, birthdate):
    # Check if password contains personal information
    if contains_personal_info(password, first_name, last_name, birthdate):
        return False, "Password should not contain your Name or Birthdate."

    # Condition 1: First or any one of the alphabet in password should be uppercase
    if not any(c.isupper() for c in password):
        return False, "Password should contain at least one Uppercase Letter, \nA Mixture of Alphabets, Numbers and Special Characters."

    # Condition 2: Password should contain at least 7 characters with a mixture of alphabets, numbers, special characters
    if len(password) < 7:
        return False, "Password should be at least 7 characters long."
    
    if not (re.search(r"[a-zA-Z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return False, "Password should Contain a Mixture of Alphabets, \nNumbers, and Special Characters."
    
    # Condition 3: Password should contain more than 1 number
    if len(re.findall(r"\d", password)) < 2:
        return False, "Password should Contain More than 1 Number."

    # Condition 4: Password should not be a common password
    if password in common_passwords:
        return False, "Password is too Common and Found in Common Passwords."

    return True, "Your Password is Great! Strong Password."

    # Clear previous result labels
def clear_results():
    for widget in frame.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel) and widget.winfo_y() >= 500:
            widget.destroy()
            
# Main program
def main():
    clear_results()
    common_passwords = load_common_passwords('common.txt')
    
    # Get the user's personal information
    first_name = entry1.get()
    last_name = entry2.get()
    birthdate = entry4.get()

    # Get the user's password
    password = entry5.get()

    # Check if any of the required fields are empty
    if not first_name or not last_name or not birthdate or not password:
        # Display a message indicating that all fields are required
        result_null = customtkinter.CTkLabel(master=frame, text="Please provide all the required information: \nFirst Name, Last Name, Birthdate and Password.", text_color="#87CEEB", font=my_font3, wraplength=700)
        result_null.place(x=105, y=520)
        return  # Exit the function early if any fields are empty
    
    # Check the password complexity
    is_strong, message = check_password_complexity(password, common_passwords, first_name, last_name, birthdate)
          
    # Print the result
    if is_strong:
        result3 = customtkinter.CTkLabel(master=frame, text="Your Password is Strong meeting required Conditions!!", text_color="#87CEEB", font=my_font3, wraplength=700)
        result3.place(x=66, y=510)

    else:
        result1 = customtkinter.CTkLabel(master=frame, text=f"Your Password can be compromised. It is a Weak Password. \nReason: {message}", text_color="red", font=my_font4)
        result1.place(x=25, y=500)
        result2 = customtkinter.CTkLabel(master=frame, text="Example of Strong Password: YouCannotHack@Me963!", text_color="#87CEEB", font=my_font3, wraplength=700)
        result2.place(x=55, y=560)


def analyze_password():
    clear_results()
    progressbar = customtkinter.CTkProgressBar(master=frame)
    # Show the progress bar and run it for 5 seconds
    progressbar.place(x=190, y=530)
    progressbar.start()
    # Use the `after` method to schedule the next steps
    app.after(3200, stop_progress_and_analyze)

def stop_progress_and_analyze():
    progressbar = customtkinter.CTkProgressBar(master=frame)
    # Stop and hide the progress bar
    progressbar.destroy()  # Destroy the progress bar after use
    # Call the main function
    main()

    
bg = customtkinter.CTkImage(Image.open("bg.png"), size=(1550,980))
l1 = customtkinter.CTkLabel(master=app, image=bg)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=600,height=600, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

title_main = customtkinter.CTkLabel(master=frame, text="Secure IT ~ A Password Complexity Analyzer", text_color="#87CEEB", font=my_font1)
title_main.place(x=88,y=20)

l2 = customtkinter.CTkLabel(master=frame, text="Enter your First Name", text_color="#ffffff", font=my_font2)
l2.place(x=45,y=80)

# Name Entry Field
entry1=customtkinter.CTkEntry(master=frame, height=40, width=500, placeholder_text="First Name")
entry1.place(x=35, y=116)

l3 = customtkinter.CTkLabel(master=frame, text="Enter your Last Name", text_color="#ffffff", font=my_font2)
l3.place(x=40,y=170)

# Name Entry Field
entry2=customtkinter.CTkEntry(master=frame, height=40, width=500, placeholder_text="Last Name")
entry2.place(x=35, y=207)

l4 = customtkinter.CTkLabel(master=frame, text="Enter your birthdate (e.g., YYYYMMDD)", text_color="#ffffff", font=my_font2)
l4.place(x=40,y=260)

# Name Entry Field
entry4=customtkinter.CTkEntry(master=frame, height=40, width=500, placeholder_text="Birthdate")
entry4.place(x=35, y=296)

l5 = customtkinter.CTkLabel(master=frame, text="Enter Password used in every Platforms", text_color="#ffffff", font=my_font2)
l5.place(x=40,y=350)

# Password Entry Field
entry5=customtkinter.CTkEntry(master=frame, height=40, width=500, placeholder_text="Password")
entry5.place(x=35, y=390)

# Analyze Password Button
analyze = customtkinter.CTkButton(master=frame, text="Analyze", width=100, height=34, font=my_font5, command=analyze_password)
analyze.place(x=235, y=460)


app.mainloop()
    
