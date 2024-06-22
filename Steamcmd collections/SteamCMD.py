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
    steamcmd_script = os.path.join(os.getcwd(), 'steamcmd_script.txt')
    with open(steamcmd_script, 'w') as script_file:
        script_file.write('login anonymous\n')
        script_file.write(f'force_install_dir {download_location}\n')
        for command in commands:
            script_file.write(command)
        script_file.write('\nquit\n')

    print(f"Running SteamCMD with script {steamcmd_script}...")

    # Run the SteamCMD script
    try:
        # Use communicate() to interact with SteamCMD
        process = subprocess.Popen([steamcmd_path, '+runscript', steamcmd_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Communicate with the process and handle output
        while process.poll() is None:
            output = process.stdout.readline()
            if output:
                print(output.strip())

        # Check for any remaining output
        remaining_output = process.communicate()[0]
        if remaining_output:
            print(remaining_output.decode().strip())

        # Check for errors
        stderr = process.stderr.read()
        if stderr:
            print(f"Error running SteamCMD: {stderr}")

    except Exception as e:
        print(f"Exception occurred while running SteamCMD: {e}")

    finally:
        # Clean up: delete the temporary SteamCMD script
        if os.path.exists(steamcmd_script):
            os.remove(steamcmd_script)

if __name__ == "__main__":
    steamcmd_path = get_file_path("SteamCMD executable")
    if steamcmd_path:
        workshop_file = get_file_path("workshop text file")
        if workshop_file:
            download_location = get_directory_path("download")
            if download_location:
                download_workshop_items(steamcmd_path, workshop_file, download_location)
