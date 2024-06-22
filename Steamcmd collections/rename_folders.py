import os

# Function to sanitize the folder name
def sanitize_folder_name(name):
    # Remove invalid characters for Windows folder names
    return name.strip().replace('\0', '')

# Function to rename folders
def rename_folders(base_folder):
    # Iterate through each folder in the base folder
    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)
        
        if os.path.isdir(folder_path):
            # Look for the .mod file in the current folder
            for file in os.listdir(folder_path):
                if file.endswith(".mod"):
                    mod_file_path = os.path.join(folder_path, file)
                    
                    # Extract the name of the .mod file (excluding the extension)
                    new_name = os.path.splitext(file)[0]
                    new_name = sanitize_folder_name(new_name)
                    print(f"Extracted new name: '{new_name}' from {mod_file_path}")
                    
                    # Ensure the new name is valid
                    if new_name:
                        new_folder_path = os.path.join(base_folder, new_name)
                        
                        try:
                            # Rename the folder
                            os.rename(folder_path, new_folder_path)
                            print(f"Renamed '{folder}' to '{new_name}'")
                            break
                        except Exception as e:
                            print(f"Error renaming '{folder_path}' to '{new_folder_path}': {e}")
                    else:
                        print(f"No valid name found for {mod_file_path}")

# Define the path to your base folder containing subfolders
base_folder = r"D:\games\Kenshi\mods"

# Call the function to rename folders
rename_folders(base_folder)
