# SteamCMD_Collections_Downloader
 
> [!NOTE]
> Some games on Steam and their corrasponding workshop mods are not available for download using the anonymous login
option that is provided by SteamCMD

Taking the URL from the Steam page for the chosen collection, visit https://steamworkshopdownloader.io/ and paste 
said URL.

After loading, select [Yes} for "Question: do you know what SteamCMD is and are you logged into it?"

then just, ctrl+a the page and paste your clipboard in place of the example text in the import_re.py file and then run the script.


### Move to and run SteamCMD.py  

>[!NOTE]
>Keep in mind this is gonna run "login anonymous" and not "login your_username your_password"

>[!TIP]
> Download information for SteamCMD https://developer.valvesoftware.com/wiki/SteamCMD#Windows:~:text=See%20Also-,Downloading%20SteamCMD,-Windows

Follow the steps
1. select SteamCMD.exe
2. select the text file that was created in the first step
3. select download location (This should not be the games mod folder, as it comes with "fluff" files)

After finishing the above steps, naviage to the download folder and to "...\steamapps\workshop\content"
this is the base folder that holds the individual mod folders, which need to be cleaned

### Run rename_folders.py
select the Base folder and wait
afterwards the subfolders within the base folder will have the correct names and will now be ready to be moved to the games mod folder
