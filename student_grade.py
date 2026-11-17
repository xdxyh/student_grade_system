# 学生成绩管理系统
DATA_FILE = "student_data.txt"

def load_data():
    """从本地文件加载学生数据"""
    stu_list = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    name, score = line.split(",")
                    stu_list.append({"name": name, "score": score})
    except FileNotFoundError:
        pass
    return stu_list

def save_data(stu_list):
    """把学生数据保存到本地文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for item in stu_list:
            f.write(f"{item['name']},{item['score']}\n")

def show_menu():
    print("=" * 30)
    print("学生成绩管理系统")
    print("1. 添加学生成绩")
    print("2. 查询全部成绩")
    print("3. 修改学生成绩")
    print("4. 删除学生信息")
    print("0. 退出系统")
    print("=" * 30)

def add_stu(stu_list):
    name = input("请输入学生姓名：")
    score = input("请输入学生成绩：")
    stu_list.append({"name": name, "score": score})
    save_data(stu_list)
    print("添加成功！")

def show_all(stu_list):
    if len(stu_list) == 0:
        print("暂无学生数据")
        return
    print("姓名\t成绩")
    for item in stu_list:
        print(f"{item['name']}\t{item['score']}")

def modify_stu(stu_list):
    name = input("请输入要修改的学生姓名：")
    for item in stu_list:
        if item["name"] == name:
            item["score"] = input("请输入新成绩：")
            save_data(stu_list)
            print("修改成功！")
            return
    print("未找到该学生")

def delete_stu(stu_list):
    name = input("请输入要删除的学生姓名：")
    for item in stu_list:
        if item["name"] == name:
            stu_list.remove(item)
            save_data(stu_list)
            print("删除成功！")
            return
    print("未找到该学生")

def main():
    stuArray = load_data()
    while True:
        show_menu()
        choice = input("请输入功能序号：")
        # 输入容错：非数字不崩溃，给出提示
        if not choice.isdigit():
            print("输入有误，请输入数字序号")
            continue
        choice = int(choice)
        if choice == 1:
            add_stu(stuArray)
        elif choice == 2:
            show_all(stuArray)
        elif choice == 3:
            modify_stu(stuArray)
        elif choice == 4:
            delete_stu(stuArray)
        elif choice == 0:
            print("系统已退出")
            break
        else:
            print("输入有误，请重新输入")

if __name__ == "__main__":
    main()