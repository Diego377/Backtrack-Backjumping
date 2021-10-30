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

        #sp.addSpeakTime(day,hour)
        # for time in sp.SpeakTime:
        #     if time[] == day:
        #         sp.removeSpeakTime(day,hour)
        Xe = self.FindSpeaker(sp)
        #Copy is made in case the assignment is inconsistent and we need to restore the values of the domain
        #copy = Xe.SpeakTime.copy() 
        #Xe.addSpeakTime(day,hour)

        for aux in Xe.Neighbors:
            neighbor = self.FindSpeaker(aux)
            copy = neighbor.SpeakTime.copy()
            neighbor.removeSpeakTime(day,hour)

            if len(neighbor.SpeakTime) == 0:
                print("Inconsistent assignment")
            else :
                print("Consistent assignment")
        neighbor.SpeakTime = copy
        
        Xe.SpeakTime = copy
    
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
            #print("prueba:" + str(v[0])+","+str(v[1]))
            #sp.removeSpeakTime(sp.SpeakTime[v][0],sp.SpeakTime[v][1])

        print( AllConstraintValues)
        return AllConstraintValues

    def Backtrack(self, sp, day, hour, w, csp):
        # if assignment.state == 'Complete':
        #     return assignment
        var = self.MRV()
        self.LeastConstrainedValue(var)
        self.ForwardChecking(var,day,hour)
        
    def AddSpeaker(self, sp, Area, NationalOrInt):
        # print("Enter the id: ")
        # Id = input()
        # print("Enter the name: ")
        # Name = input()
        # print("Is national (Nat) or international (Int)?: ")
        # NationalOrInt = input()
        # print("Enter the area: ")
        # Area = input()
        # print("Which day do you want to register in? Select a number: 1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday")
        # day = input()
        # print("Which hour do you want to register in? Type A for 9 to 10, B for 10 to 11, C for 11 to 12, D for 15 to 16, E for 16 to 17 or F for 17 to 18")
        # hour = input()
        # sp = Speaker(Id,Name,NationalOrInt,Area)
        #sp.addSpeakTime(day,hour)

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