from csv import reader, writer


def define_database(total_data):
    with open("department_database.csv", "w", newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerows(total_data)


total_data = [["Department ID", "Department Name", "List of Batches"]]

while True:
    dep_name = ""
    dep_id = ""
    batch_list = []
    row_data = []

    print("TO PROCEED, PLEASE CREATE A NEW DEPARTMENT")
    skip = input(
        "If you wish to not create a new department and skip this step, please enter 'skip'.Otherwise, press any other key: ")
    if skip == "skip":
        break

    dep_name = input("Please enter the name of the department: ")
    dep_id = input("Please enter the department id: ")
    print("Enter the list of all the batches within this department")
    while True:
        batch_id = input(
            "Please enter Batch ID.If you are done with listing all the batches, enter 'q' to quit out: ")
        if batch_id == 'q':
            break
        batch_list.append(batch_id)

    row_data = [dep_id, dep_name, batch_list]
    total_data.append(row_data)

    choice = input(
        "Please enter 'quit' to quit making new departments, or enter any other key to continue: ")
    if choice == 'quit':
        # print(total_data)
        define_database(total_data)
        break
