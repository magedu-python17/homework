import json

with open("user.json",'r') as load_f:
  d = json.load(load_f)

if not d:
	print('没有数据请先添加数据.')
	option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')
else:
	option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')
switch = True
while switch:
	if option1 == 'add':
		user_name = input('Please input your name:')
		user_data = input('Please input your date:')
		d[user_name] = user_data
		option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')
	if option1 == 'delete':
		user_name = input('Please input your name:')
		del d[user_name]
		option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')
	if option1 == 'update':
		user_name = input('Please input your name:')
		for i in d:
			if user_name in d:
				update_data = input('Please input your new data:')
				d[user_name] = update_data
				break
			else:
				print('用户不存在。。。')
				break
		option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')

	if option1 == 'find':
		user_name = input('Please input your name:')
		print(d.get(user_name,'no data'))
		option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')
	if option1 == 'list':
		print(d)
		option1 = input('请输入你的选择，add添加用户数据，delete删除用户数据，update更新用户数据，find查找用户数据，list打印输出所有用户数据，exit保存退出:')
	if option1 == 'exit':
		json_str = json.dumps(d)
		with open("user.json", "w") as f:
			json.dump(d, f)
			print("加载入信息完成...")
<<<<<<< HEAD
		switch = False
=======
		switch = False

# 作业完成的不错，争取把第二次的作业也补上来哈
>>>>>>> eb050f956f0e1532fde6ba5a848a6855e0f2f0bf
