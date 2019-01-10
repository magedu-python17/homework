action = input('choice')
db = {'name':'sarah','age':20,'contact':'2 st'}

d= []
if action =='delete':
    for k,v in db.items():
        d.append(k)
    for k in d:
        db.pop(k)

    else:
        print("This name was not available")


elif action =='update':
    user_name,age,contact = input('user_name', 'age', 'contact').split()

    if user_name in db.keys():
        db[user_name] = 'sarah'
        db['age'] = 20
        db['contact'] = '26 st.'

            # use setdefault

        db.setdefault(user_name,'sarah')
        db.setdefault('age',20)
        db.setdefault('contact','2 st.')
    else:
        print('This user doesn"t exist')


elif action =='find':
    user_name = input('sarah')
    age = 20
    contact = '2 st'

    for item in db.items():
        print(item[0],item[1])
    # another method:
    for user_name in db.keys():
        print(db['user_name'], db['age'], db['contact'])
        print('{} is {} years old and he/she lives at {}'.format(user_name, age, contact))

elif action == 'list':
    user_name, age, contact = input('sarah', '20', '2 st').split()

    print('This user has user_name, age and contact information available')
    print()
    print('{}, {}, {}'.format(user_name, age, contact))

elif action == 'exit':
    print('Please save the changed information')
    exit()




# 尝试用while True 试下，正常来说，一个操作系统，应该有用户来选择操作的，而不是运行一次就结束。
# 迭代的时候，迭代对象最好不要增删的操作,你可以试试，看会有结果
# 别的没有什么问题
# 目录改成学号+姓名哈