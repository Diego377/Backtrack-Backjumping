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
 First we have the forward checking algorithm which pretends to remove certain value from the domain of the neighbors of a speaker.
