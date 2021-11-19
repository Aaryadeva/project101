import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A7R7Ib4WXMKAeDrSuMLPkNKunxlpSq0ybT89U1tipJF_xv82jatuE1FJWEO6VWA2yMSp4_7NBmFdrE1a_4fu3g0oJKK3GFADY7LiOoYXqIICidqP3JxbFtVeldZfs9P5CHRrhII'
    transferData = TransferData(access_token)

    file_from = str(input("Enter folder path: "))
    file_to = input("Enter dropbox path: ")  

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file was uploaded")

main()