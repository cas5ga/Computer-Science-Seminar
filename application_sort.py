#Created by Caleb Street
#Computer Science Seminar Course Project
#application_sort.py
#Reads applicant information from a database
#Calculates scores for each applicant
#Determines which applicants should be selected and which applicants should not be accepted
#Adds the applicants to the appropriate database (accepted or rejected)

import sqlite3
import os.path

schoolCapacity = 3
totalNumberOfPoints = 251

#trys to connect to the Applicant database
try:
    directory = os.path.dirname(os.path.abspath(__file__))
    databasePath = os.path.join(directory, "Applicant.db")
    applicantConnection = sqlite3.connect(databasePath)
#prints an error message if connection fails
except:
    print("An error occured while connecting to the Applicant database.")


#trys to connect to the Approved database
try:
    directory = os.path.dirname(os.path.abspath(__file__))
    databasePath = os.path.join(directory, "Approved.db")
    approvedConnection = sqlite3.connect(databasePath)
#prints an error message if connection fails
except:
    print("An error occured while connecting to the Approved database.")


#trys to connect to the Rejected database
try:
    directory = os.path.dirname(os.path.abspath(__file__))
    databasePath = os.path.join(directory, "Rejected.db")
    rejectedConnection = sqlite3.connect(databasePath)
#prints an error message if connection fails
except:
    print("An error occured while connecting to the Rejected database.")


#trys to connect to the Scores database
try:
    directory = os.path.dirname(os.path.abspath(__file__))
    databasePath = os.path.join(directory, "Scores.db")
    scoresConnection = sqlite3.connect(databasePath)
#prints an error message if connection fails
except:
    print("An error occured while connecting to the Scores database.")


#gets all the required fields to make decisions on which students are more likely to be accepted
rows = applicantConnection.execute('''SELECT Education.person_ID, GPA, class_rank, clubs, extracurriculars, SAT, average_number_courses, credits_earned, average_course_grade \
FROM Education JOIN Additional_Info ON Education.person_ID = Additional_Info.person_ID''').fetchall()

#loops through each applicant
for row in rows:
    #calculates the GPA score
    #total points: 40
    GPAScore = int(float(row[1]) * 10)

    #calculates the rank score
    #total points: 10
    rankScore = int(row[2])
    if(rankScore <= 10):
        rankScore = 10
    elif(rankScore <= 50):
        rankScore = 6
    elif(rankScore <= 100):
        rankScore = 3
    else:
        rankScore = 1

    #calculates the club score
    #total points: 10
    clubValues = row[3]
    clubList = clubValues.split("\n")
    numberOfClubs = len(clubList)
    if(numberOfClubs >= 10):
        clubScore = 10
    elif(numberOfClubs >= 5):
        clubScore = 6
    elif(numberOfClubs >= 3):
        clubScore = 3
    else:
        clubScore = 1

    #calculates the extracurricular score
    #total points: 10
    extracurricularValues = row[4]
    extracurricularList = extracurricularValues.split("\n")
    numberOfExtracurriculars = len(extracurricularList)
    if(numberOfExtracurriculars >= 10):
        extracurricularScore = 10
    elif(numberOfExtracurriculars >= 5):
        extracurricularScore = 6
    elif(numberOfExtracurriculars >= 3):
        extracurricularScore = 3
    else:
        extracurricularScore = 1

    #calculates the SAT score
    #total points: 16
    SATScore = int(int(float(row[5]) / 100))

    #calculates the average number of courses score
    #total points: 5
    coursesValues = int(float(row[6]))
    if(coursesValues >= 5):
        coursesScore = 5
    elif(coursesValues >= 4):
        coursesScore = 4
    elif(coursesValues >= 3):
        coursesScore = 3
    elif(coursesValues >= 2):
        coursesScore = 2
    else:
        coursesScore = 1

    #calculates the credits earned score
    #total points: 60
    creditsValues = int(row[7])
    if(creditsValues >= 60):
        creditsScore = 60
    else:
        creditsScore = creditsValues

    #calculates the average course grade score
    #total points: 100
    courseGradeValues = int(float(row[8]))
    if(courseGradeValues >= 100):
        courseGradeScore = 100
    else:
        courseGradeScore = courseGradeValues

    #calculates the overall average score
    total = GPAScore + rankScore + clubScore + extracurricularScore + SATScore + coursesScore + creditsScore + courseGradeScore
    averageScore = (total / totalNumberOfPoints) * 100


    values = scoresConnection.execute('''SELECT person_ID FROM Scores''').fetchall()

    #determines if the provided person_ID is already in the Scores table
    flag = False
    for value in values:
        #sets the flag to true if the person_ID is in the table
        if(value[0] == row[0]):
            flag = True

    #adds the new information into the Scores table if it is not already in the table
    if(not flag):
        #adds each of the scores to the Scores database
        scoresConnection.execute('''INSERT INTO Scores (person_ID, GPA, class_rank, clubs, extracurriculars, SAT, average_number_courses, credits_earned, average_course_grade, average_score) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row[0], GPAScore, rankScore, clubScore, extracurricularScore, SATScore, coursesScore, creditsScore, courseGradeScore, averageScore))
        scoresConnection.commit()


#gets the top "schoolCapacity" applicants from the database
rows = scoresConnection.execute('''SELECT person_ID FROM Scores ORDER BY average_score DESC LIMIT ''' + str(schoolCapacity)).fetchall()

for row in rows:
    values = approvedConnection.execute('''SELECT person_ID FROM Person''').fetchall()

    #determines if the provided person_ID is already in the Person table
    flag = False
    for value in values:
        #sets the flag to true if the person_ID is in the table
        if(value[0] == row[0]):
            flag = True

    #adds the new information into the appropriate table if it is not already in the table
    if(not flag):
        #adds the information into the Person table
        PersonValues = applicantConnection.execute('''SELECT person_ID, first_name, middle_name, last_name FROM Person WHERE person_ID = ''' + str(row[0])).fetchall()
        for value in PersonValues:
            approvedConnection.execute('''INSERT INTO Person (person_ID, first_name, middle_name, last_name) VALUES (?, ?, ?, ?)''', (value[0], value[1], value[2], value[3]))

        #adds the information into the Person_Info table
        Person_InfoValues = applicantConnection.execute('''SELECT * FROM Person_Info WHERE person_ID = ''' + str(row[0])).fetchall()
        for value in Person_InfoValues:
            approvedConnection.execute('''INSERT INTO Person_Info (person_ID, email, home_phone, cell_phone) VALUES (?, ?, ?, ?)''', (value[0], value[1], value[2], value[3]))

        #adds the information into the Person_Address table
        Person_AddressValues = applicantConnection.execute('''SELECT * FROM Person_Address WHERE person_ID = ''' + str(row[0])).fetchall()
        for value in Person_AddressValues:
            approvedConnection.execute('''INSERT INTO Person_Address (person_ID, street, city, state, zip_code) VALUES (?, ?, ?, ?, ?)''', (value[0], value[1], value[2], value[3], value[4]))

        approvedConnection.commit()


#gets the total number of applicants
count = applicantConnection.execute('''SELECT COUNT(person_ID) FROM Person''').fetchone()[0]

#gets the total number of rejected applicants
numberOfRejectedApplicants = count - schoolCapacity

#gets the information for the rejected applicants
rows = scoresConnection.execute('''SELECT person_ID FROM Scores ORDER BY average_score ASC LIMIT ''' + str(numberOfRejectedApplicants)).fetchall()

for row in rows:
    values = rejectedConnection.execute('''SELECT person_ID FROM Person''').fetchall()

    #determines if the provided person_ID is already in the Person table
    flag = False
    for value in values:
        #sets the flag to true if the person_ID is in the table
        if(value[0] == row[0]):
            flag = True

    #adds the new information into the appropriate table if it is not already in the table
    if(not flag):
        #adds the information into the Person table
        PersonValues = applicantConnection.execute('''SELECT person_ID, first_name, middle_name, last_name FROM Person WHERE person_ID = ''' + str(row[0])).fetchall()
        for value in PersonValues:
            rejectedConnection.execute('''INSERT INTO Person (person_ID, first_name, middle_name, last_name) VALUES (?, ?, ?, ?)''', (value[0], value[1], value[2], value[3]))

        #adds the information into the Person_Info table
        Person_InfoValues = applicantConnection.execute('''SELECT * FROM Person_Info WHERE person_ID = ''' + str(row[0])).fetchall()
        for value in Person_InfoValues:
            rejectedConnection.execute('''INSERT INTO Person_Info (person_ID, email, home_phone, cell_phone) VALUES (?, ?, ?, ?)''', (value[0], value[1], value[2], value[3]))

        #adds the information into the Person_Address table
        Person_AddressValues = applicantConnection.execute('''SELECT * FROM Person_Address WHERE person_ID = ''' + str(row[0])).fetchall()
        for value in Person_AddressValues:
            rejectedConnection.execute('''INSERT INTO Person_Address (person_ID, street, city, state, zip_code) VALUES (?, ?, ?, ?, ?)''', (value[0], value[1], value[2], value[3], value[4]))

        rejectedConnection.commit()


applicantConnection.close()
approvedConnection.close()
rejectedConnection.close()
scoresConnection.close()