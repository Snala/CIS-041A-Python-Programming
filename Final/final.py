import csv
import os


class Student:
    def __init__(self, studentid, last, first):
        self.studentid = studentid
        self.last = last
        self.first = first

    def __eq__(self, right_character):
        return self.studentid == right_character.studentid


class School:
    def __init__(self):
        self.class_rooms = {}

    def create_rooms(self, classroom):
        if not self.class_rooms.get(classroom):
            self.class_rooms[classroom] = []

    def add_student(self, classroom, student):
        self.class_rooms.setdefault(classroom, []).append(student)

    def class_list(self, classroom):
        return self.class_rooms.get(classroom)

    def __str__(self):
        return str(self.class_rooms)


def process_list(process_file):
    s = School()
    with open(process_file, 'r') as csv_file:
        csv_output = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_output:
            if count > 0:
                db_classroom = str(row[0].strip())
                student_id = int(row[1].strip())
                last = str(row[2].strip())
                first = str(row[3].strip())
                s.create_rooms(db_classroom.upper())
                generated_student = Student(student_id, last, first)
                s.add_student(db_classroom, generated_student)
            else:
                count = count + 1
        csv_file.close()
    return s


def main():
    files = [x for x in os.listdir() if x.endswith(".csv")]
    for file in files:
        school = process_list(file)
        print("Here is the entire student/room list: \n {}".format(school))

    search_class = str()
    while search_class != "Q":
        search_class = input("What class do you want to get the list for? (q to quit)")
        search_class = search_class.strip().upper()
        if search_class != "Q":
            search_result = school.class_list(search_class)
            for i in search_result:
                print("Student ID: {}, First Name: {}, Last Name: {}".format(i.studentid, i.first, i.last))
            print("\n\n")
        else:
            print("Bye! Have a good summer!")
            exit(0)



main()