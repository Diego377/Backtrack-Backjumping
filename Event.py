from Schedule import Schedule
from Speaker import Speaker
from collections import deque

class Event:
    csp = Schedule()
    sp1 = Speaker(1,'Dudas','Nat','IA')
    sp2 = Speaker(2,'Gaby','Nat','Sec')
    sp3 = Speaker(3,'Sammy','Int','IA')
    sp4 = Speaker(4,'Seibu','Int','IngeSoft')
    speakers = [sp1,sp2,sp3,sp4]
    aux = 10

    def ForwardChecking(self,sp,day, hour):

        #sp.addSpeakTime(day,hour)
        # for time in sp.SpeakTime:
        #     if time[] == day:
        #         sp.removeSpeakTime(day,hour)
        Xe = self.FindSpeaker(sp)
        Xe.addSpeakTime(day,hour)
        
        for aux in Xe.Neighbors:
            neighbor = self.FindSpeaker(aux)
            neighbor.removeSpeakTime(day,hour)
            if len(neighbor.SpeakTime) == 0:
                print("Asignacion inconsistente")
            else :
                print("Asignacion consistente")
            #Registrar primero con dominio completo, luego elegir un horario y cambiar el dominio de sus vecinos 
    
    def MRV(speaker):
        orderedValues = deque()
        for Xi in Event.speakers:
            orderedValues.append(Xi,len(Xi.SpeakTime))
        return orderedValues.pop()

    def LeastConstrainedValue(self, speaker):
        stack = []
        AllConstraintValues = stack
        
        for v in speaker.SpeakTime:
            temp_x = self.speakers
            self.ForwardChecking(speaker,v[0],v[1])
            consistentValues = 0
            for Xi in speaker.Neighbors:
                consistentValues = len(Xi.SpeakTime)
            AllConstraintValues.append(v,consistentValues)
            self.speakers = temp_x
        return AllConstraintValues.pop()

    def Backtrack(self, sp, day, hour, w, csp):
        # if assignment.state == 'Complete':
        #     return assignment
        var = self.MRV()
        self.LeastConstrainedValue(var)
        self.ForwardChecking(var,day,hour)
        
    def AddSpeaker(self, sp, Area):
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

        for speaker in self.speakers:
            if speaker.Area == Area:
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