#coding=GBK
import sys,json,msvcrt
	
def admin_log_in():
	print('plz in put your keywords:')
	chars=[]
	while True:
		newchar=msvcrt.getch().decode(encoding='utf-8')
		if newchar in '\r\n':
			break
		if newchar in '\b' and len(chars):
			del chars[-1]
			msvcrt.putch('\b'.encode(encoding='utf-8'))
			msvcrt.putch(' '.encode(encoding='utf-8'))
			msvcrt.putch('\b'.encode(encoding='utf-8'))
		else:
			chars.append(newchar)
			msvcrt.putch('*'.encode(encoding='utf-8'))
	inputkeyword=''.join(chars)
	if inputkeyword==admin:
		return True
	else:
		print('\nerror keyword')

def sortuserinfo(sortorder):
	fanzidian={}
	fanzidiank=[]
	fanzidianv=[]
	for i,k in info_keeper.items():
		fanzidian[k[sortorder]]=i
	for i in sorted(fanzidian.keys()):
		fanzidiank.append(i)
	for i in fanzidiank:
		fanzidianv.append(fanzidian[i])
	for i in fanzidianv:
		# ~ for k,v in info_keeper[i].items():
			# ~ print(k+':'+v)
		findinfo(i)

def findinfo(info):
	print('')
	if info not in info_keeper:
		print('No massage!')
		return True
	else:
		for user_info,massage_info in info_keeper.items():
			if info in user_info:
				for massage_key,massage_value in massage_info.items():
					print(massage_key+':'+massage_value)
	print('')

def addinfo(info):
	info_keeper[info]={}
	info_keeper[info]['user_name']=input('please input user name: ')
	info_keeper[info]['age']=input('please input your age: ')
	info_keeper[info]['phone']=input('please input your phone number: ')
	savefile()
	print('')

def listinfo():
	for user_info,massage_info in info_keeper.items():
		print('')
		for massage_key,massage_value in massage_info.items():
			print(massage_key+':'+massage_value)
	print('')
	
def delinfo(info):
	if not findinfo(info):
		delinput=input('enter y to delete those infomation:')
		if delinput=='y':
			del info_keeper[info]
			print('successfully delete!')
			savefile()
	print('')

def updateinfo(info):
	if not findinfo(info):
		i=input('do you want to update '+info+"'s infomation? yes/no:")
		if i=='yes':
			info_keeper[info]['user_name']=input('please input user name: ')
			info_keeper[info]['age']=input('please input your age: ')
			info_keeper[info]['phone']=input('please input your phone number: ')
			print('massage has been update' )
			savefile()
			print('')
	
def savefile():
	with open(filename,'w') as f_obj:
		json.dump(info_keeper,f_obj)
		print('massage has been kept')

###############打开用户文件,初次运行设置密码#######################
filename='user_infomation.json'
with open(filename) as f_obj:
	info_keeper=json.load(f_obj)

try:
	with open('admin_info.json') as f_obj:
		admin=json.load(f_obj)
except FileNotFoundError:
	admin=input('set admin key word:')
	with open('admin_info.json','w') as f_obj:
		json.dump(admin,f_obj)
		print('admin keyword has setted')

#################运行程序##################################
while True:
	if admin_log_in():
		print('\nyou can input "help"to get help')
		while True:
			i=input('what you want to do ?:')
			if i=='help':
				print("""
	list: show all user infomation
	find: find a order infomation
	update: update user infomation
	delete: delete user infomation
	exit: exit this programming
	sort:Sort by requirement for showing

	""")
			elif i == 'list':
				listinfo()
			elif i == 'find':
				un=input("who's massage you wanna find?:")
				if findinfo(un):
					k=input('do you wanna add '+un+"'s infomation?"+
						" enter y to add: ")
					if k=='y':
						addinfo(un)
			elif i == 'update':
				un=input('please enter user infomation for update:')
				updateinfo(un)
			elif i == 'delete':
				delname=input('which user name you wanna delete?:')
				delinfo(delname)
			elif i=='sort':
				sortorder=input('''What sort of order do you want?\nplz input user_name\age\phone:''')
				sortuserinfo(sortorder)
			elif i=='exit':
				savefile()
				sys.exit()

# 作业没有什么问题，记得区分下目录哈，比如01 就放第一次的作业
