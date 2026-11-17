# 学生成绩管理系统
def show_menu():
    print("=" * 30)
    print("学生成绩管理系统")
    print("1. 添加学生成绩")
    print("2. 查询全部成绩")
    print("3. 修改学生成绩")
    print("4. 删除学生信息")
    print("0. 退出系统")
    print("=" * 30)

stuArray = []

def add_stu():
    name = input("请输入学生姓名：")
    score = input("请输入学生成绩：")
    stuArray.append({"name": name, "score": score})
    print("添加成功！")

def show_all():
    if len(stuArray) == 0:
        print("暂无学生数据")
        return
    print("姓名\t成绩")
    for item in stuArray:
        print(f"{item['name']}\t{item['score']}")

def modify_stu():
    name = input("请输入要修改的学生姓名：")
    for item in stuArray:
        if item["name"] == name:
            item["score"] = input("请输入新成绩：")
            print("修改成功！")
            return
    print("未找到该学生")

def delete_stu():
    name = input("请输入要删除的学生姓名：")
    for item in stuArray:
        if item["name"] == name:
            stuArray.remove(item)
            print("删除成功！")
            return
    print("未找到该学生")

while True:
    show_menu()
    choice = input("请输入功能序号：")
    if choice == "1":
        add_stu()
    elif choice == "2":
        show_all()
    elif choice == "3":
        modify_stu()
    elif choice == "4":
        delete_stu()
    elif choice == "0":
        print("系统已退出")
        break
    else:
        print("输入有误，请重新输入")