from csv import reader, writer


def define_database(total_data):
    with open("student_database.csv", "w", newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerows(total_data)


total_data = [["Student ID", "Name", "Class Roll Number", "Batch ID"]]

while True:
    student_name = ""
    student_id = ""
    roll_no = ""
    batch_id = ""

    print("TO PROCEED, PLEASE CREATE A NEW STUDENT PROFILE")
    skip = input(
        "If you wish to not create a new student profile and skip this step, please enter 'skip'.Otherwise, press any other key: ")
    if skip == "skip":
        break
    student_name = input("Please enter the name of the student: ")
    student_id = input("Please enter the student id: ")
    roll_no = input("Please enter the student's class roll number: ")
    batch_id = input(
        "Please enter the ID of the Batch to which the student belongs: ")

    row_data = [student_id, student_name, roll_no, batch_id]
    total_data.append(row_data)

    choice = input(
        "Please enter 'quit' to quit making new student profiles, or enter any other key to continue: ")
    if choice == 'quit':
        # print(total_data)
        define_database(total_data)
        break
