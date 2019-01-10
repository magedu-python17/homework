#1.判断一个指定的bash脚本是否有语法错误：如果有错误，则提醒用户键入Q或者q无视错误并退出，
#其他任何键会通过vim打开这个指定的脚本
#2.如果用户通过vim打开编辑后保存退出时仍然有错误，则重复第1步，否则就正常关闭退出

#!/bin/bash
#
until /bin/bash -n $1 &>/dev/nell;do
	read -p "Syntax error, [Qq] to quit,others for editing:" CHOICE
    case $CHOICE in
    q|Q)
		echo "Something wrong,quiting."
		exit 5
		;;
	*)
		vim + $1
		;;
	esac
done