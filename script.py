import os

# Replace 'folder_path' with the path to your folder containing the files
folder_path = 'X:\Back color'
path=os.getcwd()
print(path)
def remove_spaces_from_filenames(folder):

    try:
        # Iterate through each file in the directory
        for filename in os.listdir(folder):
            old_filepath = os.path.join(folder, filename)

            # Remove spaces from the filename
            new_filename = filename.replace(' ', '')
            new_filepath = os.path.join(folder, new_filename)

            # Rename the file without spaces in the filename
            os.rename(old_filepath, new_filepath)
            print(f"Removed spaces: {filename} to {new_filename}")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to remove spaces from filenames in the specified folder
remove_spaces_from_filenames(folder_path)
