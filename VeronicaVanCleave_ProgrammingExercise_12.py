import numpy as np
def statistics(grades):
    """
    Calculates the mean, median, standard deviation, min, and max of each exam.
    Then calculates the overall mean, median, standard deviation, min, and max.

    Parameters:
        grades = numpy array of exams

    Variables:
        exams (list): list of exams

    Logic:
        1. Define the exams list.
        2. Loop through the exams array.
        3. Calculate and display individual statistics.
        4. Calculate and display overall statistics.

    Return:
         None
    """
    print("\nStatistics:")

    exams = ["Exam1", "Exam2", "Exam3"]

    for i, exam in enumerate(exams):
        # Looks at one exam column to calculate statistics
        col = grades[:, i]
        print(f"{exam}:")
        print(f"  Mean: {np.mean(col):.2f}")
        print(f"  Median: {np.median(col):.2f}")
        print(f"  Std Dev: {np.std(col):.2f}")
        print(f"  Min: {np.min(col)}")
        print(f"  Max: {np.max(col)}")

    print(f"Overall Mean: {np.mean(grades):.2f}")
    print(f"Overall Median: {np.median(grades):.2f}")
    print(f"Overall Std Dev: {np.std(grades):.2f}")
    print(f"Overall Min: {np.min(grades)}")
    print(f"Overall Max: {np.max(grades)}")

def pass_fail(grades):
    """
    Calculates the passes and fails for all exams.

    Parameters:
        grades: numpy array of exams

    Variables:
        exams (list): list of exams
        passes (int): number of passes
        fails (int): number of fails
        total_pass (int): total number of passes
        total_fail (int): total number of fails
        total_grades (int): total number of grades
        pass_percentage (float): percentage of students passing

    Logic:
        1. Define exams and passing threshold.
        2. Loop through the exams array.
        3. Count the number of passes and fails.
        4. Calculate overall pass percentage.

    Return:
         None
    """
    exams = ["Exam1", "Exam2", "Exam3"]
    passing_grade = 60

    for i, exam in enumerate(exams):
        col = grades[:, i]
        passes = np.sum(col >= passing_grade)
        fails = np.sum(col < passing_grade)
        print(f"{exam}: {passes} passed, {fails} failed")

    # Calculates the total number of grades
    total_grades = grades.size
    total_passes = np.sum(grades >= passing_grade)
    pass_percentage = (total_passes / total_grades) * 100

    print(f"Overall Pass Percentage: {pass_percentage:.2f}%")

def main():
    """
    Loads data from the grades.csv file.

    Parameters:
        None

    Variables:
        data_structure: full data structure
        grades: numeric grade data of exams

    Logic:
        1. Load the full data structure.
        2. Load numeric grade data.
        3. Call statistics function.
        4. Call pass_fail function.

    Return:
         None
    """

    # Shows a preview of the dataset.
    data_structure = np.genfromtxt('grades.csv', dtype=str, delimiter=',')
    print("First few rows of dataset (full structure):")
    print(data_structure[:4])

    grades = np.genfromtxt('grades.csv', skip_header=1, delimiter=',', usecols=(2, 3, 4))
    print("\nFirst few rows of the numerical grades array:")
    print(grades[:4])
    print()

    statistics(grades)
    pass_fail(grades)

if __name__ == "__main__":
    main()
