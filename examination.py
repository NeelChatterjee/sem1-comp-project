from csv import reader, writer
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

student_marks = []
student_exam_marks = []
student_names = []
student_rolls = []

print("Enter marks of all students for a specific examination, view performance of all students in the examination and display examination statistics in form of a Scatter Plot\n")


course_name = input(
    "Please enter the Course Name for which the examination was conducted: ")
found_course = False
with open("course_database.csv", "r") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        if row[1] == course_name:
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
                            student_names.append(stu_name)
                            stu_roll = row[2]
                            student_rolls.append(stu_roll)
                            stu_exam_marks = input(
                                f"Enter marks obtained in exam for student {stu_name} with roll number {stu_roll}: ")
                            student_exam_marks.append(int(stu_exam_marks))
                            student_marks.append(int(stu_marks))

                i = marks.index(',') if ',' in marks else -1
                if found_student == False:
                    print("Student Not Found")
                # print(i)

if found_course == False:
    print("Course Not Found")
else:
    print("Student Name\t\tRoll Number\t\tMarks Obtained in Exam")
    for i in range(len(student_names)):
        print(
            f"{student_names[i]}\t\t\t{student_rolls[i]}\t\t\t{student_exam_marks[i]}")
    print("\n")

    plt.scatter(student_marks, student_exam_marks)

    plt.show()
