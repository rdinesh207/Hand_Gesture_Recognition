import PySimpleGUI as sg
import subprocess

base64_image = """YOUR_IMAGE"""

# Define uniform button size
button_size = (15, 2)

# Define the button's color
button_color = ('goldenrod', 'maroon')

# 2x2 Button layout, centered
button_layout = [
    [sg.Button('Gesture Detection', size=button_size, button_color=button_color, tooltip='Start Script 1'),
     sg.Button('Sign Language', size=button_size, button_color=button_color, tooltip='Start Script 2')],
    [sg.Button('Media Control', size=button_size, button_color=button_color, tooltip='Start Script 3'),
     sg.Button('Close', size=button_size, button_color=button_color, tooltip='Exit Application')]
]

# Main layout with a title, an image, description, and buttons at the bottom center of the window
layout = [
    [sg.Text('Welcome to the Application', font=("Times New Roman", 16), text_color='white', background_color='black')],  # Title text
    [sg.Image(data=base64_image)],  # Image
    [sg.Text('Select a script to run or close the application.', text_color='white', background_color='black')],  # Description text
    [sg.Column([], expand_y=True, background_color='black')],  # Empty column for vertical spacing
    [sg.Column(button_layout, element_justification='center', background_color='black')]  # Column for buttons
]

# Create the window with a specific size and background color
window = sg.Window("General Gesture", layout, size=(300, 400), background_color='black')

# Event loop
while True:
    event, values = window.read()

    if event == "Gesture Detection":
        # Specify the full path to your script1.py
        script_path = "gesture_detection.py"
        subprocess.Popen(["python", script_path])
    elif event == "Sign Language":
        # Specify the full path to your script2.py
        script_path = "sign_language.py"
        subprocess.Popen(["python", script_path])
    elif event == "Media Control":
        # Specify the full path to your script3.py
        script_path = "media_control.py"
        subprocess.Popen(["python", script_path])
    elif event == "Close" or event == sg.WIN_CLOSED:
        break

window.close()
