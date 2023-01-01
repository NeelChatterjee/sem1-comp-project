from csv import reader, writer
from subprocess import call
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

columns = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
student_marks = []


def open_course_py_file():
    call(["python", "course.py"])


func = int(input("Enter:\n1 - Create a new course\n2 - View performance of all students in the course and show Course Statistics\n"))

if func == 1:
    open_course_py_file()
    print("\n\n")


elif func == 2:
    course_id = input(
        "Enter the ID of the Course you wish to view the performance of: ")
    print("Performance Of All Students In The Course:\n")
    print("Name\t\tRoll Number\t\tMarks")
    found_course = False
    with open("course_database.csv", "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row[0] == course_id:
                found_course = True
                marks = row[2]
                stu_id = ''
                stu_marks = ''
                stu_name = ''
                stu_roll = ''
                i = 1
                while i > 0:
                    found_student = False
                    marks = marks[i:len(marks)]
                    stu_id = marks[marks.index('{') + 2:marks.index(':') - 1]
                    stu_marks = marks[marks.index(
                        ':') + 2:marks.index(':') + 4]
                    with open("student_database.csv", "r") as file:
                        csv_reader = reader(file)
                        for row in csv_reader:
                            if row[0] == stu_id:
                                found_student = True
                                stu_name = row[1]
                                stu_roll = row[2]
                                student_marks.append(int(stu_marks))
                                print(
                                    f"{stu_name}\t\t{stu_roll}\t\t{stu_marks}")

                    i = marks.index(',') if ',' in marks else -1
                    if found_student == False:
                        print("Student Not Found")
                    # print(i)

    if found_course == False:
        print("Course Not Found")
    else:
        plt.hist(student_marks, bins=columns, edgecolor='black')

        plt.title("Distribution of Marks of Students")
        plt.xlabel("Number Of Students")
        plt.ylabel("Marks")

        plt.tight_layout()

        plt.show()

else:
    print("Invalid Input.Please Try Again")
