
import sqlite3 as sq
connect = sq.connect("users.db")
age = input("Введите возраст")
cursor = connect.cursor()
f = cursor.execute('''SELECT f_name FROM users where age = (?) and f_name = (?)''', (age, "Олег",)).fetchall()
if f != []:
    for i in f:
        print(i[0])
else:
    print("Таких нет")
connect.close()


#import os.path
#    print(os.path.exists("file.txt"))
#print(os.path.abspath("file.txt"))
#f = open ("file.txt", "r")
#for line in f.readline():
#    print("ABC" + line)
#with open("file.txt", "r") as f:
#    for i in f:
#        print(i)
#print(f.writelines(["хуяч\n", "хуяч"]))
#print(f.tell())
#print(f.read(5))
#f.seek(0)
#print(f.read())
#print(f.tell(5))
#f.close()
#print(f.readline())
#print(f.readline())
#print(f.read(5))
#print(f.read(6))