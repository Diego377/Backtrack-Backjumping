# Backtrack-Backjumping
## Context
The problem to solve is about an event in the Universidad Catolica Boliviana where they organize an event and there are both nationals and internationals speakers to give talks about interesting subjects and relevants in the informatic area.
There are three areas: Informatic Security (Inf Sec), Software engineering (Soft eng) and Artificial Intelligence (AI).
The talks hours are from monday to friday, from 9 to 12 and from 15 to 18.
The Committee wants us to make an informatic program to organize the schedule.

## Propose the problem as a CSP
- First we have the **variables**, these were defined as the talks, having a speaker already assigned.
- Then we have the **domains**, thse were defined to be the time spaces 
- And finally we have the **constraints**:
  - A speaker can have 5 talks in the same area but they can not give 2 talks in a row.
  - Two speakers of the same area will not have assigned one same hour for their talks.
  - Two international guests should not have a talk at the same hour.

## Implementation
- We have a class named speaker which has an initializer with all the attributes that a speaker has, such as id, name, if it is national or international, the area, number of talks and a speak time which represents the spaces of time.
  To make is easy to understand and to work with, the hours are divided with letters. The first hour, 9 to 10, is represented with the letter A, the second hour, 10 to 11, with the letter B and so on until the last hour of a day which is 17 to 18 represented with the letter F.
  And also the days have a different representation, for monday is 1, tuesday 2, wednesday 3, thursday 4 and friday 5.
  The speak time is represented with a dictionary where the keys are the ascii codes of the letters of the hours multiplied by the day that corresponds. It is multiplied so that we can generate a unique code for every hour.
  For example, if the day is tuesday (2) from 10 to 11 (B), the ascii code for B is 66 so 66 * 2 is 132 and that is going to be the key that represents that time.
  Every time that a speaker is addedd we check the area and the nationality so that we can say if that speaker has a neighbor or not.
- Then we have a class named event in which we have everything that is going on through the event. On this class we have a list of speakers that starts empty. It can be filled manually or by reading the **json file** that is in the archives of the respository.
  Also in this class are all the algorithms implemented.
  
 ## Experiments
 The first thing to do is to get a list of speakers, for the experiment this is done by reading the json file with the option 6 from the menu.
 The json file looks like this:
 
 ![image](https://user-images.githubusercontent.com/58644744/140085793-f226c8e1-eb41-411f-bbc6-2590e76b9023.png)

 On the list of speakers we can see that we have 3 speakers. The first one has the area "Inf sec" like the second one, so that, they are neighbors. And the second one is international like the third one, so they are neighbors too. Each one of them has all the values of their domains at the beginning. 
 The diagram that represents the graph is:
 
 ![Untitled Diagram (1)](https://user-images.githubusercontent.com/58644744/140197889-102a5778-431b-446a-85d3-1de691d54fc0.jpg)

If we load the file and then want to check the speakers from the terminal we get the next:
 
 ![image](https://user-images.githubusercontent.com/58644744/140086041-d2dde3d3-72a7-4175-8b85-aea9e5fb22fa.png)

### Forward checking 
 Next we have the **forward checking** algorithm which pretends to remove certain value from the domain of the neighbors of a speaker, in this case the value would be the hour that a speaker wants.
For the experiment to check if the **forward checking algorithm** works fine, we have to add a speak time on any speaker, on the **add speaker algorithm** the **forward checking algorithm** is called with the id of the speaker on whom the speak time is been added and once we have done that the value (the speak time) should be gone in the domain of the neighbors.
So if we assign the hour **1 A and 1 C** to the first speaker those values should not appear on the domain of the neighbors, in this case the only neighbor is speaker 2.

![image](https://user-images.githubusercontent.com/58644744/140092839-d39f3c01-b936-4885-a8eb-771e9dc349c7.png)

As we can see, the only values on the speaker 1 domain are the added, the speaker 2 doesn't have those values on the domain and the domain of the speaker 3 was not affected because it's not a neighbor of speaker 1.

### Minimum remaining values algorithm
Then we have the **Minimum remaining values algorithm** which pretends to choose the variable with the fewest consistent values between the neighbors of a speaker. The output of this algorithm is a tuple with the number of values (which should be the least amount) and the id of the speaker who owns the domain with that amount.
For the experiment we continue with the previous assignment and as the speaker 1 is the one with values on its domain we will check the values of the speaker 1 neighbors, for that we introduce the id 1 when selecting the MRV option in the menu.

![image](https://user-images.githubusercontent.com/58644744/140095536-d2e479b5-f088-4da7-8e3a-6d91d5fe6c44.png)

The result is a tuple with the value 28 which represents the number of values in the domain of the speaker and the 2 in the tuple is the id of the speaker. 
As we saw before the speaker 2 who is neighbor of speaker 1 has it's domain affected because of the **forward checking** and the time values that were added to speaker's 1 domain are no longer part of speaker's 2 domain, so that we have 28 values on the domain while speaker 3 has all the 30 values on it's domain.

### Least Constrained value
This heuristic is used to order the values of the domains of the neighbors so that we get how many of them are consistent.

### Running the program
To run the program open a new terminal and type **"python menu.py"** and the menu should appear. Then you can either add some speakers on your own with option 1 or you can load them from the json file with option 6. Then you can choose any other option to see how it works.
