import json
import os
from student import Student

class GradeManager:
    def __init__(self):
        self.students = {}  # student_id : Student 对象
        self.filename = "students.json"
        self.load_from_file()

    def add_student(self, student):
        self.students[student.student_id] = student
        self.save_to_file() 
        print("📦 添加学生成功，并调用了保存函数")

    
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            print(f"学生ID {student_id} 不存在。")

    def get_student(self, student_id):
        return self.students.get(student_id)

    def print_all_grades(self):
        print("学生ID\t姓名\t平均成绩")
        for student in self.students.values():
            print(f"{student.student_id}\t{student.name}\t{student.average():.2f}")

    def save_to_file(self):
        data = {sid: stu.to_dict() for sid, stu in self.students.items()}
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            print("✅ 数据已保存到json")


    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = {sid: Student.from_dict(info) for sid, info in data.items()}
