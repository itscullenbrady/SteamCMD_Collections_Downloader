import re
import tkinter as tk
from tkinter import filedialog

def extract_workshop_items(text):
    # Define the regular expression pattern to match workshop_download_item lines
    pattern = r'workshop_download_item \d+ \d+'

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Join the matches with newline character to separate each match into its own line
    result = '\n'.join(matches)

    return result

# Example text
text = """
Steam Workshop Downloader
Want to download files from the steam workshop? This website will show you how it's done.

Enter the file you want to download and follow the interactive tutorial.

https://steamcommunity.com/sharedfiles/filedetails/?id=2180342763
256 Recruitment Limit
256 Recruitment Limit   Created: 2016-06-17 00:11   Updated: 2018-04-19 16:32
Game: Kenshi
Size: ~ 690 kB ?
Usually works with anonymous login.
By using Steam or any affiliated software, you have to agree with the Steam Subscriber Agreement.
We are not responsible for any issues or damages that may arise from using this tutorial.
1. Please enter the following command into SteamCMD and press enter:
workshop_download_item 233860 705119823 
Hint 1: You can use Ctrl+V hotkey, or right click on title bar -> edit -> paste to paste the command!
2. Wait for the download to complete. There is no progress bar!
3. Go to the folder that is shown on the screen. Your download is here!

Did you get an error? Try logging in with a real account that owns the game. Otherwise, the game is unsupported and you should buy it.
KenshICONS
KenshICONS   Created: 2017-08-08 14:23   Updated: 2017-10-01 22:01
Game: Kenshi
Size: ~ 1.36 MB ?
Usually works with anonymous login.
By using Steam or any affiliated software, you have to agree with the Steam Subscriber Agreement.
We are not responsible for any issues or damages that may arise from using this tutorial.
1. Please enter the following command into SteamCMD and press enter:
workshop_download_item 233860 1104521739 
Hint 1: You can use Ctrl+V hotkey, or right click on title bar -> edit -> paste to paste the command!
2. Wait for the download to complete. There is no progress bar!
3. Go to the folder that is shown on the screen. Your download is here!

Did you get an error? Try logging in with a real account that owns the game. Otherwise, the game is unsupported and you should buy it.
"""

# Extract workshop items
extracted_items = extract_workshop_items(text)

# Set up the Tkinter root
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file save dialog
file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

# Save the extracted items to the selected file
if file_path:
    with open(file_path, 'w') as file:
        file.write(extracted_items)
    print(f"Extracted workshop items saved to {file_path}")
else:
    print("Save operation cancelled.")
