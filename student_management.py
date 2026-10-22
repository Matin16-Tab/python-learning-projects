students = [
    {"name": "Matin", "score": 18, "city": "Tabriz"},
    {"name": "Sara", "score": 20, "city": "Tehran"},
    {"name": "Mahdi", "score": 7, "city": "Shiraz"},
    {"name": "Hadi", "score": 15, "city": "Tabriz"},
    {"name": "Reza", "score": 22, "city": "Rasht"},
    {"name": "Farhad", "score": 12, "city": "Tehran"}
]
def check_score(score):
    if 0 <= score <= 20:
        if score >= 10:
            return "Accepted"
        else:
            return "Rejected"
    else:
        return "Invalid"
accepted_count = 0
rejected_count = 0
invalid_count = 0
accepted_students = []
cities = set()
for student in students:
    status = check_score(student["score"])
    cities.add(student["city"])
    if status == "Accepted":
        accepted_count += 1
        accepted_students.append(student)
    elif status == "Rejected":
        rejected_count += 1
    else:
        invalid_count += 1
city_counts = {}
for student in students:
    city = student["city"]
    if city in city_counts:
        city_counts[city] += 1
    else:
        city_counts[city] = 1
searched_name = input("Enter name : ")
found = False
for student in students:
    if searched_name == student["name"]:
        print(student)
        found = True
if not found == True:
    print("The name not exist.")
print("Accepted students count :", accepted_count)
print("Rejected students count :", rejected_count)
print("Students have invalid score count :", invalid_count)
print("Accepted students name :")
for student in accepted_students:
    print(student["name"])
print("Cities :", cities)
print("Each city count :", city_counts)
students_with_valid_score = []
for student in students:
    status = check_score(student["score"])
    if status == "Accepted" or status == "Rejected":
        students_with_valid_score.append(student)
ranked_students = sorted(
    students_with_valid_score,
    key=lambda student : student["score"],
    reverse = True
)
print("Students sorted by score :")
for index, student in enumerate(ranked_students):
    print(index+1, student["name"], "-", student["score"])
