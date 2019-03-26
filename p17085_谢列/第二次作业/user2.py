import json
with open("user2.json",'r') as load_f:
	d = json.load(load_f)
administrator = input('请设置管理员密码：')
if not d:
	print('没有数据请先添加数据.')
	option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
else:
	option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
switch = True
lst1 = []
guess = 3
while switch:
	if option1 == 'add':
		validation = input('请输入管理员密码：')
		if validation == administrator and guess > 0 :
			print('密码正确！')
			user_name = input('Please input your name:')
			user_gender = input('Please input your gender:')
			user_age = input('Please input your age:')
			user_phone_number = input('Please input your phone number:')
			user_data = {'user_gender': user_gender, 'user_age': user_age, 'user_phone_number': user_phone_number}
			d[user_name] = user_data
			option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
		else:
			print('密码错误！')
			guess -= 1
			print('你还有'+str(guess)+'机会输入')

		if guess == 0 :
			break
	if option1 == 'delete':
		validation = input('请输入管理员密码：')
		if validation == administrator and guess > 0 :
			user_name = input('Please input your name:')
			del d[user_name]
			option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
		else:
			print('密码错误！')
			guess -= 1
			print('你还有' + str(guess) + '机会输入')

		if guess == 0:
			break
	if option1 == 'update':
		validation = input('请输入管理员密码：')
		if validation == administrator and guess > 0 :
			user_name = input('Please input your name:')
			for i in d:
				if user_name in d:
					user_gender = input('Please input your gender:')
					user_age = input('Please input your age:')
					user_phone_number = input('Please input your phone number:')
					user_data = {'user_gender': user_gender, 'user_age': user_age, 'user_phone_number': user_phone_number}
					d[user_name] = user_data
					break
				else:
					print('用户不存在。。。')
					break
			option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
		else:
			print('密码错误！')
			guess -= 1
			print('你还有' + str(guess) + '机会输入')

		if guess == 0:
			break
	if option1 == 'find':
		validation = input('请输入管理员密码：')
		if validation == administrator and guess > 0 :
			user_name = input('Please input your name:')
			print(d.get(user_name,'no data'))
			option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
		else:
			print('密码错误！')
			guess -= 1
			print('你还有' + str(guess) + '机会输入')

		if guess == 0:
			break
	if option1 == 'list':
		validation = input('请输入管理员密码：')
		if validation == administrator and guess > 0 :
			print(sorted(d))
			option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')
		else:
			print('密码错误！')
			guess -= 1
			print('你还有' + str(guess) + '机会输入')

		if guess == 0:
			break
	if option1 == 'exit':
		validation = input('请输入管理员密码：')
		if validation == administrator:
			json_str = json.dumps(d)
			with open("user2.json", "w") as f:
				json.dump(d, f)
				print("加载入信息完成...")
			switch = False
		else:
			print('密码错误！')
			guess -= 1
			print('你还有' + str(guess) + '机会输入')

		if guess == 0:
			break
	if option1 == 'sorted':
		option2 = input('请输入你想要排序的类型字段，age，gender,phone:')
		if option2 == 'age':
			for i in d.values():
				lst1.append(i.get('user_age'))
		elif option2 == 'gender':
			for i in d.values():
				lst1.append(i.get('user_gender'))
		elif option2 == 'phone':
			for i in d.values():
				lst1.append(i.get('user_phone_number'))
		print(sorted(lst1))
		lst1 = []
		option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出,sorted选择字段排序:')

# 写的不错，尝试用函数的方法写下

