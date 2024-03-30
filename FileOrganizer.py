# file_organizer.py

import os
import shutil

class FileOrganizer:
    def organize_files_by_extension(self, path):
        if not os.listdir(path):
            return "Error: Directory is empty"

        file_types = {
            ".png": "PngFiles",
            ".txt": "TextFiles",
            ".pdf": "PdfFiles",
            ".docx": "WordFiles",
            ".xlsx": "ExcelFiles"
        }

        for file in os.listdir(path):
            file_extension = os.path.splitext(file)[1]
            if file_extension in file_types:
                dir_name = file_types[file_extension]
                new_path = os.path.join(path, dir_name)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                shutil.move(os.path.join(path, file), new_path)

        return "Operation Successful"
