
import os
import shutil

class File(object):
    def __init__(self, file):
        self.file = file
        self.subFolders = None
        self.extention = None
        self.isFolder = os.path.isdir(os.path.join(file))
        if self.isFolder:
            self.mapSubFolders()
            
    def mapSubFolders(self):
        if self.subFolders == None:
            self.subFolders = []
        for subFile in os.listdir(self.file):
                self.subFolders.append(File(self.file+subFile))

    def getFileName(self):
        fileParts = self.file.split("/")
        return fileParts[len(fileParts)-1].split(".")[0]

    def getExtension(self):
        fileParts = self.file.split(".")
        return fileParts[len(fileParts)-1]

    def renameFile(self, newName):
        self.file
    
    def isFileOfType(self, type):
        return false

    def copyFileTo(self, target):
        print(target)
    
    def unzipFile(self, target):
        shutil.unpack_archive(self.file, target)

