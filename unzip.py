import zipfile
import os
import subprocess
import io

def unzip_file(zip_file_path, extract_to='.'):
    try:
        # Read the ZIP file into memory
        with open(zip_file_path, 'rb') as zip_file:
            zip_data = zip_file.read()

        # Delete the ZIP file
        os.remove(zip_file_path)
        print(f"Deleted ZIP file: {os.path.abspath(zip_file_path)}")

        # Extract the ZIP file from memory
        with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Unzipped successfully to {os.path.abspath(extract_to)}")

        # List the folders after extracting
        print("Listing folders:")
        for root, dirs, files in os.walk(extract_to):
            # Only print directories (folders)
            for dir_name in dirs:
                print(os.path.join(root, dir_name))

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
