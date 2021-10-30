import numpy as np
# Stores data about speaker
class Speaker:
    # Initializes speaker data
    def __init__(self, id, name, NationalOrInt,Area, Talks):
        self.Id = id
        self.Name = name
        self.NationalOrInt = NationalOrInt
        self.Area = Area
        #self.SpeakTime = []
        self.Days = []
        self.SpeakTime = {
            66: [1,'A'],
            67: [1,'B'],
            68: [1,'C'],
            69: [1,'D'],
            70: [1,'E'],
            71: [1,'F']
        }
        #[[1,'A'],[1,'B'],[1,'C'],[1,'D'],[1,'E'],[1,'F']],[2,'A'],[2,'B'],[2,'C'],[2,'D'],[2,'E'],[2,'F']]
        # [3,'A'],[3,'B'],[3,'C'],[3,'D'],[3,'E'],[1,'F'],[4,'A'],[4,'B'],[4,'C'],[4,'D'],[4,'E'],[4,'F'],
        # [5,'A'],[5,'B'],[5,'C'],[5,'D'],[5,'E'],[5,'F']]
        self.Neighbors = []
        self.Talks = Talks

    #def fillSpeakTime():


    def identifyTime(self,day,hour):
        resp = 0
        resp = ord(hour) + int(day)
        return resp

    # Bind speaker to speak time
    def addSpeakTime(self, day, hour):
        self.Days.append(day)
        self.SpeakTime.clear()
        self.SpeakTime.append([int(day),hour])
    
    def removeSpeakTime(self,day,hour):
        aux = self.identifyTime(day,hour)
        del self.SpeakTime[aux]

    def ShowSpeaker(self):
        print("Id: " + str(self.Id))
        print("Name: " + self.Name)
        print("National or international: " + self.NationalOrInt)
        print("Area: " + self.Area)
        print("Days: " + str(self.Days))
        print("Domain: " + str(self.SpeakTime))
        print("Talks:" + str(self.Talks))
        print("Neighbors: " + str(self.Neighbors) + "\n")

    def AddNeighbor(self, idNeighbor):
        self.Neighbors.append(idNeighbor)
    