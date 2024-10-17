"""
Password Manager Application

Author: Moa Burke
Date: 17 Oct 2024
Description:
    This program implements a simple Password Manager using Python and Tkinter for the GUI.
    Users can generate random passwords, save name of website, email/username, and password details to a file,
    retrieve them later, and copy the password to the clipboard. It ensures that no input fields are left empty before
    saving and allows the user to set their own default email in the input field. The application also includes
    a search functionality to find saved details for a specific website.
    Error handling has been implemented to manage file-related issues, and website names are saved in title case to
    ensure consistency and data retrieval.

Version: 1.1

Changelog:
    - 1.1:  Updated data storage to JSON format (from .txt), added try-except error handling for file operations,
            enforced title case for website names to ensure consistency and data retrieval, and introduced a search
            feature for retrieving saved passwords.
    - 1.0:  Initial version with core functionality (password generation, saving, and validation).
"""

from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


# Default Email Constant
DEFAULT_EMAIL = "my_email@gmail.com" # Default email to be displayed in the input field

# UI Appearance Constants
FONT_NAME = "Courier" # Font for labels and buttons
FONT = (FONT_NAME, 10, "bold") # Default font
LABEL_FONT = (FONT_NAME, 10, "bold") # Font for labels
BUTTON_FONT = (FONT_NAME, 12, "bold") # Font for 'Add' button
WHITE = 'white' # Background color for the UI
GRAY = 'gray98' # Input field background color
DARK_BLUE = '#132c52' # Primary text color
LIGHT_BLUE = '#a8d9f0' # 'Add' Button background color

# Padding Constants
PADDING_Y = 2 # Vertical padding between widgets
PADDING_X = 10 # Horizontal padding between widgets

# Entry and Button Size Constants
ENTRY_WIDTH = 60 # Width for input fields
BUTTON_WIDTH = 35 # Width for 'Add' button

# File Path Constants
DATA_FILE_PATH = "./data.txt" # Path to save the password data
LOGO_IMAGE_PATH = "logo.png" # Path to the logo image file

#Password Generator Parameters
MIN_LETTERS = 8
MAX_LETTERS = 10
MIN_SYMBOLS = 2
MAX_SYMBOLS = 4
MIN_NUMBERS = 2
MAX_NUMBERS = 4

# Message Box Constants
ERROR_TITLE = "Error" #Title for error message boxes
ERROR_MESSAGE = "Please don't leave any empty fields." # Error message

def find_data():
    """
    Function to find and retrieve saved data (email/username and password) for a specified website.
    It searches in the 'data.json' file, coped the password to the clipboard if found,
    and displays the information in a message box. If no data file is found or the website
    it nos present in the data, it shows an error message.
    """

    # Get the website name entered by the user and convert it to title case for consistency
    website = website_input.get().title()

    try:
        # Try and open the JSON file containing saved data
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file) # Load the data from the file
    except FileNotFoundError:
        # If the file does not exist, show an error message
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # Check if the website is in the saved data
        if website in data:
            # Retrieve the associated email and password
            email = data[website]["email"]
            password = data[website]["password"]

            # Copy the password to the system clipboard for easy pasting
            pyperclip.copy(password)

            # Display the email and password in a message box
            messagebox.showinfo(title=website, message=f"Email/Username: {email} \nPassword: {password} \n\nPassword has been copied to the clipboard.")

        else:
            # If no details are found for the entered website, show an error message
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


def generate_password():
    """
    Function to generate a random password using letters, symbols and numbers.
    Updates the password input field and copies the password to the clipboard.
    """
    # Lists of possible characters for the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly determine the number letters, symbols, and numbers for the password
    nr_letters = random.randint(MIN_LETTERS, MAX_LETTERS) # Choose random number of letters
    nr_numbers = random.randint(MIN_NUMBERS, MAX_NUMBERS) # Choose random number of numbers
    nr_symbols = random.randint(MIN_SYMBOLS, MAX_SYMBOLS) # Choose random number of symbols

    # Select random characters from each list based on the above numbers
    password_letters = [random.choice(letters) for _ in range(nr_letters)] # List of random letters
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)] # List of random numbers
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)] # List of random symbols

    # Combine the letters, symbols, and numbers info a single list
    password_list = password_letters + password_numbers + password_symbols

    # Shuffle the list to ensure randomness in the final password
    random.shuffle(password_list)

    # Convert the shuffled list of characters into a single string to form the final password
    password = "".join(password_list)

    # Clear the current password in the input fields and insert the new password
    password_input.delete(0, END) # Remove any previous password
    password_input.insert(0, password) # Insert the generated password into the input field

    # Copy the generated password to the system clipboard for easy pasting
    pyperclip.copy(password)


def save_data():
    """
    Function to save website, email, and password information to a JSON file.
    It checks if any input fields are empty before saving and shows a confirmation message.
    If the data file exists, it updates the existing data: if not, it creates a new file.
    """
    # Get the data from the input fields
    website = website_input.get().title() # Convert the website name to title case
    email = email_input.get() # Get the email from the input field
    password = password_input.get() # Get the password from the input field

    # Create a new dictionary to store the current website's details
    new_data = { website: {
            "email": email,
            "password": password
        }
    }

    # Check if any of the input fields are left empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        # Show error message if any field is blank
        messagebox.showinfo(title=ERROR_TITLE, message=ERROR_MESSAGE)
    else: # All input fields has been filled out
        try:
            # Try to open the existing JSON file and load its content
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file) # Load the old data from the file
        except FileNotFoundError:
            # If data_file does not exist, create a new one with the current data
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data's information
            data.update(new_data)

            # Save the updated data back to the file
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clear the input fields after the data has been saved
            delete_input()


def delete_input():
    """
    Function to clear the website and password input fields
    """
    website_input.delete(0, 'end') # Clear the website input field
    password_input.delete(0, 'end') # Clear the password input field


# Main window setup
window = Tk() # Create a new Tkinter window
window.title("Password Manager by Moa Burke") # Set the window title
window.config(padx=50, pady=50, bg=WHITE) # Configure padding and background color

# Create canvas to display logo
canvas = Canvas(width=350, height=200, highlightthickness=0) # Create a canvas widget
logo_img = PhotoImage(file=LOGO_IMAGE_PATH) # Load the logo image
canvas.create_image(175, 100, image=logo_img) # Add the image to the canvas
canvas.grid(column=0, row=0, columnspan=3) # Position the canvas on the grid


# Labels
website_label = Label(text="Website:", bg=WHITE, fg=DARK_BLUE, font=FONT) # Create a label for 'Website'
website_label.grid(column=0, row=1, pady=PADDING_Y)

email_label = Label(text="Email/Username:", bg=WHITE, fg=DARK_BLUE, font=FONT) # Create a label for 'Email/Usernames'
email_label.grid(column=0, row=2, pady=PADDING_Y)

password_label = Label(text="Password:", bg=WHITE, fg=DARK_BLUE, font=FONT) # Create a label for 'Password'
password_label.grid(column=0, row=3)


# Input fields (Entry Widgets)
website_input = Entry(width=40, bg=GRAY) # Create an input field for the website name
website_input.grid(row=1, column=1)
website_input.focus() # Set focus to the website input field

email_input = Entry(width=70, bg=GRAY)  # Create an input field for the email
email_input.grid(row=2, column=1, columnspan=2, padx=PADDING_X)
email_input.insert(0, "my_email@gmail.com") # Set a default email in the input fields

password_input = Entry(width=40, bg=GRAY)  # Create an input field for the password
password_input.grid(row=3, column=1)


# Buttons
#Button to find saved data
button_password = Button(text="Search", command=find_data, width="18", bg=LIGHT_BLUE, fg=DARK_BLUE, font=FONT)
button_password.grid(row=1, column=2, pady=PADDING_Y)

# Button to generate password
button_password = Button(text="Generate Password", command=generate_password, width="18", bg=LIGHT_BLUE, fg=DARK_BLUE, font=FONT)
button_password.grid(row=3, column=2, pady=PADDING_Y)

# Button to save data
button_add = Button(text="ADD", command=save_data, width=41 ,bg=DARK_BLUE, fg=WHITE, font=(FONT_NAME, 12, "bold"), borderwidth=5 )
button_add.grid(row=4, column=1, columnspan=2, pady=5)


# Start the Tkinter event loop
window.mainloop() # Keep the window open until manually closed