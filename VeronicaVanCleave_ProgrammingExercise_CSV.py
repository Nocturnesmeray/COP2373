def recording_grades():
    """
    Gets the students first and last name, exam 1, exam 2, and exam 3 scores for the grades.csv file.

    Parameters:
        None

    Variables:
        first name(str): First name of the student.
        last name(str): Last name of the student.
        exam 1(int): The student's score for Exam 1.
        exam 2(int): The student's score for Exam 2.
        exam 3(int): The student's score for Exam 3.

    Logic:
        1. Asks the user how many students there are.
        2. Loops through all of the inputs.
        3. Creates the grades.csv file for later use.

    Return:
        grades.csv file
    """
    import csv
    students = int(input("How many students are there? "))

    #Creates the grades.csv file.
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        for i in range(students):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            exam_1 = int(input("Enter exam 1: "))
            exam_2 = int(input("Enter exam 2: "))
            exam_3 = int(input("Enter exam 3: "))

            writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])


    print("grades.csv has successfully been created.")



if __name__ == "__main__":
    recording_grades()
