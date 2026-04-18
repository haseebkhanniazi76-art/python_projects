import pandas as pd
class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.status = None

    def check_status(self):
        average = (self.math_score + self.science_score) / 2

        # Pass/Fail logic
        if average >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"
df=pd.read_csv("raw_grades.csv")
df_cleaned = df.fillna(0)

student_objects = []

for index, row in df_cleaned.iterrows():
    student_obj = Student(
        name=row['Student_Name'],
        math_score=row['Math_Score'],
        science_score=row['Science_Score']
    )

    student_obj.check_status()

    student_objects.append(student_obj)


final_list = []
for s in student_objects:
    final_list.append({
        "Name": s.name,
        "Math": s.math_score,
        "Science": s.science_score,
        "Result": s.status
    })

final_report = pd.DataFrame(final_list)

final_report['School_Year'] = "2023-2024"

print("final grading report")
print(final_report)
