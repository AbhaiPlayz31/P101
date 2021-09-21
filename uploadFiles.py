import dropbox
import os

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, fileFrom, fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                localPath = os.path.join(root,fileName)
                path = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, path)
                with open(localPath, 'rb')as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overwrite')
                    

def main():
    accessToken='74-gnWLkl4cAAAAAAAAAAYbWHePBcNAyLX5KQkPjXTvC_1HASt4ldXmMbaT-02PB'
    transferData = TransferData(accessToken)
    fileFrom = input('Enter the file to be sent: ')
    fileTo = input('Enter the destination: ')
    transferData.uploadFiles(fileFrom, fileTo)

    print('FIle has been successfully moooooooved! :>')

main()
                

    