import zipfile
import os
import subprocess

def unzip_file(zip_file_path, extract_to='.'):
    try:
        # Check if the file is a valid ZIP archive
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.testzip()  # Test the archive to ensure it's valid

        # Delete the ZIP file before extracting
        os.remove(zip_file_path)
        print(f"Deleted ZIP file: {os.path.abspath(zip_file_path)}")

        # Extract contents
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Unzipped successfully to {os.path.abspath(extract_to)}")

    except zipfile.BadZipFile:
        print("Error: The file is not a valid ZIP archive.")
    except FileNotFoundError:
        print("Error: The specified ZIP file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
zip_file_path = 'zip.zip'  # replace with your file path
extract_to = ''  # replace with your desired extraction path
unzip_file(zip_file_path, extract_to)

subprocess.run(["python", "main.py"], check=True)
