accepted = 0
rejected = 0
invalid = 0
total_accepted_score = 0
accepted_students = []
above_average_count = 0
students = [
    {
        "name": "Matin",
        "age": 17,
        "score": 21,
        "city": "Tabriz"
    },
    {
        "name": "Sara",
        "age": 17,
        "score": 21,
        "city": "Tehran"
    }, 
    {
        "name": "Mahdi",
        "age":19,
        "score": 17.1,
        "city": "Shiraz"
    },
    {
        "name": "Hadi",
        "age": 18,
        "score": 19,
        "city": "Isfahan"
    },
    {
        "name": "Farhad",
        "age": 15,
        "score": 17,
        "city": "Rasht"
    },
    {
        "name": "Reza",
        "age": 14,
        "score": 19,
        "city": "Rasht"
    }
]
cities = set()
city_counts = {}
for student in students:
    cities.add(student["city"])
    if student["city"] in city_counts:
        city_counts[student["city"]] += 1
    else:
        city_counts[student["city"]] = 1
most_common_city = ""
max_count = 0
for city, count in city_counts.items():
    if count > max_count:
        max_count = count
        most_common_city = city
print("most common city and students no :", most_common_city, max_count)
print("students count every city :", city_counts.items())
def check_score(score):
    if 10 <= score <= 20:
        return "Accepted"
    elif 0 <= score < 10:
        return "Rejected"
    else:
        return "Invalid"
for student in students:
    result = check_score(student["score"])
    if result == "Accepted":
        student["status"] = "Accepted"
        accepted_students.append(student["name"])
        accepted += 1
        total_accepted_score += student["score"]
    elif result == "Rejected":
        student["status"] = "Rejected"
        rejected += 1
    else:
        student["status"] = "Invalid"
        invalid += 1
if accepted >= 1:
    average = total_accepted_score / accepted
    print("Average :", average)
else:
    print("Not valid accepted.")
above_average_students = []
for student in students:
    if accepted >= 1 and student["status"] == "Accepted" and student["score"] > average:
        above_average_count += 1
        above_average_students.append(student["name"])
accepted_students_data = []
for student in students:
    if student["status"] == "Accepted":
        accepted_students_data.append(student.copy())
school_info = ("Danesh", "Tabriz", 1405)
school_name, school_city, school_year = school_info
ranked_students = sorted(
    students,
    key=lambda student : student["score"],
    reverse=True
)
for rank, student in enumerate(ranked_students):
    print(rank+1, student["name"], student["score"])
search_name = input("Enter student name : ")
found = False
for rank, student in enumerate(ranked_students):
    if student["name"] == search_name:
        print(rank+1, student["name"], student["age"], student["score"], student["city"], student["status"])
        found = True
if found == False:
    print("Entered student is not in the list.")
print(school_info[1])
print(school_info[:2])
uppered_school_name = school_name.upper()
print(uppered_school_name)
print(school_name[2:4])
print(school_name[2])
print("Accepted:", accepted)
print("Rejected:", rejected)
print("Invalid:", invalid)
print("Above average students name :", above_average_students)
print("Above average students no :", above_average_count)
