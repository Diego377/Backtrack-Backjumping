#Stores the data about the schedule
class Schedule:
    #Initializes the schedule
    def __init__(self):
        #Each sub list represents a day
        # self.schedule = [['Free','Free','Free','Free','Free','Free'],['Free','Free','Free','Free','Free','Free'],['Free','Free','Free','Free','Free','Free']
        # ,['Free','Free','Free','Free','Free','Free'],['Free','Free','Free','Free','Free','Free']]
        self.schedule = {
            1 : ['A F','B F','C F','D F','E F','F F'],
            2 : ['A F','B F','C F','D F','E F','F F'],
            3 : ['A F','B F','C F','D F','E F','F F'],
            4 : ['A F','B F','C F','D F','E F','F F'],
            5 : ['A F','B F','C F','D F','E F','F F'],
            6 : ['A F','B F','C F','D F','E F','F F'],
        }

    # Bind speaker to speak time
    def addSpeakTime(self, day, hour):
        i = 0
        j = 0
        if(day == 1):
            i = 0
        if(day == 2):
            i = 1
        if(day == 3):
            i = 2
        if(day == 4):
            i = 3
        if(day == 5):
            i = 4
        if(day == 6):
            i = 5
        if(hour == 'A'):
            j = 0
        if(hour == 'B'):
            j = 1
        if(hour == 'C'):
            j = 2
        if(hour == 'D'):
            j = 3
        if(hour == 'E'):
            j = 4
        if(hour == 'F'):
            j = 5

        if(self.schedule[i][j] == 'Occupied'):
            print("The date is occupied, please choose another \n check the schedule first! \n")
        else:
            self.schedule[i][j] = 'Occupied'
        #print(self.schedule[i][j])

    def showSchedule(self):
        for i in range(len(self.schedule)):
            print('[')
            for j in range(len(self.schedule[i])):
                print (self.schedule[i][j])
            print (']')
