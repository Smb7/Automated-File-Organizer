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
            ".xlsx": "ExcelFiles",
            ".py" : "PythonFiles",
            ".cs" : "CSharpFiles"
        }

        folder_types = {
            "python": "PythonProjects",
            "py" : "PythonProjects",
            "csharp": "CSharpProjects",
            "c#" : "CSharpProjects"
        }

        # Organize files
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1]
                if file_extension in file_types:
                    dir_name = file_types[file_extension]
                    new_path = os.path.join(path, dir_name)
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                    shutil.move(item_path, new_path)
            
            # Organize folders
            elif os.path.isdir(item_path):
                for keyword, folder_name in folder_types.items():
                    if keyword in item.lower():
                        new_path = os.path.join(path, folder_name)
                        if not os.path.exists(new_path):
                            os.makedirs(new_path)
                        shutil.move(item_path, new_path)
                        break

        return "Operation Successful"

