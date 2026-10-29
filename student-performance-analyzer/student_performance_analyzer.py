students = [
    {
        "name": "Matin",
        "age": 17,
        "city": "Tabriz",
        "scores": [18, 20, 16]
    },
    {
        "name": "Sara",
        "age": 16,
        "city": "Tehran",
        "scores": [19, 17, 20]
    },
    {
        "name": "Ali",
        "age": 18,
        "city": "Tabriz",
        "scores": [15, 16, 18]
    },
    {
        "name": "Mahdi",
        "age": 17,
        "city": "Shiraz",
        "scores": [20, 19, 18]
    },
    {
        "name": "Reza",
        "age": 16,
        "city": "Tehran",
        "scores": [12, 14, 15]
    }
]
print("========== STUDENT REPORT ==========")
for student in students:
    total_score = 0
    for score in student["scores"]:
        total_score += score
    average = total_score / len(student["scores"])
    student["score average"] = average
    if average >= 18:
        student["status"] = "Excellent"
    elif average >= 15:
        student["status"] = "Good"
    else:
        student["status"] = "Needs Improvement"
    print(student["name"], "|", "Average :", average, "|", "Status :", student["status"])
print("========== CLASS ANALYSIS ==========")
total_average = 0
max_average = 0
max_average_name = ""
more_than_18_average_count = 0
for student in students:
    total_average += student["score average"]
    if student["score average"] > max_average:
        max_average = student["score average"]
        max_average_name = student["name"]
    if student["score average"] >= 18:
        more_than_18_average_count += 1
class_average = total_average / len(students)
print("Class Average :", class_average)
print("Top student :", max_average_name)
print("Excellent Student count :", more_than_18_average_count)
print("========== CITY ANALYSIS ==========")
city_count = {}
for student in students:
    city = student["city"]
    if student["city"] in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
for city in city_count:
    print(city, ":", city_count[city])
max_city = 0
max_city_name = ""
for city in city_count:
    if city_count[city] >= max_city:
        max_city = city_count[city]
        max_city_name = city
for city in city_count:
    if city_count[city] == max_city:
        print("Most common city :", city)
print("========== STUDENT SEARCH ==========")
found = False
searched_name = input("Enter name : ")
for student in students:
    if student["name"].lower() == searched_name.lower():
        found = True
        print("Name :", student["name"])
        print("Age :", student["age"])
        print("City :", student["city"])
        print("Average :", student["score average"])
        print("Status :", student["status"])
if found != True:
    print("Student not found.")
