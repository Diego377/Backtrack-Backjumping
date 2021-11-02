from Schedule import Schedule
from Speaker import Speaker
from collections import deque
from queue import PriorityQueue
import json


class Event:
    csp = Schedule()
    speakers = []

    def ForwardChecking(self,sp,day, hour):
        
        Xe = self.FindSpeaker(sp)
        cont = 0

        for aux in Xe.Neighbors:
            neighbor = self.FindSpeaker(aux)
            if cont == 0:
                copy = neighbor.SpeakTime.copy()
                cont = 1

            aux2 = neighbor.identifyTime(day,hour)
            if aux2 in neighbor.SpeakTime.keys():
                neighbor.removeSpeakTime(day,hour)
            #neighbor.SpeakTime = copy

            if len(neighbor.SpeakTime) == 0:
                print("Inconsistent assignment")
            else :
                print("Consistent assignment")
        
        #Xe.SpeakTime = copy
    
    def MRV(self, idSpeaker):

        orderedValues = PriorityQueue()
        size = 30
        Xi = self.FindSpeaker(idSpeaker)
        for aux in Xi.Neighbors:
            neighbor = self.FindSpeaker(aux)
            if len(neighbor.SpeakTime) < size:
                orderedValues.put([len(neighbor.SpeakTime),neighbor.Name])
        
        resp = orderedValues.get()
        print(resp)
        return resp

        # orderedValues = deque()
        # for Xi in Event.speakers:
        #     orderedValues.append(Xi,len(Xi.SpeakTime))
        # return orderedValues.pop()

    def LeastConstrainedValue(self, idSpeaker):
        
        sp = self.FindSpeaker(idSpeaker)

        temp_x = sp.SpeakTime.copy()

        stack = []
        AllConstraintValues = stack

        for v in sp.SpeakTime:
            self.ForwardChecking(sp.Id,sp.SpeakTime[v][0],sp.SpeakTime[v][1])

            consistentValues = 0
            
            for aux in sp.Neighbors:
                neighbor = self.FindSpeaker(aux)
                consistentValues = consistentValues + len(neighbor.SpeakTime)

            AllConstraintValues.append([v,consistentValues])

            sp.SpeakTime = temp_x

        print( AllConstraintValues)
        return AllConstraintValues

    def Backtrack(self, sp, day, hour, w, csp):
        # if assignment.state == 'Complete':
        #     return assignment
        var = self.MRV()
        self.LeastConstrainedValue(var)
        self.ForwardChecking(var,day,hour)
        
    def AddSpeaker(self, sp, Area, NationalOrInt):

        #Neighbors are addedd if the "area" or the "national or international" values are the same
        for speaker in self.speakers:
            if speaker.Area == Area:
                speaker.AddNeighbor(sp.Id)
                sp.AddNeighbor(speaker.Id)
            if speaker.NationalOrInt == 'int' and speaker.NationalOrInt == NationalOrInt:
                speaker.AddNeighbor(sp.Id)
                sp.AddNeighbor(speaker.Id)
            # for d in sp.Days:
            #     if d == day:
            #         speaker.AddNeighbor(sp.Id)
            #         sp.AddNeighbor(speaker.Id)

        self.speakers.append(sp)

        #self.ForwardChecking(sp,int(day),hour)

    def FindSpeaker(self, idSpeaker):
        for sp in self.speakers:
            if int(sp.Id) == int(idSpeaker):
                return sp

    def showSpeakers(self):
        for i in self.speakers:
            i.ShowSpeaker()

    def readFile(self):
        with open('data.json') as file:
            data = json.load(file)
        for speaker in data['speakers']:
            sp = Speaker(int(speaker['Id']),speaker['Name'],speaker['NatOrInt'],speaker['Area'],speaker['Talks'])
            self.AddSpeaker(sp,sp.Area,sp.NationalOrInt)
