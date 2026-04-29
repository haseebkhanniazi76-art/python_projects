class Student:
    def __init__(self, student_name,math_score, science_score):
        self.student_name = student_name
        self.math_score = math_score
        self.science_score = science_score
    def check_status(self):
        average_score = (self.math_score + self.science_score) / 2
        if average_score >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"
import pandas as pd
df = pd.read_csv("raw_grades.csv")
y = df.fillna(0)
new_student = []
for _, row in y.iterrows():
    s1 = Student(row["student_name"],row["math_score"],row["science_score"])
    s1.check_status()
    new_student.append(s1)
processed_data_dict = {"student_name": [s1.student_name for s1 in new_student],
                       "math_score": [s1.math_score for s1 in new_student],
"science_score": [s1.science_score for s1 in new_student],}
df = pd.DataFrame(processed_data_dict)
df["School_Year"]="2023-2024"
class NewStudent(Student):
    def add_status(self):
        df["Status"] = self.status
        s1.add_status()
print(df)
