nametb=['zhangsan','lishi','wangwu','zhaoliu']
agetb=['18','22','30','44']
cnttb=['13522222222','13733333333','14533333333','55555555']
while True:
    print('用户信息格式 >>> Name:Age:Contect')
    print('命令 >>> delete,update,find,list,exit')
    cmd = input("Please input a cmd:").lower()
    if cmd == 'delete':
        name=input('请输入一个用户名:')
        if nametb.count(name) > 0:
            ind=nametb.index(name)
            nametb.remove(nametb[ind])
            agetb.remove(agetb[ind])
            cnttb.remove(cnttb[ind])
            print(nametb)
            print(agetb)
            print(cnttb)
            continue
        else:
            print('查无此人')
            continue
    if cmd == 'update':
        print('用户信息格式<<<Name:Age:Contect>>>')
        userinfo=input('>>>')
        upuser=userinfo.split(':')
        if nametb.count(upuser[0]) > 0: #如果用户存在，更新
            f1 = nametb.count(upuser[0])
            i1 = nametb.index(upuser[0])
            agetb[i1]=upuser[1]
            cnttb[i1]=upuser[2]
            print(nametb)
            print(agetb)
            print(cnttb)
            continue
        else: #如果用户不存在，增加此用户
            nametb.append(upuser[0])
            agetb.append(upuser[1])
            cnttb.append(upuser[2])
            print(nametb)
            print(agetb)
            print(cnttb)
            continue
    if cmd == 'find':
        name=input('请输入一个用户名:')
        ind=nametb.index(name)
        print(nametb[ind],agetb[ind],cnttb[ind])
        continue
    if cmd=='list':
        print(nametb)
        print(agetb)
        print(cnttb)
        continue
    if cmd=='exit':
        break
    else:
        print('查无此人')
        continue

