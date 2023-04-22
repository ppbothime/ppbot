from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def getGoogleAuth():

    gauth = GoogleAuth()
    drive_auth = GoogleDrive(gauth)

    return drive_auth
