class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # 课程: 成绩

    def add_grade(self, course, grade):
        self.grades[course] = grade
    
    def delete_grade(self, course):
        if course in self.grades:
            del self.grades[course]
        else:
            print(f"课程 {course} 不存在于 {self.name} 的成绩中。")


    def average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0.0
    
    
    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data):
        s = Student(data["name"], data["student_id"])
        s.grades = data.get("grades", {})
        return s

