import os
from student import Student
from manager import GradeManager
print("=== 当前运行路径是：", os.getcwd(), "===")

def main():
    print("欢迎使用学生成绩系统")
    manager = GradeManager()

    while True:
        print("\n1. 添加学生\n2. 添加成绩\n3. 查询学生平均成绩\n4. 显示所有学生成绩\n5. 删除学生成绩\n6. 删除学生\n7. 退出")
        choice = input("请选择操作（1-7）：")

        if choice == '1':
            name = input("学生姓名：")
            student_id = input("学生ID：")
            student = Student(name, student_id)
            manager.add_student(student)

        elif choice == '2':
            sid = input("输入学生ID：")
            student = manager.get_student(sid)
            if student:
                course = input("课程名：")
                grade = float(input("成绩："))
                student.add_grade(course, grade)
                manager.save_to_file()  # 保存到文件
                print(f"已为 {student.name} 添加成绩：{course} - {grade}")  
            else:
                print("未找到该学生")

        elif choice == '3':
            sid = input("输入学生ID：")
            student = manager.get_student(sid)
            if student:
                print(f"{student.name} 的平均成绩是：{student.average():.2f}")
            else:
                print("未找到该学生")

        elif choice == '4':
            manager.print_all_grades()
        
        elif choice == '5':
            sid = input("输入学生ID：")
            student = manager.get_student(sid)
            if student:
                course = input("输入要删除的课程名：")
                student.delete_grade(course)
            else:
                print("未找到该学生")
        
        elif choice == '6':
            sid = input("输入学生ID：")
            manager.delete_student(sid)
            print(f"学生ID {sid} 已删除。")



        elif choice == '7':
            print("退出系统，再见！")
            break

        else:
            print("无效的选项，请重新选择。")

if __name__ == "__main__":
    main()
