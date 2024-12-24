import zipfile
import os
import io
import traceback
import subprocess
def unzip_file(zip_file_path, extract_to='.'):
    try:
        # Read the ZIP file into memory
        print(f"Reading ZIP file: {zip_file_path}")
        with open(zip_file_path, 'rb') as zip_file:
            zip_data = zip_file.read()

        # Delete the ZIP file
        print(f"Deleting ZIP file: {zip_file_path}")
        os.remove(zip_file_path)

        # Extract the ZIP file from memory
        print(f"Extracting files to: {extract_to}")
        with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Unzipped successfully to {os.path.abspath(extract_to)}")

        # List the folders after extracting
        print("Listing folders:")
        if not os.path.exists(extract_to):
            print("Error: Extraction path does not exist.")
            return
        for root, dirs, files in os.walk(extract_to):
            for dir_name in dirs:
                print(f"Folder: {os.path.join(root, dir_name)}")

    except Exception as e:
        print("An unexpected error occurred:")
        traceback.print_exc()

# Example usage
zip_file_path = 'zip.zip'  # Replace with your file path
extract_to = '.'  # Replace with your desired extraction path
unzip_file(zip_file_path, extract_to)


subprocess.run(["python", "main.py"], check=True)
