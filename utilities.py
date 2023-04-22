import random
from auth import *

def getRandomFile():
    drive = getGoogleAuth()
    print("GETTING A FILE")
    # Filter file_list to only include files with an `.mkv` extension
    file_list = drive.ListFile({'q': "title contains '.mkv' and trashed=false"}).GetList()
    # If no files with `.mkv` extension found, return None
    if not file_list:
        return None
    file = random.choice(file_list)
    title = file['title']
    extension = title.split(".")[1]

    # downloads file, which is deleted later
    file.GetContentFile(title)

    return {'title': title, 'extension': extension}
