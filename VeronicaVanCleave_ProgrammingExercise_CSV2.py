def read_grades():
    """
       Prints the students first and last name, exam 1, exam 2, and exam 3 scores in the grades.csv file.

       Parameters:
           None

       Variables:
           None

       Logic:
           1. Opens the grades.csv file.
           2. Loops through all of the inputs.

       Return:
           grades.csv file info
       """

    import csv

    with open('grades.csv', mode='r', newline='') as file:
        reader = csv.reader(file)


        # Prints the grades.csv file in a tabular format
        for row in reader:
            print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*row))

if __name__ == "__main__":
    read_grades()