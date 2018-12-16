#/usr/bin/python3
#function: user system 
#author: Jayzhao
#2018年12月16日00:35:08
import json
from pathlib import Path


def add(data):
    name = input("Please enter new name:")
    age = input("Please enter new age:")
    tel = input("Please enter nwe tel:")
    if  name not in data.keys():
        data[name] = {"age":age,"tel":tel}
    return data


def delete(data):
    name = input("Please enter delete username:")
    error = "The name is not exist"
    prompt = data.pop(name,error)
    print(prompt)
    return data


def update(data):
    names = input("Please enter string format:{name:age:tel}:")
    if len(names.split(":")) == 3:
        name,age,tel = names.split(":")
        if name in data.keys():
            data[name] = {"age": age, "tel": tel}
            print("The user update successfully! ")
            print("name:{}\nage:{}\ntel:{}".format(name, data[name].get('age'), data[name].get('tel')))
        else:
            print("name is not exit")
    else:
        print("The format error.")
    return data


def find(data):
    name = input("Please enter find name:")
    if name in data.keys():
        print("name:{}\nage:{}\ntel:{}".format(name,data[name].get('age'),data[name].get('tel')))
    else:
        print("name is not exit")


def list(data):
    print("name\tage\ttel")
    for k,v in data.items():
        print("{}\t{}\t{}".format(k,str(v['age']),str(v['tel'])))



def exit(data,file):
    with open(file,'w') as f:
        json.dump(data,f)
    print("The data saved successfully! exit...")
    
  


def main():
    filename = "users.json"
    path = Path(filename)
    if path.is_file():
        with open(filename) as f:
            users = json.load(f)
            if users:
                pass
            else:
                add(users)
    else:
        users = {}
        add(users)

    while True:
        value = input("Please choose (add|update|find|list|delete|exit):")
        if value == "delete":
            delete(users)
        elif value == "add":
            add(users)
        elif value == "update":
           update(users)
        elif value == "find":
            find(users)
        elif value == "list":
            list(users)
        elif value == "exit":
            exit(users, filename)
            break
        else:
            print("Sorry,Enter error...again check")
            value = input("Please choose (add|update|find|list|delete|exit):")


if __name__ == "__main__":
    main()
