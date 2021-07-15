import _sqlite3

homework_dict = [{'姓名':'学员1','年龄':33,'作业数':1},
                 {'姓名':'学员2','年龄':35,'作业数':5},
                 {'姓名':'学员3','年龄':22,'作业数':22},]

conn = _sqlite3.connect('homeworkdb.sqlite')
cursor = conn.cursor()
#
# cursor.execute('create table homework_info (姓名 varchar(40),年龄 int,作业数 int)')
# cursor.execute('insert into homework_info(姓名,年龄,作业数) values("学员1",33,1)')
# cursor.execute('insert into homework_info(姓名,年龄,作业数) values("学员2",35,5)')
# cursor.execute('insert into homework_info(姓名,年龄,作业数) values("学员3",22,22)')
# for teacher in homework_dict:
#     name = teacher['姓名']
#     age = teacher['年龄']
#     homework = teacher['作业数']
# conn.commit()

user_notify = '''
请输入查询选项：
输入1 ：查询整个数据库
输入2 ：基于姓名查询
输入3 ：基于年龄查询
输入4 ：基于作业数查询
输入0 ：退出
'''
while True:
    print(user_notify)
    user_input = input('请选择：')
    if user_input == '1':
        cursor.execute('select * from homework_info')
        results = cursor.fetchall()
        for teacher  in results :
            print(f'学员姓名：{teacher[0]} 学员年龄：{teacher[1]} 学员作业数:{teacher[2]}')
    elif user_input =='2':
        user_sn = input('请输入学员姓名：')
        if not user_sn:
            continue
        cursor.execute(f'select * from homework_info where 姓名="{user_sn}"')
        results =cursor.fetchall()
        if not results:
            print('学员信息未找到！')
        for teacher in results:
            print(f'学员姓名：{teacher[0]} 学员年龄：{teacher[1]} 学员作业数:{teacher[2]}')
    elif user_input=='3':
        user_age = input('搜索大于输入年龄的学员，请输入学员年龄：')
        if not user_age:
            continue
        cursor.execute(f'select * from homework_info where 年龄>"{user_age}"')
        results = cursor.fetchall()
        if not results:
            print('学员信息未找到！')
        for teacher in results:
            print(f'学员姓名：{teacher[0]} 学员年龄：{teacher[1]} 学员作业数:{teacher[2]}')
    elif user_input=='4':
        user_homework = input('搜索大于输入作业数的学员，请输入作业数：')
        if not user_homework:
            continue
        cursor.execute(f'select * from homework_info where 作业数>"{user_homework}"')
        results = cursor.fetchall()
        if not results:
            print('学员信息未找到！')
        for teacher in results:
            print(f'学员姓名：{teacher[0]} 学员年龄：{teacher[1]} 学员作业数:{teacher[2]}')
    elif user_input=='0':
        break
    else:
        print('输入错误，请重试')




