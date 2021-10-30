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
        # if(day == 1):
        #     if(hour == 'A'):
        #         resp = 1
        #     if(hour == 'B'):
        #         resp = 2
        #     if(hour == 'C'):
        #         resp = 3
        #     if(hour == 'D'):
        #         resp = 4
        #     if(hour == 'E'):
        #         resp = 5
        #     if(hour == 'F'):
        #         resp = 6
        # if(day == 2):
        #     if(hour == 'A'):
        #         resp = 7
        #     if(hour == 'B'):
        #         resp = 8
        #     if(hour == 'C'):
        #         resp = 9
        #     if(hour == 'D'):
        #         resp = 10
        #     if(hour == 'E'):
        #         resp = 11
        #     if(hour == 'F'):
        #         resp = 12
        # if(day == 3):
        #     if(hour == 'A'):
        #         resp = 13
        #     if(hour == 'B'):
        #         resp = 14
        #     if(hour == 'C'):
        #         resp = 15
        #     if(hour == 'D'):
        #         resp = 16
        #     if(hour == 'E'):
        #         resp = 17
        #     if(hour == 'F'):
        #         resp = 18
        # if(day == 4):
        #     if(hour == 'A'):
        #         resp = 19
        #     if(hour == 'B'):
        #         resp = 20
        #     if(hour == 'C'):
        #         resp = 21
        #     if(hour == 'D'):
        #         resp = 22
        #     if(hour == 'E'):
        #         resp = 23
        #     if(hour == 'F'):
        #         resp = 24
        # if(day == 5):
        #     if(hour == 'A'):
        #         resp = 25
        #     if(hour == 'B'):
        #         resp = 26
        #     if(hour == 'C'):
        #         resp = 27
        #     if(hour == 'D'):
        #         resp = 28
        #     if(hour == 'E'):
        #         resp = 29
        #     if(hour == 'F'):
        #         resp = 30
        # return resp

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
    
    