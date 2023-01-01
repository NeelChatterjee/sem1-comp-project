from csv import reader, writer
from subprocess import call


def open_student_py_file():
    call(["python", "student.py"])


func = int(input(
    "Enter:\n1 - Create New Student Profile\n2 - Update Student Details\n3 - Remove a Student from the Database\n4 - Generate report card of a student\n"))
# print(func)

if func == 1:
    open_student_py_file()
    print("\n\n")
elif func == 2:
    with open("student_database.csv", "r") as file:
        csv_reader = reader(file)
        l = []
        u_id = input(
            "Enter the id of the student whose details are to be updated: ")
        found = False
        for row in csv_reader:
            if row[0] == u_id:
                found = True
                name = input("Enter updated name of student: ")
                roll = input("Enter updated roll number: ")
                batch_id = input("Enter updated batch id: ")
                row[1] = name
                row[2] = roll
                row[3] = batch_id
            l.append(row)

        if found == False:
            print("Student Not Found")

        else:
            with open("student_database.csv", "w", newline='') as file:
                csv_writer = writer(file)
                csv_writer.writerows(l)

elif func == 3:
    with open("student_database.csv", "r") as file:
        csv_reader = reader(file)
        l = []
        d_id = input(
            "Enter the id of the student whose details are to be deleted: ")
        found = False
        for row in csv_reader:
            if row[0] == u_id:
                found = True
            else:
                l.append(row)

        if found == False:
            print("Student Not Found")

        else:
            with open("student_database.csv", "w", newline='') as file:
                csv_writer = writer(file)
                csv_writer.writerows(l)

elif func == 4:
    student_id = input(
        "Enter the id of a student to generate his/her Report Card as a text file")
    found = False
    report_card = "Subject\tGrade\tPass/Fail\n"
    total_marks = 0
    percentage = 0.0
    count = 0
    with open("course_database.csv", "r") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            subject = row[1]
            # print(subject)
            grade = ''
            pass_fail = ''
            marks = row[2]
            if student_id in marks:
                found = True
                id_index = marks.index(student_id)
                flag_index = 0
                for i in range(id_index, len(marks)):
                    if marks[i] == ':':
                        flag_index = i
                        break

                # print(id_index)
                subject_marks = int(marks[flag_index+2:flag_index+4])
                # print(subject_marks)
                if subject_marks >= 90:
                    grade = 'A'
                    pass_fail = 'PASS'
                elif subject_marks >= 80:
                    grade = 'B'
                    pass_fail = 'PASS'
                elif subject_marks >= 70:
                    grade = 'C'
                    pass_fail = 'PASS'
                elif subject_marks >= 60:
                    grade = 'D'
                    pass_fail = 'PASS'
                elif subject_marks >= 50:
                    grade = 'E'
                    pass_fail = 'PASS'
                elif subject_marks < 40:
                    grade = 'F'
                    pass_fail = 'FAIL'

                total_marks += subject_marks
                count += 1

            report_card = report_card + \
                f"{subject}\t{grade}\t{pass_fail}\n"

        percentage = total_marks / count
        report_card = report_card + f"\nPercentage = {percentage}"
        file = open("Report Card.txt", "w")
        file.write(report_card)
        file.close()

    if found == False:
        print('Student Not Found')
    else:
        print("Report Card has been generated")

else:
    print("Invalid Input.Please Try Again")
