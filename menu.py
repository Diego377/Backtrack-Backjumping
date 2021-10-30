from Schedule import Schedule
from Event import Event
from Speaker import Speaker
if (__name__ == '__main__'):
    
    event = Event()
    main = Schedule()
    option = 0
    
    while(option != 6):
        
        print("Choose an option: \n")
        print("1. Check in")
        print("2. Assign a day and time")
        print("3. Show speakers")
        print("4. MRV")
        print("5. Least constrained value")
        option = input()

        if option == "1":
            # print("Which day do you want to register in? Select a number: 1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday")
            # day = input()
            # print("Which hour do you want to register in? Type A for 9 to 12 or B for 15 to 18")
            # hour = input()
            #main.addSpeakTime(int(day),hour)
            cont = 0
            print("Enter the id: ")
            Id = input()
            print("Enter the name: ")
            Name = input()
            print("Is national (Nat) or international (Int)?: ")
            NationalOrInt = input()
            print("Enter the area: ")
            Area = input()
            print("Enter the number of talks: ")
            Talks = input()
            # print("Which day do you want to register in? Select a number: 1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday")
            # day = input()
            # print("Which hour do you want to register in? Type A for 9 to 10, B for 10 to 11, C for 11 to 12, D for 15 to 16, E for 16 to 17 or F for 17 to 18")
            # hour = input()
            
            sp = Speaker(Id,Name,NationalOrInt,Area,Talks)
            
            event.AddSpeaker(sp,Area, NationalOrInt)
            
        if option == "2":
            #main.showSchedule()
            event.showSpeakers()
            print("Select a speaker by id :")
            spId = input()
            print("Which day do you want to register in? Select a number: 1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday")
            day = input()
            print("Which hour do you want to register in? Type A for 9 to 10, B for 10 to 11, C for 11 to 12, D for 15 to 16, E for 16 to 17 or F for 17 to 18")
            hour = input()

            speaker = event.FindSpeaker(spId)
            speaker.removeNextSpeakTime(day,hour)
            event.ForwardChecking(spId,day,hour)
        
        if option == "3":
            #event.sp1 = Speaker(1,'Dudas','Nat','IA')
            for s in event.speakers:
                s.ShowSpeaker()
                # event.sp1.ShowSpeaker()
                # event.sp3.ShowSpeaker()
            
        if option == "4":
            event.showSpeakers()
            print("Select a speaker by id :")
            spId = input()
            event.MRV(spId)

        if option == "5":
            #errores en los dominios vecinos cuando se agrega una hora 
            event.showSpeakers()
            print("Select a speaker by id :")
            spId = input()
            event.LeastConstrainedValue(spId)