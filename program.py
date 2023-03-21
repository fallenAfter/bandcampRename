from fileHandler import File
from config import Config
import re
class Program:
    def __init__(self):
        self.config = Config().loadConfig()
        # in the future allow this to be overridable in some way
        self.rootFileLocation = self.config['directories']['rootFileLocation']
        self.bandcampDlFile = self.rootFileLocation+self.config['directories']['defaultInputFolder']
        self.zipExtractLocation = self.rootFileLocation+self.config['directories']['zipExtractLocation']
        self.run()
        

    def run(self):
        # run the program
        print('run')
        self.getDownloadedMusicFromSource()
        
    def getDownloadedMusicFromSource(self):
        filesChecked = 0
        unprocessedFilesLocation = File(self.bandcampDlFile)
        for subfile in unprocessedFilesLocation.subFolders:
            filesChecked= filesChecked +1
            print("("+str(filesChecked)+"/"+str(len(unprocessedFilesLocation.subFolders))+"): "+subfile.getFileName())
            self.unzipBandcampFiles(subfile)
        
    def unzipBandcampFiles(self, file):
        if file.getExtension() == "zip":
            albumSubFolder = self.generatPathForAlbumOutput(file)
            print(self.zipExtractLocation)
            file.unzipFile(self.zipExtractLocation+albumSubFolder)

    def generatPathForAlbumOutput(self, file):
        fileParts = self.seperateBandcampNameIntoParts(file)
        return fileParts[0]+"/"+fileParts[1]+"/"

    # returned array indexes should represent: [0]artist [1]album name
    def seperateBandcampNameIntoParts(self, file):
        result = re.findall(r"((\w|\s)*\w)\s\-\s((\w|\s)*\w)", file.getFileName())
        return [result[0][0], result[0][2]]


Program()
