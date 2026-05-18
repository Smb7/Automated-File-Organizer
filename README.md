# Automated File Organizer

A Python-based desktop application that automates the organization of files into categorized folders based on file type.

## Overview

Automated File Organizer is a user-friendly tool designed to streamline file management by intelligently sorting and organizing files into dedicated directories. Simply point the application to a folder, and it will automatically categorize and move files into appropriate subdirectories based on their file extensions.

## Features

- **Automated Organization**: Quickly sort files into predefined categories
- **File Type Recognition**: Intelligently identifies and categorizes various file types
- **User-Friendly Interface**: Intuitive file selection and execution
- **Cross-Platform Support**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.7 or higher
- tkinter (usually included with Python)

## Installation & Usage

1. **Download and Extract**: Download the repository as a ZIP file and extract it to your desired location
2. **Open Terminal/Command Prompt**: Navigate to your operating system's terminal or command prompt
3. **Navigate to Directory**: Use `cd` command to navigate to the extracted folder path
4. **Run Application**: Execute the following command:
   ```bash
   python3 app.py
   ```
5. **Select Folder**: A file browser window will open—select the folder you wish to organize
6. **Start Organization**: Click the "Start" button to begin the file organization process
7. **View Results**: The application will display a success or error message upon completion
8. **Exit**: Close the window when finished

## How It Works

The application uses Python's file system capabilities to:
- Scan the selected directory for all files
- Categorize files based on their extensions
- Create organized subdirectories as needed
- Move files to their corresponding category folders

## Project Purpose

This project demonstrates proficiency in:
- Python development
- File system operations
- GUI application development with tkinter
- User experience design

## Future Enhancements

Potential improvements for future versions:
- Customizable categorization rules
- Undo functionality
- Detailed logging and file movement history
- Support for nested directory organization

## License

This project is open source and available for personal and educational use.

## Author

Created by Smb7
