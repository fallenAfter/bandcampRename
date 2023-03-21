import os
import json
class Config:
    def __init__(self):
        self.configLocation = os.path.dirname(os.path.abspath(__file__))

    def loadConfig(self):
        print(self.configLocation)
        f = open(self.configLocation+"/config.json")
        self.data = json.load(f)
        f.close()
        return self.data

    def getConfig(self):
        return self.data