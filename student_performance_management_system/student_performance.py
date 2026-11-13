students = [
    {
        "id":101,
        "name":"Matin",
        "age":16,
        "city":"Tabriz",
        "scores":[18, 19, 17]
    },
    {
        "id":102,
        "name":"Sara",
        "age":17,
        "city":"Tehran",
        "scores":[20, 19, 18]
    },
    {
        "id":103,
        "name":"Ali",
        "age":16,
        "city":"Tabriz",
        "scores":[12, 14, 15]
    },
    {
        "id":104,
        "name":"Hadi",
        "age":17,
        "city":"Shiraz",
        "scores":[16, 18, 17]
    },
    {
        "id":105,
        "name":"Reza",
        "age":16,
        "city":"Tehran",
        "scores":[9, 11, 10]
    },
    {
        "id":106,
        "name":"Mahdi",
        "age":17,
        "city":"Rasht",
        "scores":[19, 18, 20]
    },
    {
        "id":107,
        "name":"Amir",
        "age":16,
        "city":"Tabriz",
        "scores":[14, 13, 16]
    }
]

def display_students(students):
    for student in students:
        print("Student id :", student["id"])
        print("Student name :", student["name"])
        print("Student age :", student["age"])
        print("Student city :", student["city"])
        print("Student scores :", student["scores"])
        
def calculate_averages(students):
    for student in students:
        total_score = 0
        for score in student["scores"]:
            total_score += score
        student["average"] = total_score / len(student["scores"])

def check_student_status(students):
    for student in students:
        if 15 <= student["average"] <= 20:
            student["status"] = "Excellent"
        elif 10 <= student["average"] < 15:
            student["status"] = "Accepted"
        else:
            student["status"] = "Rejected"

def search_student(students, name):
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student id :", student["id"])
            print("Student name :", student["name"])
            print("Student city :", student["city"])
            print("Student age :", student["age"])
            print("Student scores :", student["scores"])
            found = True
    if found != True:
        print("Student not found!")




def show_city_statistics(students):
    cities = set()
    for student in students:
        cities.add(student["city"])
    for city in cities:
        student_count = 0
        total_average = 0
        city_average = 0
        for student in students:
            if student["city"] == city:
                student_count += 1
                total_average += student["average"]
        city_average = total_average / student_count
        print("City name :", city)
        print("Student count :", student_count)
        print("City average :", city_average)
                
def show_top_students(students):
    highest_average = 0
    for student in students:
        if student["average"] > highest_average:
            highest_average = student["average"]
    for student in students:
        if student["average"] == highest_average:
            print("Student name :", student["name"])
            print("Student city :", student["city"])
            print("Student average :", student["average"])
            
display_students(students)
print("-_-_-_-_-_-_-_-_-_-_-_-_-")
calculate_averages(students)
check_student_status(students)
show_city_statistics(students)
search_student(students, "Matin")
print("-_-_-_-_-_-_-_-_-_-_-_-_-")
show_top_students(students)

