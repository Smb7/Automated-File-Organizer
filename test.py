import unittest
import os
from FileOrganizer import FileOrganizer  # Adjust the import according to your actual file structure
import tempfile
import shutil

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_empty_directory(self):
        organizer = FileOrganizer()
        result = organizer.organize_files_by_extension(self.test_dir)
        self.assertEqual(result, "Error: Directory is empty")

    def test_organize_files(self):
        # Setup - create some dummy files
        files_and_folders = {
            '.png': 'PngFiles',
            '.txt': 'TextFiles',
            '.pdf': 'PdfFiles',
            '.docx': 'WordFiles',
            '.xlsx': 'ExcelFiles',
        }
        for ext in files_and_folders.keys():
            with open(os.path.join(self.test_dir, f"test{ext}"), 'w') as temp_file:
                temp_file.write("This is a test.")

        organizer = FileOrganizer()
        result = organizer.organize_files_by_extension(self.test_dir)
        
        self.assertEqual(result, "Operation Successful")
        for ext, folder in files_and_folders.items():
            folder_path = os.path.join(self.test_dir, folder)
            self.assertTrue(os.path.isdir(folder_path), f"{folder_path} does not exist")
            file_path = os.path.join(folder_path, f"test{ext}")
            self.assertTrue(os.path.exists(file_path), f"{file_path} was not moved correctly")

if __name__ == '__main__':
    unittest.main()
