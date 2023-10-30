#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json
class  assignment():
    assign={}
    ID=[]
    ID1=0
    AssignmentValue=[]
    AssignmentName=[]
    def createAssignment(self):
        #print("please Enter name and value with _ _")
        a=str(input("Enter the assignment name: "))
        b=int(input("Enter in Assignment Value: "))
        print(f"Your assignment has been assigned ID {self.ID1}")
        self.AssignmentValue.append(b)
        self.AssignmentName.append(a)
        self.ID.append(self.ID1)
        self.ID1+=1

        dict={}                   #Assign={Assignment1:[]}
        for i in range(b):
            dict[i+1]=0
        self.assign[a]=dict
        print(self.assign)

        print()
        self.__init__()


            

    def assignmentScore(self):
        print(f"Current Assignment ID you can search : {self.ID}")
        a=int(input("Enter in the assignment ID: "))  #0

        print(f"Enter in the scores for {self.AssignmentValue[a]} students for {self.AssignmentName[a]}: ")
        for i in range(self.AssignmentValue[a]):
            b=int(input(f"{i+1}: "))
            self.assign[self.AssignmentName[a]][i+1]=b

        print(self.assign)
        print()
        self.__init__()

    def writeData(self):
        file=json.dumps(self.assign)
        print(file)
        print(type(file))
        file.to_csv("data.csv", index=False)


    def __init__(self):
        a=int(input("1. Create an Assignment\n2. Enter in Assignment Scores\n3. Write your data to file\nEnter in your choice: "))
        if a==1:
            print()
            self.createAssignment()
        elif a==2:
            print()
            self.assignmentScore()
        else:
            print()
            self.writeData()
            



a=assignment()