#coding=GBK
import sys,json
filename='user_infomation.json'
with open(filename) as f_obj:
	info_keeper=json.load(f_obj)

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
		i=input('do you want to update '+info+"'s infomation? yes/no")
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

while True:
	i=input('what you want to do ?:')
	if i == 'list':
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
		update(un)
	elif i == 'delete':
		delname=input('which user name you wanna delete?:')
		delinfo(delname)
	elif i=='exit':
		savefile()
		sys.exit()

# 逻辑上没有问题， 需要添加个提示菜单的操作，还有代码里面有个小问题，你再看看