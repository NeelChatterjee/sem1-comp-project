from csv import reader, writer


def define_database(total_data):
    with open("batch_database.csv", "w", newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerows(total_data)


total_data = [["Batch ID", "Batch Name", "Department ID",
               "List of Courses", "List of Students"]]

while True:
    batch_id = ""
    batch_name = ""
    dep_name = ""
    course_list = []
    student_list = []
    row_data = []

    print("TO PROCEED, PLEASE CREATE A NEW BATCH")
    skip = input(
        "If you wish to not create a new batch and skip this step, please enter 'skip'.Otherwise, press any other key: ")
    if skip == "skip":
        break
    batch_name = input("Please enter the name of the batch: ")
    batch_id = input("Please enter the batch id: ")
    dep_name = input("Please enter the department name: ")
    print("Enter the list of all the courses within this batch: ")
    while True:
        course_id = input(
            "Please enter Course ID.If you are done with listing all the courses, enter 'q' to quit out: ")
        if course_id == 'q':
            print("Enter the list of all the student enrolled in this(these) course(s): ")
            while True:
                student_id = input(
                    "Please enter Student ID.If you are done listing all the students, enter 'exit' to exit: ")
                if student_id == 'exit':
                    break
                student_list.append(student_id)
            break
        course_list.append(course_id)

    row_data = [batch_id, batch_name, dep_name, course_list, student_list]
    total_data.append(row_data)

    choice = input(
        "Please enter 'quit' to quit making new batches, or enter any other key to continue: ")
    if choice == 'quit':
        # print(total_data)
        define_database(total_data)
        break
