import numpy as np

# Stores data about speaker
class Speaker:
    # Initializes speaker data
    def __init__(self, Id, name, NationalOrInt,Area, Talks):
        self.Id = Id
        self.Name = name
        self.NationalOrInt = NationalOrInt
        self.Area = Area
        self.Talks = Talks
        #self.SpeakTime = []
        self.Days = []
        self.SpeakTime = {
            65: [1,'A'],
            66: [1,'B'],
            67: [1,'C'],
            68: [1,'D'],
            69: [1,'E'],
            70: [1,'F'],
            130: [2,'A'],
            132: [2,'B'],
            134: [2,'C'],
            136: [2,'D'],
            138: [2,'E'],
            140: [2,'F'],
            195: [3,'A'],
            198: [3,'B'],
            201: [3,'C'],
            204: [3,'D'],
            207: [3,'E'],
            210: [3,'F'],
            260: [4,'A'],
            264: [4,'B'],
            268: [4,'C'],
            272: [4,'D'],
            276: [4,'E'],
            280: [4,'F'],
            325: [5,'A'],
            330: [5,'B'],
            335: [5,'C'],
            340: [5,'D'],
            345: [5,'E'],
            350: [5,'F']
        }
        self.Neighbors = []


    def identifyTime(self,day,hour):
        resp = 0
        resp = ord(hour) * int(day)
        return resp

    # Bind speaker to speak time
    def addSpeakTime(self, day, hour):
        self.Days.append(day)
        #self.removeNextSpeakTime(day,hour)
        #time = self.identifyTime(day,hour)
        #self.SpeakTime.clear()
        aux = self.identifyTime(day,hour)
        self.SpeakTime[aux] = [int(day),hour]
        #self.SpeakTime.append([int(day),hour])
    
    def removeSpeakTime(self,day,hour):
        aux = self.identifyTime(day,hour)
        del self.SpeakTime[aux]
    
    #This is to remove the times ahead and in the back of the time that it's been agregated
    def removeNextSpeakTime(self,day,hour):
        aux = self.identifyTime(day,hour)
        aux = aux + 1
        if int(aux) == self.SpeakTime.keys():
            del(self.SpeakTime[aux])
            # aux = aux - 2
            # if aux == self.SpeakTime.keys():
            #     del self.SpeakTime[aux]
        
        #This is how we know that every talk has been asigned
        if len(self.SpeakTime) + int(self.Talks) == 30:
            self.SpeakTime.clear
            #Add in days the times that are reserved
            for i in self.Days:
                self.identifyTime()
            #self.SpeakTime = self.Days

    def ShowSpeaker(self):
        print("Id: " + str(self.Id))
        print("Name: " + self.Name)
        print("National or international: " + self.NationalOrInt)
        print("Area: " + self.Area)
        print("Days: " + str(self.Days))
        print("Domain: " + str(self.SpeakTime))
        print("Talks: " + str(self.Talks))
        print("Neighbors: " + str(self.Neighbors) + "\n")

    def AddNeighbor(self, idNeighbor):
        self.Neighbors.append(idNeighbor)
    