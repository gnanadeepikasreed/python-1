
applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nEnter details of applicant", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks: "))

    print("Enter subject marks:")
    s1 = float(input("Subject 1: "))
    s2 = float(input("Subject 2: "))
    s3 = float(input("Subject 3: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Check scholarship eligibility
    if (marks >= 0 and marks <= 100 and
        s1 >= 0 and s1 <= 100 and
        s2 >= 0 and s2 <= 100 and
        s3 >= 0 and s3 <= 100):

        if (marks >= 0 and
            s1 >= 0 and s2 >= 0 and s3 >= 0 and
            attendance >= 0 and income >= 0):

            applicants.append(
                (name, marks, s1, s2, s3, attendance, income)
            )

# Get scholarship eligibility criteria
min_marks = float(input("\nEnter minimum aggregate marks: "))
min_subject = float(input("Enter minimum subject marks: "))
min_attendance = float(input("Enter minimum attendance: "))
max_income = float(input("Enter maximum family income: "))

eligible = []

for student in applicants:
    name, marks, s1, s2, s3, attendance, income = student

    if (marks >= min_marks and
        s1 >= min_subject and
        s2 >= min_subject and
        s3 >= min_subject and
        attendance >= min_attendance and
        income <= max_income):

        eligible.append(student)

# Ranking students
eligible.sort(key=lambda x: (-x[1], -x[5], x[6], x[0]))

# Display results
print("\n----- SCHOLARSHIP RESULTS -----")

if len(eligible) == 0:
    print("No eligible students found.")

else:
    print("\nEligible Students Ranking:")

    rank = 1

    for student in eligible:
        name, marks, s1, s2, s3, attendance, income = student

        print("\nRank:", rank)
        print("Name:", name)
        print("Aggregate Marks:", marks)
        print("Attendance:", attendance)
        print("Family Income:", income)

        rank += 1

print("\nTotal Eligible Students:", len(eligible))
