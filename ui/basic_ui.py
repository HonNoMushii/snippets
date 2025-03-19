import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QListWidget
from PyQt5.QtCore import QFileSystemWatcher
import re
import os

def is_valid(s):
    """
    Validate the license plate string.

    Args:
        s (str): The license plate string to validate.

    Returns:
        bool: True if the license plate is valid, False otherwise.
    """
    # Define the regex pattern for a valid plate
    pattern = r'^[A-Z]{2,6}[0-9]{0,4}$'
    
    # Check if the plate matches the pattern
    if not re.match(pattern, s):
        return False
    
    # Check if the first number is 0
    numbers_part = re.search(r'[0-9]+', s)
    if numbers_part and numbers_part.group(0)[0] == '0':
        return False
    
    return True

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window.
        """
        super().__init__()
        self.saved_input_file = "saved_input.txt"  # File to save the input
        self.setWindowTitle("Validating license plate")  # Set the window title
        self.resize(800, 400)  # Set the window size
        
        # Ensure the saved_input_file exists (so QFileSystemWatcher can watch it)
        if not os.path.exists(self.saved_input_file):
            with open(self.saved_input_file, "w") as file:
                pass
        
        # Create UI elements
        self.label = QLabel("Enter the name of your license plate:")
        self.textbox_input = QLineEdit()
        self.validate_button = QPushButton("Validate")
        self.result_label = QLabel("")
        self.saved_list = QListWidget()  # Initialize the saved_list as a QListWidget
        
        # Connect the validate button to the validate_plate method
        self.textbox_input.returnPressed.connect(self.on_return_pressed)
        self.validate_button.clicked.connect(self.validate_plate)
        
        # Create a vertical layout and add UI elements to it
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox_input)
        layout.addWidget(self.validate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(QLabel("Saved Plates:"))
        layout.addWidget(self.saved_list)
                
        # Create a container widget and set the layout
        container = QWidget()
        container.setLayout(layout)
        # Set the central widget of the main window
        self.setCentralWidget(container)
        
        # Load the saved input
        self.load_saved_input()
        
        # Set up a QFileSystemWatcher to monitor file changes
        self.watcher = QFileSystemWatcher([self.saved_input_file], self)
        self.watcher.fileChanged.connect(self.load_saved_input)
    
    def on_return_pressed(self):
        """
        Called when the user presses the return key in the textbox.
        """
        self.validate_plate()  # Call the validate_plate method
    
    def load_saved_input(self):
        """
        Load the saved input from the file.
        """
        try:
            with open(self.saved_input_file, "r") as file:
                lines = file.readlines()
                self.saved_list.clear()
                for line in lines:
                    plate = line.strip()
                    if is_valid(plate):
                        self.saved_list.addItem(plate)
        except FileNotFoundError:
            # File doesn't exist, ignore no saved input to display
            pass
        except Exception as e:
            QMessageBox.warning(self, "Load Error", "Failed to load the saved input: " + str(e))
    
    def save_input(self, plate):
        """
        Save the input to a file.
        """
        try:
            with open(self.saved_input_file, "a") as file:
                file.write(plate + "\n")
        except Exception as e:
            QMessageBox.warning(self, "Save Error", "Failed to save the input: " + str(e))
            
    def validate_plate(self):
        """
        Validate the license plate entered in the textbox, save it, and update the UI.
        """
        plate = self.textbox_input.text().strip().upper()
        if not plate:
            QMessageBox.warning(self, "Input Error", "Please enter a license plate.")
            return
        
        self.save_input(plate)
        
        if is_valid(plate):
            self.result_label.setText("Valid")
        else:
            self.result_label.setText("Invalid")
            QMessageBox.warning(self, "Validation Error", "The license plate is invalid.")
        
        # Clear the textbox after processing
        self.textbox_input.clear()
        
        
# Create the application
app = QApplication(sys.argv)

# Create and show the main window
window = MainWindow()
window.show()

# Run the application event loop
sys.exit(app.exec_())
