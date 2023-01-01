from subprocess import call
from csv import reader, writer


def open_student_func_file():
    call(["python", "student_func.py"])


def open_course_func_file():
    call(["python", "course_func.py"])


def open_batch_func_file():
    call(["python", "batch_func.py"])


def open_department_func_file():
    call(["python", "department_func.py"])


def open_examination_file():
    call(["python", "examination.py"])


while True:
    choice_func = input(
        "Please enter:\nSTU - Create/Modify Student Data\nCOU - Create/Modify Course Data\nBAT - Create/Modify Batch Data\nDPT - Create/Modify Department Data\nEXAM - Compute Exam Results\nEXIT - Exit Out Of The Portal\n")
    if choice_func == "EXIT":
        print("You have exited the Portal")
        break

    if choice_func == 'STU':
        open_student_func_file()
        print("\n")

    elif choice_func == 'COU':
        open_course_func_file()
        print("\n")

    elif choice_func == 'BAT':
        open_batch_func_file()
        print("\n")

    elif choice_func == 'DPT':
        open_department_func_file()
        print("\n")

    elif choice_func == 'EXAM':
        open_examination_file()
        print("\n")

    else:
        print("Invalid Input.Please Try Again\n")
