from fileHandler import File
from config import Config
import re
class Program:
    def __init__(self):
        self.config = Config().loadConfig()
        # TODO: Allow file paaths to be overriden by user input
        self.rootFileLocation = self.config['directories']['rootFileLocation']
        self.bandcampDlFile = self.rootFileLocation+self.config['directories']['defaultInputFolder']
        self.zipExtractLocation = self.rootFileLocation+self.config['directories']['zipExtractLocation']

        # TODO: find a better spot to store commoon data types
        self.bandcampMusicFileTypes = {'wav'}

        self.run()
        

    def run(self):
        self.getDownloadedMusicFromSource()
        # TODO: rename songs to not include artist and album information
        
    def getDownloadedMusicFromSource(self):
        # TODO create method for generating process displays
        filesChecked = 0
        unprocessedFilesLocation = File(self.bandcampDlFile)
        # TODO: refactor this to run inside the run() method
        for subfile in unprocessedFilesLocation.subFolders:
            filesChecked= filesChecked +1
            print("("+str(filesChecked)+"/"+str(len(unprocessedFilesLocation.subFolders))+"): "+subfile.getFileName())
            self.unzipBandcampFiles(subfile)
        
    def unzipBandcampFiles(self, file):
        # TODO: move "zip" to a variable, or a dictionary
        if file.getExtension() == "zip":
            albumSubFolder = self.generatPathForAlbumOutput(file)
            file.unzipFile(self.zipExtractLocation+albumSubFolder)

    def generatPathForAlbumOutput(self, file):
        fileParts = self.seperateBandcampNameIntoParts(file)
        return fileParts[0]+"/"+fileParts[1]+"/"

    # returned array indexes should represent: [0]artist [1]album name
    def seperateBandcampNameIntoParts(self, file):
        # re: bandcamp zip file format [artist name] - [album - name] regex selects words with spaces and digits
        # use {,64} instead of ungreedy characters due to possible re performance issues
        result = re.search(r"((?:\w|\s|\d){,64}(?:\w|\d))\s\-\s((?:\w|\s|\d){,64}(?:\w|\d))", file.getFileName()).groups()
        return [result[0], result[1]]


Program()
