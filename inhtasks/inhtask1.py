class Person:
    def __init__(self, name, surname, age, number, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
        self.email = email

    def introduce(self):
        print(f"Hello, I'm {self.name} {self.surname}. My age is {self.age}. \n")

    def __str__(self):
        return f"Name: {self.name}. Surname: {self.surname}. Age: {self.age}. Phone number: {self.number}. Email: {self.email}"


class Student(Person):
    def __init__(self, faculty, course, group, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faculty = faculty
        self.course = course
        self.group = group
        self.rating = 0
        self.subjects = set()

    def add_subject(self, subjects_list):
        for subject in subjects_list:
            self.subjects.add(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

    def show_subjects(self):
        print(", ".join(self.subjects))

    def set_rating(self, rating):
        self.rating = rating

    def show_rating(self):
        print(self.rating)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}. Faculty: {self.faculty}. Course: {self.course}. Group: {self.group}. Rating: {self.rating}"


class Teacher(Person):
    def __init__(self, experience, specialization, *args, salary=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.experience = experience
        self.specialization = specialization
        self.salary = salary
        self.schedule = {
            "Monday": {},
            "Tuesday": {},
            "Wednesday": {},
            "Thursday": {},
            "Friday": {},
            "Saturday": {},
        }

    def add_schedule_entry(self, group, weekday, time, room):
        if time not in self.schedule[weekday]:
            self.schedule[weekday][time] = {"group": group, "classroom": room}
            return self.schedule[weekday][time]
        print("Schedule entry already exist for this date and time")
        return None

    def delete_schedule_entry(self, weekday, time):
        if time in self.schedule[weekday]:
            entry = self.schedule[weekday][time]
            del self.schedule[weekday][time]
            return entry
        print("Schedule entry does not exist for this date and time")
        return None

    def show_schedule(self, weekday=None):
        return self.schedule[weekday] if weekday else self.schedule

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}. Experience: {self.experience}. Specialization: {self.specialization}."


print("Student: \n")
student = Student(
    "Faculty of Software and Hardware Engineering",
    "Software Engineering",
    "3SE",
    "John",
    "Smith",
    "20",
    "+9834765221",
    "johnsmith@email.com",
)
print(student)

print("\nStudent's rating after setting:")
student.set_rating(3.8)
student.show_rating()

student.add_subject(["System Analysis", "Software Development", "Machine Learning", "Object Oriented Programming"])
print("\nSubjects list after adding:")
student.show_subjects()

student.remove_subject("System Analysis")
print("\nSubjects list after deleting 'System Analysis':")
student.show_subjects()

print("\nGreeting:")
student.introduce()

print("Teacher: \n")
teacher = Teacher("10 years", "Machine Learning", "Mary", "Bell", "35", "+38499912440", "bellmary@email.com", salary=10000)
print(teacher)

teacher.add_schedule_entry("3SE", "Monday", "12:00", 332)
teacher.add_schedule_entry("2HE", "Wednesday", "17:00", 203)
teacher.add_schedule_entry("4DS", "Friday", "10:00", 261)

print("\nSchedule after adding:")
print(teacher.show_schedule())

teacher.delete_schedule_entry("Friday", "10:00")
print("\nSchedule after deleting:")
print(teacher.show_schedule())

print("\nGreeting:")
teacher.introduce()
