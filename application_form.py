#Created by Caleb Street
#Computer Science Seminar Course Project
#application_form.py
#Creates an electronic form for college applications
#This is the form the applicant must fill out to apply for the college
#This form sends applicant information to a database

import tkinter
import pyautogui
import sqlite3
import os.path

#Checks for an integer value
def checkInt(num):
    try:
        num = int(num)
        return True
    except:
        return False

#Checks for a two digit integer value
def checkTwoInt(num):
    try:
        if(not checkInt(num)):
            return False
        if(len(num) == 2):
            return True
        return False
    except:
        return False

#Checks for a three digit integer value
def checkThreeInt(num):
    try:
        if(not checkInt(num)):
            return False
        if(len(num) == 3):
            return True
        return False    
    except:
        return False

#Checks for a four digit integer value
def checkFourInt(num):
    try:
        if(not checkInt(num)):
            return False
        if(len(num) == 4):
            return True
        return False
    except:
        return False

#checks for a five digit integer value
def checkFiveInt(num):
    try:
        if(not checkInt(num)):
            return False
        if(len(num) == 5):
            return True
        return False
    except:
        return False

#Checks for a decimal value
def checkDecimal(num):
    try:
        num = float(num)
        return True
    except:
        return False

#checks for a string
def checkString(value):
    try:
        value = str(value)
        return True
    except:
        return False

#Checks for a valid social security number
def checkSocialSecurity(num):
    try:
        values = num.split("-")
        if(not checkThreeInt(values[0])):
            return False
        if(not checkTwoInt(values[1])):
            return False
        if(not checkFourInt(values[2])):
            return False
        return True
    except:
        return False

#Checks for a valid date of birth
def checkBirthDate(num):
    try:
        values = num.split("-")
        if(not checkTwoInt(values[0])):
            return False
        if(not checkTwoInt(values[1])):
            return False
        if(not checkFourInt(values[2])):
            return False
        return True
    except:
        return  False

#Checks for a valid email
def checkEmail(value):
    try:
        values = value.split("@")
        emailList = [values[0]]
        values = values[1].split(".")
        emailList.append(values[0])
        emailList.append(values[1])
        if(not checkString(emailList[0])):
            return False
        if(not checkString(emailList[1])):
            return False
        if(not checkString(emailList[2])):
            return False
        return True
    except:
        return False

#Checks for a valid phone number
def checkPhone(num):
    try:
        values = num.split("-")
        if(not checkThreeInt(values[0])):
            return False
        if(not checkThreeInt(values[1])):
            return False
        if(not checkFourInt(values[2])):
            return False
        return True
    except:
        return False

#Checks for a valid SAT score
def checkSATScore(num):
    if(not checkInt(num)):
        return False
    if(int(num) < 400 or int(num) > 1600):
        return False
    return True


#Sends the appropriate information to the Applicant.db database
#when the submit button is clicked
def submitFirstForm():
    #trys to connect to the database
    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        databasePath = os.path.join(directory, "Applicant.db")
        connection = sqlite3.connect(databasePath)
    #prints an error message if connection fails
    except:
        print("An error occured while connecting to the database.")

    #tries to open the text file
    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.join(directory, "numbers.txt")
        numberFile = open(filePath, "a")
    #prints an error message if it fails to open the file
    except:
        print("Failed to open the file")


    #gets all the user input from the first page of the form
    personID = personIDEntry.get()
    firstName = firstNameEntry.get()
    middleName = middleNameEntry.get()
    lastName = lastNameEntry.get()
    SSN = SSNEntry.get()
    birthDate = birthDateEntry.get()
    gender = genderEntry.get()
    citizenship = citizenshipEntry.get()
    ethnicity = ethnicityEntry.get()
    language = languageEntry.get()
    email = emailEntry.get()
    homePhone = homePhoneEntry.get()
    cellPhone = cellPhoneEntry.get()
    personStreet = personStreetEntry.get()
    personCity = personCityEntry.get()
    personState = personStateEntry.get()
    personZipCode = personZipEntry.get()
    schoolID = schoolIDEntry.get()
    classRank = rankEntry.get()
    GPA = GPAEntry.get()
    schoolName = schoolNameEntry.get()
    SAT = SATEntry.get()
    averageNumCourses = averageCoursesEntry.get()
    collegeCredits = collegeCoursesNumEntry.get()
    averageCollegeGrade = collegeCourseAvgEntry.get()

    flagList = []

    #input validation for the Personal Id Number field
    if(not checkFiveInt(personID)):
        flagList.append("personID")
        personIDLabel.config(foreground = "red")
    else:
        personIDLabel.config(foreground = "black")

    #input validation for the First Name field
    if(firstName == ""):
        flagList.append("firstName")
        firstNameLabel.config(foreground = "red")
    else:
        firstNameLabel.config(foreground = "black")

    #input validation for the Middle Name field
    if(middleName == ""):
        flagList.append("middleName")
        middleNameLabel.config(foreground = "red")
    else:
        middleNameLabel.config(foreground = "black")

    #input validation for the Last Name field
    if(lastName == ""):
        flagList.append("lastName")
        lastNameLabel.config(foreground = "red")
    else:
        lastNameLabel.config(foreground = "black")

    #input validation for the Social Security Number field
    if(not checkSocialSecurity(SSN)):
        flagList.append("SSN")
        SSNLabel.config(foreground = "red")
    else:
        SSNLabel.config(foreground = "black")

    #input validation for Date of Birth field
    if(not checkBirthDate(birthDate)):
        flagList.append("birthDate")
        birthDateLabel.config(foreground = "red")
    else:
        birthDateLabel.config(foreground = "black")

    #input validation for Gender field
    if(gender == "" or gender == "Select a Gender"):
        flagList.append("gender")
        genderLabel.config(foreground = "red")
    else:
        genderLabel.config(foreground = "black")

    #input validation for the Citizenship field
    if(citizenship == "" or citizenship == "Select an Option"):
        flagList.append("citizenship")
        citizenshipLabel.configure(foreground = "red")
    else:
        citizenshipLabel.config(foreground = "black")

    #input validation for the Ethnicity field
    if(ethnicity == "" or ethnicity == "Select an Ethnicity"):
        flagList.append("ethnicity")
        ethnicityLabel.config(foreground = "red")
    else:
        ethnicityLabel.config(foreground = "black")

    #input validation for Primary Language field
    if(language == ""):
        flagList.append("language")
        languageLabel.config(foreground = "red")
    else:
        languageLabel.config(foreground = "black")

    #input validation for Email Address field
    if(not checkEmail(email) or email == "Enter full email address (Ex. johndoe1234@gmail.com)"):
        flagList.append("email")
        emailLabel.config(foreground = "red")
    else:
        emailLabel.config(foreground = "black")

    #input validation for Home Phone Number field
    if(not checkPhone(homePhone)):
        flagList.append("homePhone")
        homePhoneLabel.config(foreground = "red")
    else:
        homePhoneLabel.config(foreground = "black")

    #input validation for Cell Phone Number field
    if(not checkPhone(cellPhone)):
        flagList.append("cellPhone")
        cellPhoneLabel.config(foreground = "red")
    else:
        cellPhoneLabel.config(foreground = "black")

    #input validation for Street Address field
    if(personStreet == ""):
        flagList.append("personStreet")
        personStreetLabel.config(foreground = "red")
    else:
        personStreetLabel.config(foreground = "black")

    #input validatoin for City field
    if(personCity == ""):
        flagList.append("personCity")
        personCityLabel.config(foreground = "red")
    else:
        personCityLabel.config(foreground = "black")

    #input validation for State field
    if(personState == "" or personState == "Select a State"):
        flagList.append("personState")
        personStateLabel.config(foreground = "red")
    else:
        personStateLabel.config(foreground = "black")

    #input validation for Zip Code field
    if(personZipCode == ""):
        flagList.append("personZipCode")
        personZipLabel.config(foreground = "red")
    else:
        personZipLabel.config(foreground = "black")

    #input validation for High School Code field
    if(not checkFiveInt(schoolID)):
        flagList.append("schoolID")
        schoolIDLabel.config(foreground = "red")
    else:
        schoolIDLabel.config(foreground = "black")

    #input validation for High School Name field
    if(schoolName == ""):
        flagList.append("schoolName")
        schoolNameLabel.config(foreground = "red")
    else:
        schoolNameLabel.config(foreground = "black")

    #input validation for Class Rank field
    if(not checkInt(classRank)):
        flagList.append("classRank")
        rankLabel.config(foreground = "red")
    else:
        rankLabel.config(foreground = "black")

    #input validation for GPA field
    if(not checkDecimal(GPA)):
        flagList.append("GPA")
        GPALabel.config(foreground = "red")
    else:
        GPALabel.config(foreground = "black")

    #input validation for SAT Score field
    if(not checkSATScore(SAT)):
        flagList.append("SAT")
        SATLabel.config(foreground = "red")
    else:
        SATLabel.config(foreground = "black")

    #input validation for Average Total Courses Taken field
    if(not checkDecimal(averageNumCourses)):
        flagList.append("averageNumCourses")
        averageCoursesLabel.config(foreground = "red")
    else:
        averageCoursesLabel.config(foreground = "black")

    #input validation for College Credits Earned field
    if(not checkInt(collegeCredits)):
        flagList.append("collegeCredits")
        collegeCoursesNumLabel.config(foreground = "red")
    else:
        collegeCoursesNumLabel.config(foreground = "black")

    #input validation for Average College Course Grade field
    if(not checkInt(averageCollegeGrade)):
        flagList.append("averageCollegeGrade")
        collegeCourseAvgLabel.config(foreground = "red")
    else:
        collegeCourseAvgLabel.config(foreground = "black")

    if(len(flagList) != 0):
        errorMessageLabel.place(x = (int(0.575 * screenWidth)), y = (int(0.83 * screenHeight)))
        return
    else:
        errorMessageLabel.place_forget()

    #adds the appropriate information to the person table in the database
    connection.execute('''INSERT INTO Person (person_ID, first_name, middle_name, last_name, SSN, birth_date, gender, citizenship_status, ethnicity, primary_language) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (personID, firstName, middleName, lastName, SSN, birthDate, gender, citizenship, ethnicity, language))

    #adds the appropriate information to the person_info table in the database
    connection.execute('''INSERT INTO Person_Info (person_ID, email, home_phone, cell_phone) \
        VALUES (?, ?, ?, ?)''', (personID, email, homePhone, cellPhone))

    #adds the appropriate information to the person_adderess table in the database
    connection.execute('''INSERT INTO Person_Address (person_ID, street, city, state, zip_code) \
        VALUES (?, ?, ?, ?, ?)''', (personID, personStreet, personCity, personState, personZipCode))

    #adds the appropriate information to the education table in the database
    connection.execute('''INSERT INTO Education (person_ID, school_ID, class_rank, GPA, SAT, average_number_courses, credits_earned, average_course_grade) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (personID, schoolID, classRank, GPA, SAT, averageNumCourses, collegeCredits, averageCollegeGrade))

    #gets all the current school_IDs in the School_Info table
    rows = connection.execute('''SELECT school_ID FROM School_Info''').fetchall()
    
    #determines if the provided school code is already in the School_Info table
    flag = False
    for row in rows:
        #sets the flag to true if the code is in the table
        if(row[0] == schoolID):
            flag = True

    #adds the new information into the School_Info table if it is not already in the table
    if(not flag):
        #adds the appropriate information to the School_Info table in the database
        connection.execute('''INSERT INTO School_Info (school_ID, school_name) \
            VALUES (?, ?)''', (schoolID, schoolName))

    #commits the changes to the database and closes the connection
    connection.commit()
    connection.close()

    #adds personID to the file and closes the file
    numberFile.write(personID + "\n")
    numberFile.close()

    #hides the labels and entry fields of the first form
    removeFirstForm()
    #shows the labels and entry fields of the second form
    displaySecondForm()


#Displays all the lablel and entry fields from the first page
def displayFirstForm():
    pageLabel.place(x = (int(0.24 * screenWidth)), y = (int(0.2 * screenHeight)))

    #first row label fields (personal information section)
    personIDLabel.place(x = (int(0.03 * screenWidth)), y = (int(0.25 * screenHeight)))
    firstNameLabel.place(x = (int(0.27 * screenWidth)), y = (int(0.25 * screenHeight)))
    middleNameLabel.place(x = (int(0.52 * screenWidth)), y = (int(0.25 * screenHeight)))
    lastNameLabel.place(x = (int(0.77 * screenWidth)), y = (int(0.25 * screenHeight)))

    #first row entry fields (personal information section)
    personIDEntry.place(x = (int(0.03 * screenWidth)), y = (int(0.27 * screenHeight)))
    personIDEntry.insert(0, "5 Digit Code (provided to you) (Ex. 12345)")
    firstNameEntry.place(x = (int(0.27 * screenWidth)), y = (int(0.27 * screenHeight)))
    middleNameEntry.place(x = (int(0.52 * screenWidth)), y = (int(0.27 * screenHeight)))
    lastNameEntry.place(x = int(0.77 * screenWidth), y = (int(0.27 * screenHeight)))

    #second row label fields (personal information section)
    SSNLabel.place(x = (int(0.1 * screenWidth)), y = (int(0.31 * screenHeight)))
    birthDateLabel.place(x = (int(0.4 * screenWidth)), y = (int(0.31 * screenHeight)))
    genderLabel.place(x = (int(0.7 * screenWidth)), y = (int(0.31 * screenHeight)))

    #second row entry fields (personal information section)
    SSNEntry.place(x = (int(0.1 * screenWidth)), y = (int(0.33 * screenHeight)))
    SSNEntry.insert(0, "Add dashes between sections (Ex. 123-45-6789)")
    birthDateEntry.place(x = (int(0.4 * screenWidth)), y = (int(0.33 * screenHeight)))
    birthDateEntry.insert(0, "Add dashes between sections (Ex. 01-11-2001)")
    genderEntry.place(x = (int(0.7 * screenWidth)), y = (int(0.33 * screenHeight)))
    genderEntry.current(0)

    #thrid row label fields (personal information section)
    citizenshipLabel.place(x = (int(0.1 * screenWidth)), y = (int(0.37 * screenHeight)))
    ethnicityLabel.place(x = (int(0.4 * screenWidth)), y = (int(0.37 * screenHeight)))
    languageLabel.place(x = (int(0.7 * screenWidth)), y = (int(0.37 * screenHeight)))

    #thrid row entry fileds (personal information section)
    citizenshipEntry.place(x = (int(0.1 * screenWidth)), y = (int(0.39 * screenHeight)))
    citizenshipEntry.current(0)
    ethnicityEntry.place(x = (int(0.4 * screenWidth)), y = (int(0.39 * screenHeight)))
    ethnicityEntry.current(0)
    languageEntry.place(x = (int(0.7 * screenWidth)), y = (int(0.39 * screenHeight)))

    #fourth row label fields (personal information section)
    emailLabel.place(x = (int(0.1 * screenWidth)), y = (int(0.43 * screenHeight)))
    homePhoneLabel.place(x = (int(0.4 * screenWidth)), y = (int(0.43 * screenHeight)))
    cellPhoneLabel.place(x = (int(0.7 * screenWidth)), y = (int(0.43 * screenHeight)))

    #fourth row entry fields (personal information section)
    emailEntry.place(x = (int(0.1 * screenWidth)), y = (int(0.45 * screenHeight)))
    emailEntry.insert(0, "Enter full email address (Ex. johndoe1234@gmail.com)")
    homePhoneEntry.place(x = (int(0.4 * screenWidth)), y = (int(0.45 * screenHeight)))
    homePhoneEntry.insert(0, "Add dashes between sections (Ex. 123-456-7890)")
    cellPhoneEntry.place(x = int(0.7 * screenWidth), y = (int(0.45 * screenHeight)))
    cellPhoneEntry.insert(0, "Add dashes between sections (Ex. 123-456-7890)")

    #fifth row label fields (personal information section)
    personStreetLabel.place(x = (int(0.03 * screenWidth)), y = (int(0.49 * screenHeight)))
    personCityLabel.place(x = (int(0.27 * screenWidth)), y = (int(0.49 * screenHeight)))
    personStateLabel.place(x = (int(0.52 * screenWidth)), y = (int(0.49 * screenHeight)))
    personZipLabel.place(x = (int(0.77 * screenWidth)), y = (int(0.49 * screenHeight)))

    #fifth row entry fields (personal information section)
    personStreetEntry.place(x = (int(0.03 * screenWidth)), y = (int(0.51 * screenHeight)))
    personCityEntry.place(x = (int(0.27 * screenWidth)), y = (int(0.51 * screenHeight)))
    personStateEntry.place(x = (int(0.52 * screenWidth)), y = (int(0.51 * screenHeight)))
    personStateEntry.current(0)
    personZipEntry.place(x = (int(0.77 * screenWidth)), y = (int(0.51 * screenHeight)))
    pageLabel2.place(x = (int(0.24 * screenWidth)), y = (int(0.6 * screenHeight)))

    #first row label fields (prior education section)
    schoolIDLabel.place(x = (int(0.03 * screenWidth)), y = (int(0.655 * screenHeight)))
    schoolNameLabel.place(x = (int(0.27 * screenWidth)), y = (int(0.655 * screenHeight)))
    rankLabel.place(x = (int(0.52 * screenWidth)), y = (int(0.655 * screenHeight)))
    GPALabel.place(x = (int(0.77 * screenWidth)), y = (int(0.655 * screenHeight)))

    #first row entry fields (prior education section)
    schoolIDEntry.place(x = (int(0.03 * screenWidth)), y = (int(0.675 * screenHeight)))
    schoolIDEntry.insert(0, "5 Digit Code (provided to you) (Ex. 12345)")
    schoolNameEntry.place(x = (int(0.27 * screenWidth)), y = (int(0.675 * screenHeight)))
    rankEntry.place(x = (int(0.52 * screenWidth)), y = (int(0.675 * screenHeight)))
    rankEntry.insert(0, "Numeric Value (Ex. 5)")
    GPAEntry.place(x = int(0.77 * screenWidth), y = (int(0.675 * screenHeight)))
    GPAEntry.insert(0, "Decimal Value (Ex. 4.0)")

    #second row label fields (prior education section)
    SATLabel.place(x = (int(0.03 * screenWidth)), y = (int(0.715 * screenHeight)))
    averageCoursesLabel.place(x = (int(0.27 * screenWidth)), y = (int(0.715 * screenHeight)))
    collegeCoursesNumLabel.place(x = (int(0.52 * screenWidth)), y = (int(0.715 * screenHeight)))
    collegeCourseAvgLabel.place(x = (int(0.77 * screenWidth)), y = (int(0.715 * screenHeight)))

    #second row entry fields (prior education section)
    SATEntry.place(x = (int(0.03 * screenWidth)), y = (int(0.735 * screenHeight)))
    SATEntry.insert(0, "Numeric Value (Ex. 1500)")
    averageCoursesEntry.place(x = (int(0.27 * screenWidth)), y = (int(0.735 * screenHeight)))
    averageCoursesEntry.insert(0, "Decimal Value (Ex. 4.8)")
    collegeCoursesNumEntry.place(x = (int(0.52 * screenWidth)), y = (int(0.735 * screenHeight)))
    collegeCoursesNumEntry.insert(0, "Numeric Value (Ex. 20)")
    collegeCourseAvgEntry.place(x = (int(0.77 * screenWidth)), y = (int(0.735 * screenHeight)))
    collegeCourseAvgEntry.insert(0, "Numeric Value (Ex. 95)")

    pageLabel3.place(x = (int(0.235 * screenWidth)), y = (int(0.8 * screenHeight)))

    submitButtonOne.place(x = (int(0.475 * screenWidth)), y = (int(0.83 * screenHeight)))


#Hides all the label and entry fields from the first page
def removeFirstForm():
    pageLabel.place_forget()

    #first row label fields (personal information section)
    personIDLabel.place_forget()
    firstNameLabel.place_forget()
    middleNameLabel.place_forget()
    lastNameLabel.place_forget()

    #first row entry fields (personal information section)
    personIDEntry.place_forget()
    firstNameEntry.place_forget()
    middleNameEntry.place_forget()
    lastNameEntry.place_forget()

    #first row entry fields (personal information section)
    personIDEntry.delete(0, 'end')
    firstNameEntry.delete(0, 'end')
    middleNameEntry.delete(0, 'end')
    lastNameEntry.delete(0, 'end')

    #second row label fields (personal information section)
    SSNLabel.place_forget()
    birthDateLabel.place_forget()
    genderLabel.place_forget()

    #second row entry fields (personal information section)
    SSNEntry.place_forget()
    birthDateEntry.place_forget()
    genderEntry.place_forget()

    #second row entry fields (personal information section)
    SSNEntry.delete(0, 'end')
    birthDateEntry.delete(0, 'end')
    genderEntry.delete(0, 'end')

    #thrid row label fields (personal information section)
    citizenshipLabel.place_forget()
    ethnicityLabel.place_forget()
    languageLabel.place_forget()

    #thrid row entry fields (personal information section)
    citizenshipEntry.place_forget()
    ethnicityEntry.place_forget()
    languageEntry.place_forget()

    #third row entry fields (personal information section)
    citizenshipEntry.delete(0, 'end')
    ethnicityEntry.delete(0, 'end')
    languageEntry.delete(0, 'end')

    #fourth row label fields (personal information section)
    emailLabel.place_forget()
    homePhoneLabel.place_forget()
    cellPhoneLabel.place_forget()

    #fourth row entry fields (personal information section)
    emailEntry.place_forget()
    homePhoneEntry.place_forget()
    cellPhoneEntry.place_forget()

    #fourth row entry fields (personal information section)
    emailEntry.delete(0, 'end')
    homePhoneEntry.delete(0, 'end')
    cellPhoneEntry.delete(0, 'end')

    #fifth row label fields (personal information section)
    personStreetLabel.place_forget()
    personCityLabel.place_forget()
    personStateLabel.place_forget()
    personZipLabel.place_forget()

    #fifth row entry fields (personal information section)
    personStreetEntry.place_forget()
    personCityEntry.place_forget()
    personStateEntry.place_forget()
    personZipEntry.place_forget()

    #fifth row entry fields (personal information section)
    personStreetEntry.delete(0, 'end')
    personCityEntry.delete(0, 'end')
    personStateEntry.delete(0, 'end')
    personZipEntry.delete(0, 'end')

    pageLabel2.place_forget()

    #first row label fields (prior education section)
    schoolIDLabel.place_forget()
    schoolNameLabel.place_forget()
    rankLabel.place_forget()
    GPALabel.place_forget()

    #first row entry fields (prior education section)
    schoolIDEntry.place_forget()
    schoolNameEntry.place_forget()
    rankEntry.place_forget()
    GPAEntry.place_forget()

    #first row entry fields (prior education section)
    schoolIDEntry.delete(0, 'end')
    schoolNameEntry.delete(0, 'end')
    rankEntry.delete(0, 'end')
    GPAEntry.delete(0, 'end')

    #second row label fields (prior education section)
    SATLabel.place_forget()
    averageCoursesLabel.place_forget()
    collegeCoursesNumLabel.place_forget()
    collegeCourseAvgLabel.place_forget()

    #second row entry fields (prior education section)
    SATEntry.place_forget()
    averageCoursesEntry.place_forget()
    collegeCoursesNumEntry.place_forget()
    collegeCourseAvgEntry.place_forget()

    #second row entry fields (prior education section)
    SATEntry.delete(0, 'end')
    averageCoursesEntry.delete(0, 'end')
    collegeCoursesNumEntry.delete(0, 'end')
    collegeCourseAvgEntry.delete(0, 'end')

    pageLabel3.place_forget()

    submitButtonOne.place_forget()

#Sends the appropriate information to the Applicant.db database
#when the submit button is clicked
def submitSecondForm():
    #trys to connect to the database
    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        databasePath = os.path.join(directory, "Applicant.db")
        connection = sqlite3.connect(databasePath)
    #prints an error message if connection fails
    except:
        print("An error occured while connecting to the database.")

    #tries to open the text file
    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.join(directory, "numbers.txt")
        numberFile = open(filePath)
    #prints an error message if it fails to open the file
    except:
        print("Failed to open the file")


    #gets all the user input from the second page of the form
    numbers = numberFile.readlines()
    personID = numbers[-1]
    personID = personID.strip()
    clubs = clubEntry.get('1.0', 'end-1c')
    extracurriculars = extracurricularEntry.get('1.0', 'end-1c')
    comments = commentEntry.get('1.0', 'end-1c')

    #adds the appropriate information to the additional_info table in the database
    connection.execute('''INSERT INTO Additional_Info (person_ID, clubs, extracurriculars, comments) \
        VALUES (?, ?, ?, ?)''', (personID, clubs, extracurriculars, comments))

    #commits the changes to the database and closes the connection
    connection.commit()
    connection.close()

    #hides the labels and entry fields of the second form
    removeSecondForm()
    #shows the labels and entry fields of the first form
    displayFirstForm()

#Displays all the label and entry fields from the second page
def displaySecondForm():
    pageLabel4.place(x = (int(0.24 * screenWidth)), y = (int(0.18 * screenHeight)))

    #first row label fields (additional information section)
    clubLabel.place(x = (int(0.078 * screenWidth)), y = (int(0.22 * screenHeight)))
    extracurricularLabel.place(x = (int(0.378 * screenWidth)), y = (int(0.22 * screenHeight)))
    commentLabel.place(x = (int(0.678 * screenWidth)), y = (int(0.22 * screenHeight)))

    #first row entry fields (additional information section)
    clubEntry.place(x = (int(0.1 * screenWidth)), y = (int(0.24 * screenHeight)))
    extracurricularEntry.place(x = (int(0.4 * screenWidth)), y = (int(0.24 * screenHeight)))
    commentEntry.place(x = (int(0.7 * screenWidth)), y = (int(0.24 * screenHeight)))

    pageLabel5.place(x = (int(0.235 * screenWidth)), y = (int(0.8 * screenHeight)))

    submitButtonTwo.place(x = (int(0.475 * screenWidth)), y = (int(0.83 * screenHeight)))


#Hides all the label and entry fields from the second page
def removeSecondForm():
    pageLabel4.place_forget()

    #first row label fields (additional information)
    clubLabel.place_forget()
    extracurricularLabel.place_forget()
    commentLabel.place_forget()

    #first row entry fields (additional information section)
    clubEntry.place_forget()
    extracurricularEntry.place_forget()
    commentEntry.place_forget()


    #first row entry fields (additional information section)
    clubEntry.delete('1.0', 'end')
    extracurricularEntry.delete('1.0', 'end')
    commentEntry.delete('1.0', 'end')

    pageLabel5.place_forget()

    submitButtonTwo.place_forget()


#Main function
screenWidth, screenHeight = pyautogui.size()
backgroundColor = "red3"
foregroundColor = "white"
labelColor = "gray45"

#creates the window
window = tkinter.Tk()
window.title("College Application Form")
window.geometry(str(screenWidth)+"x"+str(screenHeight))
window.configure(background = "light gray")

#list of states for the drop-down menu
states = [
"Select a State",
"Alabama", 
"Alaska", 
"Arizona", 
"Arkansas", 
"California", 
"Colorado", 
"Connecticut", 
"Delaware", 
"Florida", 
"Georgia", 
"Hawaii", 
"Idaho", 
"Illinois",
"Indiana", 
"Iowa", 
"Kansas", 
"Kentucky", 
"Louisiana", 
"Maine", 
"Maryland", 
"Massachusetts", 
"Michigan", 
"Minnesota", 
"Mississippi", 
"Missouri", 
"Montana",
"Nebraska", 
"Nevada", 
"New Hampshire", 
"New Jersey", 
"New Mexico", 
"New York", 
"North Carolina", 
"North Dakota", 
"Ohio", 
"Oklahoma", 
"Oregon", 
"Pennsylvania",
"Rhode Island", 
"South Carolina", 
"South Dakota", 
"Tennessee", 
"Texas", 
"Utah", 
"Vermont", 
"Virginia", 
"Washington", 
"West Virginia", 
"Wisconsin", 
"Wyoming"
]

#Header Section
#Colored Box
coloredBox = tkinter.Canvas(window, width = int(screenWidth), height = int(0.15 * screenHeight), bg = backgroundColor, highlightthickness = int(0.0028*screenHeight), highlightbackground = "black")
coloredBox.place(x = 0, y = 0)

#Logo
directory = os.path.dirname(os.path.abspath(__file__))
logoPath = os.path.join(directory, "logo.png")
logo = tkinter.PhotoImage(file = logoPath)
coloredBox.create_image(int(0.38 * screenWidth),int(0.01 * screenHeight),anchor = "nw", image = logo)

#Application Message (in the header section)
applicationMessage = tkinter.Label(window, text = "Electronic College Application Form", font = ("bold", int(0.035 * screenHeight)), fg = "white", bg = backgroundColor)
applicationMessage.place(x = int(0.35 * screenWidth), y = int(0.1 * screenHeight))

#First Form
pageLabel = tkinter.Label(window, text = "Personal Information", width = (int(0.04 * screenWidth)), font = ("bold", int(0.014*screenHeight)), bg = labelColor, fg = foregroundColor)

#first row label fields (personal information section)
personIDLabel = tkinter.Label(window, text = "Personal ID Number: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
firstNameLabel = tkinter.Label(window, text = "First Name: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
middleNameLabel = tkinter.Label(window, text = "Middle Name: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
lastNameLabel = tkinter.Label(window, text = "Last Name: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#first row entry fields (personal information section)
personIDEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
firstNameEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
middleNameEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
lastNameEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))

#second row label fields (personal information section)
SSNLabel = tkinter.Label(window, text = "Social Security Number:", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
birthDateLabel = tkinter.Label(window, text = "Date of Birth: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
genderLabel = tkinter.Label(window, text = "Gender:", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#second row entry fields (personal infromation section)
SSNEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
birthDateEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
genderEntry = tkinter.ttk.Combobox(window, width = (int(0.02188 * screenWidth - 1)))
genderEntry['values'] = ("Select a Gender", "Male", "Female")

#thrid row label fields (personal information section)
citizenshipLabel = tkinter.Label(window, text = "Are you a US Citizen:", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
ethnicityLabel = tkinter.Label(window, text = "What is your Ethnicity: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
languageLabel = tkinter.Label(window, text = "What is your Primary Language:", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#third row entry fields (personal information section)
citizenshipEntry = tkinter.ttk.Combobox(window, width = (int(0.02188 * screenWidth - 1)))
citizenshipEntry['values'] = ("Select an Option", "Yes", "No")
ethnicityEntry = tkinter.ttk.Combobox(window, width = (int(0.02188 * screenWidth - 1)))
ethnicityEntry['values'] = ("Select an Ethnicity", "American Indian or Alaska Native", "Asian", "Black or African American", "Hispanic or Latino", "Native Hawaiian or Other Pacific Islander", "White")
languageEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))

#fourth row label fields (personal information section)
emailLabel = tkinter.Label(window, text = "Email Address: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
homePhoneLabel = tkinter.Label(window, text = "Home Phone Number: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
cellPhoneLabel = tkinter.Label(window, text = "Cell Phone Number: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#fourth row entry fields (personal information section)
emailEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
homePhoneEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
cellPhoneEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))

#fifth row label fields (person informational section)
personStreetLabel = tkinter.Label(window, text = "Street Address: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
personCityLabel = tkinter.Label(window, text = "City: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
personStateLabel = tkinter.Label(window, text = "State: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
personZipLabel = tkinter.Label(window, text = "Zip Code: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#fifth row entry fields (personal information section)
personStreetEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
personCityEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
personStateEntry = tkinter.ttk.Combobox(window, width = (int(0.02188 * screenWidth - 1)))
personStateEntry['values'] = states
personZipEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
pageLabel2 = tkinter.Label(window, text = "Prior Education", width = (int(0.04 * screenWidth)), font = ("bold", int(0.014*screenHeight)), bg = labelColor, fg = foregroundColor)

#first row label fields (prior education section)
schoolIDLabel = tkinter.Label(window, text = "High School Code: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
schoolNameLabel = tkinter.Label(window, text = "High School Name: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
rankLabel = tkinter.Label(window, text = "Class Rank: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
GPALabel = tkinter.Label(window, text = "GPA: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#first row entry fields (prior ecucation section)
schoolIDEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
schoolNameEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
rankEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
GPAEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))

#second row label fields (prior education section)
SATLabel = tkinter.Label(window, text = "SAT Score: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
averageCoursesLabel = tkinter.Label(window, text = "Average Number of Total Courses Taken per Semester: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
collegeCoursesNumLabel = tkinter.Label(window, text = "Total Number of College Credits Earned: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")
collegeCourseAvgLabel = tkinter.Label(window, text = "Average College Courses Grade (100 point scale): ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0084*screenHeight)), bg = "light gray")

#second row entry fields (prior education section)
SATEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
averageCoursesEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
collegeCoursesNumEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))
collegeCourseAvgEntry = tkinter.Entry(window, width = (int(0.025 * screenWidth - 1)), font = ("bold", int(0.0084*screenHeight)))

pageLabel3 = tkinter.Label(window, text = "Submit and go to the next page:", width = (int(0.04 * screenWidth)), font = ("bold", int(0.014*screenHeight)), bg = "light gray")

submitButtonOne = tkinter.Button(window, text = "Submit", command = submitFirstForm, padx = int(0.01 * screenWidth), pady = int(0.005 * screenWidth))
#End First Form

#Second Form
pageLabel4 = tkinter.Label(window, text = "Additional Information", width = (int(0.04 * screenWidth)), font = ("bold", int(0.014*screenHeight)), bg = labelColor, fg = foregroundColor)

#first row label fields (additional information section)
clubLabel = tkinter.Label(window, text = "Clubs (one per line): ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0112*screenHeight)), bg = "light gray")
extracurricularLabel = tkinter.Label(window, text = "Extracurricular Activities (one per line): ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0112*screenHeight)), bg = "light gray")
commentLabel = tkinter.Label(window, text = "Additional Comments: ", width = (int(0.025 * screenWidth)), font = ("bold", int(0.0112*screenHeight)), bg = "light gray")

#first row entry fields (additional information section)
clubEntry = tkinter.Text(window, width = (int(0.025 * screenWidth - 1)), height = (int(0.035 * screenHeight)), font = ("bold", int(0.0084*screenHeight)))
extracurricularEntry = tkinter.Text(window, width = (int(0.025 * screenWidth - 1)), height = (int(0.035 * screenHeight)), font = ("bold", int(0.0084*screenHeight)))
commentEntry = tkinter.Text(window, width = (int(0.025 * screenWidth - 1)), height = (int(0.035 * screenHeight)), font = ("bold", int(0.0084*screenHeight)))

pageLabel5 = tkinter.Label(window, text = "Submit and finish:", width = (int(0.04 * screenWidth)), font = ("bold", int(0.014*screenHeight)), bg = "light gray")

submitButtonTwo = tkinter.Button(window, text = "Submit", command = submitSecondForm, padx = int(0.01 * screenWidth), pady = int(0.005 * screenWidth))

#error message for input validation
errorMessageLabel = tkinter.Label(window, text = "Please correct all errors marked with red labels", width = (int(0.015 * screenWidth)), font = ("bold", int(0.014*screenHeight)), bg = "light gray", fg = "red")

displayFirstForm()

window.mainloop()