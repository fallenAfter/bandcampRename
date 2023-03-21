from fileHandler import File
from config import Config
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
            file.unzipFile(self.zipExtractLocation)

Program()