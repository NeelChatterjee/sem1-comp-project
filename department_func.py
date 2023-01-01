from csv import reader, writer
from subprocess import call
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

x_axis = []
y_axis = []


def open_department_py_file():
    call(["python", "department.py"])


func = int(input("Enter:\n1 - Create a new department\n2 - View all batches in a department\n3 - View average performance of all batches in a department and show department statistics\n"))
print(func)


if func == 1:
    open_department_py_file()
    print("\n\n")

elif func == 2:
    dep_id = input(
        "Please enter the Department ID to display the list of all batches in it: ")
    found = False
    with open("department_database.csv", "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row[0] == dep_id:
                found = True
                print(row[2])
                break

    if found == False:
        print("Department Not Found")

elif func == 3:
    dep_id = input(
        "Please enter the Department ID to view the average performance of all batches in it: ")
    found_department = False
    print("Batch Name\tAverage Percentage Of All Students")
    with open("department_database.csv") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row[0] == dep_id:
                found_department = True
                batch_list = row[2]
                batch_id = ''
                total_marks = 0
                percentage = 0.0
                cumu_percentage = 0.0
                average_percentage = 0.0
                count = 0
                subject_count = 0
                i = 2
                while i > 0:
                    found_batch = False
                    batch_list = batch_list[i:len(batch_list)]
                    batch_id = batch_list[batch_list.index(
                        batch_list[0]) + 1 if batch_list[0] == "'" else batch_list.index(batch_list[0]):batch_list.index("'")]
                    # print(batch_id)
                    with open("batch_database.csv", "r") as file:
                        csv_reader = reader(file)
                        for row in csv_reader:
                            if row[0] == batch_id:
                                found_batch = True
                                batch_name = row[1]
                                stu_name = ''
                                stu_roll = ''
                                student_list = row[4]
                                # print(student_list)
                                stu_id = ''
                                j = 2
                                while j > 0:
                                    found_student = False
                                    student_list = student_list[j:len(
                                        student_list)]
                                    # print(student_list)
                                    index1 = student_list.index(
                                        student_list[0]) + 1 if student_list[0] == "'" else student_list.index(student_list[0])
                                    # print(index1)
                                    index2 = student_list.index("'")
                                    # print(index2)
                                    stu_id = student_list[index1:index2]
                                    # labels.append(stu_id)
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
                                                            id_index = marks.index(
                                                                stu_id)
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
                                                            subject_count += 1

                                                    percentage = total_marks / subject_count
                                                    total_marks = 0
                                                    subject_count = 0
                                        if found_student == True:
                                            cumu_percentage += percentage
                                            count += 1

                                    j = student_list.index(
                                        ',') + 3 if ',' in student_list else -1

                        if cumu_percentage == 0.0 and count == 0:
                            average_percentage = 0
                        else:
                            average_percentage = cumu_percentage / count
                        x_axis.append(batch_name)
                        y_axis.append(average_percentage)
                        cumu_percentage = 0.0
                        count = 0
                        if found_batch == False:
                            print("Batch Not Found")
                        else:
                            print(f"{batch_name}\t\t{average_percentage}")

                    i = batch_list.index(",") + 3 if "," in batch_list else -1

    if found_department == False:
        print("Department Not Found")
    else:
        plt.plot(x_axis, y_axis)
        plt.title("Line Plot Showing Average Performance Of The Department")
        plt.tight_layout()
        plt.show()

else:
    print("Invalid Input.Please Try Again")
