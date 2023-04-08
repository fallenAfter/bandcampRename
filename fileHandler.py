
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
            if self.file[len(self.file)-1] == "/":
                self.subFolders.append(File(self.file+subFile))
            if self.file[len(self.file)-1] != "/":
                self.subFolders.append(File(self.file+"/"+subFile))

    def getFileName(self):
        fileParts = self.file.split("/")
        return fileParts[len(fileParts)-1].split(".")[0]
    
    def getFilePath(self):
        output = ''
        fileParts = self.file.split("/")
        counter = 0
        # the last part in fileParts is a 
        while counter < len(fileParts)-1:
            output = output + fileParts[counter]+"/"
            counter = counter + 1
        return output

    def getExtension(self):
        fileParts = self.file.split(".")
        return fileParts[len(fileParts)-1]

    def rename(self, newName):
        path = self.getFilePath()
        os.rename(self.file, path+newName)
    
    def isFileOfType(self, type):
        return self.getExtension() == type

    def copyFileTo(self, target):
        print(target)
    
    def unzipFile(self, target):
        shutil.unpack_archive(self.file, target)

