import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def get_file_path(file_type):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=f"Select {file_type} file", filetypes=[("All Files", "*.*")])
    if not file_path:
        messagebox.showerror("Error", f"No {file_type} file selected.")
    return file_path

def get_directory_path(directory_type):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    directory_path = filedialog.askdirectory(title=f"Select {directory_type} directory")
    if not directory_path:
        messagebox.showerror("Error", f"No {directory_type} directory selected.")
    return directory_path

def download_workshop_items(steamcmd_path, workshop_file, download_location):
    if not os.path.exists(workshop_file):
        print(f"Error: {workshop_file} not found.")
        return

    with open(workshop_file, 'r') as file:
        commands = file.readlines()

    if not commands:
        print(f"No commands found in {workshop_file}.")
        return

    # Create a SteamCMD script
    steamcmd_script = 'steamcmd_script.txt'
    with open(steamcmd_script, 'w') as script_file:
        script_file.write('login anonymous\n')
        script_file.write(f'force_install_dir {download_location}\n')
        for command in commands:
            script_file.write(command)
        script_file.write('quit\n')

    # Run the SteamCMD script
    result = subprocess.run([steamcmd_path, '+runscript', steamcmd_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print(f"Error running SteamCMD: {result.stderr.decode()}")
    else:
        print(f"Successfully ran SteamCMD script:\n{result.stdout.decode()}")

if __name__ == "__main__":
    steamcmd_path = get_file_path("SteamCMD executable")
    if steamcmd_path:
        workshop_file = get_file_path("workshop text file")
        if workshop_file:
            download_location = get_directory_path("download")
            if download_location:
                download_workshop_items(steamcmd_path, workshop_file, download_location)
