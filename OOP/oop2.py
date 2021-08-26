""" Extra lesson in object-oriented programming """

import csv
from participant import Participant  # importing our Participant class from participant.py

STUDENT_DATA = "students.csv"


def read_student_data():

    with open("students.csv") as f:
        reader = csv.DictReader(f)

        for line in reader:
            student_name = line['ï»¿name']  # The CSV file has this as the name for some reason
            student_email = line['email']
            section_number = int(line['section_number'])

            new_student = Participant(student_name, student_email, "student")

            print(f"The participant's name is {new_student.name}")
            print(f"The participant's email is {new_student.email}")
            print(f"The participant's role is {new_student.role}")


def main():
    read_student_data()


if __name__ == "__main__":
    main()
