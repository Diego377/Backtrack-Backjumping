from Schedule import Schedule
from Speaker import Speaker
from collections import deque
from queue import PriorityQueue

class Event:
    csp = Schedule()
    sp1 = Speaker(1,'Diego','Nat','SI',3)
    sp2 = Speaker(2,'Gabriela','Nat','Inge Soft',2)
    sp3 = Speaker(3,'Sam','Int','Inge soft',3)
    sp4 = Speaker(4,'Sebas','Int','IA',4)
    speakers = [sp1,sp2,sp3,sp4]
    aux = 10

    def ForwardChecking(self,sp,day, hour):
        
        Xe = self.FindSpeaker(sp)
        cont = 0
        #Copy is made in case the assignment is inconsistent and we need to restore the values of the domain
        #copy = Xe.SpeakTime.copy() 
        #Xe.addSpeakTime(day,hour)=

        for aux in Xe.Neighbors:
            neighbor = self.FindSpeaker(aux)
            if cont == 0:
                copy = neighbor.SpeakTime.copy()
                cont = 1

            neighbor.removeSpeakTime(day,hour)
            neighbor.SpeakTime = copy

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
            if speaker.NationalOrInt == NationalOrInt:
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
            if sp.Id == idSpeaker:
                return sp

    def showSpeakers(self):
        for i in self.speakers:
            i.ShowSpeaker()