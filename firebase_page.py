#code by leah Kemp 2024
import sys
import json
import requests
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtGui import QIcon 
from colorama import Fore
import os

class ModernUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Adds icon for app
        self.setWindowIcon(QIcon('../AppLogo.png'))
        
        # Create layout
        layout = QVBoxLayout()

        # Add widgets
        title_label = QLabel("Firebase DB Writing tool")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title_label)

        name_label = QLabel("Database Link:")
        name_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(name_label)

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("font-size: 16px; padding: 5px;")
        layout.addWidget(self.name_input)
        
        back_button = QPushButton("Back to Main Page")
        back_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #007bff; color: white;")
        back_button.clicked.connect(self.go_to_main_page)

        # Add file selection button for .json file
        select_file_button = QPushButton("Select JSON File")
        select_file_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #bf1b39; color: white;")
        select_file_button.clicked.connect(self.select_json_file)
        layout.addWidget(select_file_button)

        # Add submit button
        submit_button = QPushButton("Submit Without Credentials")
        submit_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #28a745; color: white;")
        submit_button.clicked.connect(self.submit_form)
        layout.addWidget(submit_button)
#----------------------------------- buttons below need command code for them -----------------------------------
        # Add submit with creds button
        submit_with_creds_button = QPushButton("Submit With Credentials (WIP)")
        submit_with_creds_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #e87e0c; color: white;")
        submit_with_creds_button.clicked.connect(self.submit_with_creds_button)
        layout.addWidget(submit_with_creds_button)

#----------------------------------------------------------------------------------------------------------------
        # Add Download Firebase button
        Download_Firebase_button = QPushButton("Download Firebase Database")
        Download_Firebase_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #145fd9; color: white;")
        Download_Firebase_button.clicked.connect(self.Download_Firebase_button)
        layout.addWidget(Download_Firebase_button)

        # Add console log output section
        console_label = QLabel("Console Log:")
        console_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(console_label)

        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.console_output)
        self.console_output.append("DISCLAIMER: This script is to be used for legitimate purposes only. By using this script, you agree that the author is not responsible for any misuse, damage, or other liability arising from the use or inability to use this script. Use this script at your own risk.")

        # Set layout
        self.setLayout(layout)

    # submit with creds button
    def Download_Firebase_button(self):
        name = self.name_input.text()
        if not name.startswith("https://"):
            name = "https://" + name
        rsp_download = requests.get(name)
        current_time = datetime.datetime.now()
        file_name = f"Firebase_output_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.json"  # Corrected file name formatting
        with open(file_name, "w+") as file:
            file.write(rsp_download.text)
        with open(file_name, "r") as file:  # Corrected file name
            self.console_output.append(file.read())
        self.console_output.append(f'Saved Firebase output to "{file_name}" in local directory')

    # submit with creds button (WIP)
    def submit_with_creds_button(self):
        self.console_output.append("This is a work in progress")

    def select_json_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select JSON File", "", "JSON Files (*.json)")
        if file_path:
            self.console_output.append(f"Selected JSON File: {file_path}")
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                self.console_output.append(f"JSON Content: {json_data}")
                self.json_data = json_data

    def submit_form(self):
        name = self.name_input.text()
        if not name.startswith("https://"):
            name = "https://" + name
        self.console_output.append(f"Database Name: {name}")
        if hasattr(self, 'json_data'):
            FB_URL = name
            data = self.json_data
            rsp = requests.put(FB_URL, json=data)
            #--------status codes--------#
            if rsp.status_code == 200:
                self.console_output.append("Data Successfully written to Firebase server")
            elif rsp.status_code == 401:
                self.console_output.append("Error: 401 Access Denied")
            elif rsp.status_code == 404:
                self.console_output.append("Error: 404 Firebase Database Not Found")
            else:
                self.console_output.append("Error: An Unknown Error Occurred, unable to send data")
        else:
            self.console_output.append("Error: Please select a JSON file first")
    
    def go_to_main_page(self):
        # Close the current Firebase page
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ModernUI()
    ui.setWindowTitle("Firebase DB Writing tool")
    ui.setGeometry(100, 100, 400, 300)
    ui.show()
    sys.exit(app.exec_())