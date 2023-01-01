from csv import reader, writer
from subprocess import call
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = []
labels = []


def open_batch_py_file():
    call(["python", "batch.py"])


func = int(input("Enter:\n1 - Create a new Batch\n2 - View list of all students and list of all courses in a Batch\n3 - View complete performance of all students in a Batch and display a Pie Chart showing their percentages\n"))

if func == 1:
    open_batch_py_file()
    print("\n\n")

elif func == 2:
    batch_id = input("Enter a Batch ID: ")
    found = False
    with open("batch_database.csv", "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row[0] == batch_id:
                print("List Of All Students\t\t\tList Of All Courses")
                found = True
                print(f"{row[4]}\t\t\t\t{row[3]}")
                break
        if found == False:
            print("Batch Not Found")

elif func == 3:
    batch_id = input("Enter a Batch ID: ")
    found_batch = False
    total_marks = 0
    percentage = 0.0
    count = 0
    print("Student Name\t\tRoll Number\t\tPercentage")
    with open("batch_database.csv", "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row[0] == batch_id:
                found_batch = True
                stu_name = ''
                stu_roll = ''
                student_list = row[4]
                # print(student_list)
                stu_id = ''
                i = 2
                while i > 0:
                    found_student = False
                    student_list = student_list[i:len(student_list)]
                    # print(student_list)
                    index1 = student_list.index(
                        student_list[0]) + 1 if student_list[0] == "'" else student_list.index(student_list[0])
                    # print(index1)
                    index2 = student_list.index("'")
                    # print(index2)
                    stu_id = student_list[index1:index2]
                    labels.append(stu_id)
                    # print(stu_id)
                    # print()
                    with open("student_database.csv", "r") as file:
                        csv_reader = reader(file)
                        for row in csv_reader:
                            if row[0] == stu_id:
                                found_student = True
                                stu_name = row[1]
                                stu_roll = row[2]
                                with open("course_database.csv", "r") as file:
                                    csv_reader = reader(file)
                                    next(csv_reader)
                                    for row in csv_reader:
                                        subject = row[1]
                                        # print(subject)
                                        marks = row[2]
                                        if stu_id in marks:
                                            found = True
                                            id_index = marks.index(stu_id)
                                            flag_index = 0
                                            for i in range(id_index, len(marks)):
                                                if marks[i] == ':':
                                                    flag_index = i
                                                    break

                                            # print(id_index)
                                            subject_marks = int(
                                                marks[flag_index+2:flag_index+4])
                                            # print(subject_marks)

                                            total_marks += subject_marks
                                            count += 1

                                    percentage = total_marks / count
                                    total_marks = 0
                                    count = 0
                                    slices.append(percentage)
                                # student_marks.append(int(stu_marks))
                                print(
                                    f"{stu_name}\t\t\t\t{stu_roll}\t\t{percentage}")

                    i = student_list.index(
                        ',') + 3 if ',' in student_list else -1
                    if found_student == False:
                        print("Student Not Found")
                    # print(i)

    if found_batch == False:
        print("Batch Not Found")
    else:
        plt.pie(slices, labels=labels, shadow=True,
                autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

        plt.title("Pie Chart Displaying Student Percentages")
        plt.tight_layout()
        plt.show()

else:
    print("Invalid Input.Please Try Again")
