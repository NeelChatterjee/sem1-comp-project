from csv import reader, writer


def define_database(total_data):
    with open("course_database.csv", "w", newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerows(total_data)


total_data = [["Course ID", "Course Name", "Marks Obtained"]]

while True:
    course_name = ""
    course_id = ""
    marks_list = []
    row_data = []

    print("TO PROCEED, PLEASE CREATE A NEW COURSE")
    skip = input(
        "If you wish to not create a new course and skip this step, please enter 'skip'.Otherwise, press any other key: ")
    if skip == "skip":
        break
    course_name = input("Please enter the name of the course: ")
    course_id = input("Please enter the course id: ")
    print("Enter the list of all Student IDs along with their respective marks obtained in the course")
    while True:
        student_id = input(
            "Please enter Student ID: ")
        marks = int(input(
            "Please enter the student's marks in the course: "))
        marks_list.append({student_id: marks})
        exit_choice = input(
            "If you are done with listing all the students and their marks, enter 'q' to quit out: ")
        if exit_choice == 'q':
            break

    row_data = [course_id, course_name, marks_list]
    total_data.append(row_data)

    choice = input(
        "Please enter 'quit' to quit making new courses, or enter any other key to continue: ")
    if choice == 'quit':
        # print(total_data)
        define_database(total_data)
        break
