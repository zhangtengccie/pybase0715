import sqlite3
import os

homework_dict = [{'姓名': '学员1', '年龄': 33, '作业数': 1},
                 {'姓名': '学员2', '年龄': 35, '作业数': 5},
                 {'姓名': '学员3', '年龄': 22, '作业数': 22}, ]

# if os.path.exists('homework_standarddb.sqlite'):
#     os.remove('homework_standarddb.sqlite')
# conn = sqlite3.connect('homework_standarddb.sqlite')
# cursor = conn.cursor()
#
#
# cursor.execute('create table homework_info (姓名 varchar(40),年龄 int,作业数 int)')
#
# for teacher in homework_dict:
#     name = teacher['姓名']
#     age = teacher['年龄']
#     homework = teacher['作业数']
#     cursor.execute('insert into homework_info values("{0}","{1}","{2}")'.format(name,age,homework))
#
# conn.commit()


user_notify = '''
请输入查询选项：
输入1 ：查询整个数据库
输入2 ：基于姓名查询
输入3 ：基于年龄查询
输入4 ：基于作业数查询
输入0 ：退出
'''


def search_result_str(searcha_sql):
    conn = sqlite3.connect('homework_standarddb.sqlite')
    cursor = conn.cursor()
    all_search_info = cursor.execute(searcha_sql)
    all_description = [des[0] for des in all_search_info.description]
    search_result = cursor.fetchall()
    if not search_result:
        conn.close()
        return '学员信息未找到'
    return_str = ''
    for x in search_result:
        for y in zip(all_description, x):
            return_str += f"{y[0]:>5}:{y[1]:<5}"
        return_str += '\n'
    conn.close()
    return return_str



while True:
    print(user_notify)
    user_input = input('请选择： ')
    if user_input == '0':
        break
    elif user_input == '1':
        print(search_result_str('select * from homework_info'))
    elif user_input == '2':
        user_sn = input('请输入姓名： ')
        if not user_sn:
            continue
        print(search_result_str("select * from homework_info where 姓名='{0}'".format(user_sn)))
    elif user_input == '3':
        user_age= input('请输入年龄： ')
        if not user_age:
            continue
        print(search_result_str("select * from homework_info where 年龄>'{0}'".format(user_age)))
    elif user_input == '4':
        user_homework= input('请输入作业数： ')
        if not user_homework:
            continue
        print(search_result_str("select * from homework_info where 作业数>'{0}'".format(user_homework)))