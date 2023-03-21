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
        # re: bandcamp zip file format [artist name] - [album - name] regex selects words with spaces and digits, but must end with word or digit up to 64 characters for each
        result = re.search(r"((?:\w|\s|\d){,64}(?:\w|\d))\s\-\s((?:\w|\s|\d){,64}(?:\w|\d))", file.getFileName()).groups()
        return [result[0], result[1]]


Program()
