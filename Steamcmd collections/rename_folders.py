import os
import tkinter as tk
from tkinter import filedialog, messagebox

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

def select_base_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt user to select the base folder
    base_folder = filedialog.askdirectory(title="Select Base Folder Containing Subfolders")
    
    if base_folder:
        rename_folders(base_folder)
        
        # Show completion message
        messagebox.showinfo("Operation Completed", "Folder renaming operation completed.")
    else:
        messagebox.showerror("Error", "No base folder selected. Operation aborted.")

if __name__ == "__main__":
    # Call the function to select the base folder and rename folders
    select_base_folder()
