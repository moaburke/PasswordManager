# Password Manager Application

A simple password manager that allows users to:
1. Generate random passwords using letters, numbers, and symbols.
2. Save website, email/username, and password details into a file.
3. Copy generated passwords to the clipboard for easy pasting.
4. Validate user input and provide error messages for incomplete entries.

![password_manager_interface.png](password_manager_interface.png)

## Features

- Generates strong, random passwords.
- Saves the password securely in a text file with easy-to-read formatting.
- Utilizes Tkinter for the user interface with a clean and responsive design.
- Includes functionality to generate, save, and manage multiple passwords.

## Installation
To run this project, ensure you have Python installed on your computer. You can download Python from [python.org](https://www.python.org/).
- **Note**: Tkinter is included with most Python installations. No additional installation is required for Tkinter.
  
1. **Clone the Repository**:
```bash
git clone https://github.com/moaburke/PasswordManager.git
```
2. **Navigate to the project directory**:
```bash
cd PasswordManager
```
4. **Install required packages** (if applicable):
```bash
pip install pyperclip
```


- ## Usage

1. **Run the Application**:
   - Execute the Python script to launch the Password Manager interface. Make sure you have Tkinter and any required libraries installed.

2. **Enter Website Information**:
   - In the **Website** field, input the name of the website for which you want to save the password.

3. **Email/Username Entry**:
   - Fill in the **Email/Username** field with your email address or username associated with the website. A default email is pre-filled for convenience, which you can modify. You can also set your own email as the default email by changing the value in the code.

4. **Enter or Generate a Password**:
   - You can either enter your own password or click the **"Generate Password"** button to create a random password. The generated password will automatically appear in the **Password** field.

5. **Save the Password Details**:
   - Click the **"ADD"** button to save your website, email, and password information. If any fields are empty, an error message will prompt you to fill them out.

6. **Copy Password to Clipboard**:
   - After generating a password, it is automatically copied to your clipboard for easy pasting into other applications.

7. **Review Saved Data**:
- The application saves the entered details in `data.txt`, which you can open using any text editor (e.g., Notepad, VSCode) to review your saved passwords.


**Files**:
- Saves password data in `data.txt`.
- Uses `logo.png` as the application logo.
