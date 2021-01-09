try:
    file=open("eee","r+")
except Exception as e:
    print("there is no this file")
    response=input("do you want to create a new file")
    if response=='y':
        file=open("eee","w")
    else:
        pass
else:
    file.write("sss")
file.close()