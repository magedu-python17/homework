comments= (
    "Implementation note",
    "Changed",
    "ABC for generator"
)

def add_ellipsis(lstinfo,length=10,dic={}):
	dic=dict(zip(lstinfo,[info[:length]+'.......' if len(info)>length else info for info in lstinfo]))
	return '\n'.join(dic.values())
print(add_ellipsis(comments,length=7))
    
# 逻辑上没有问题