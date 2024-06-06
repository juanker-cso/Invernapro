import mysql.connector
from icecream import ic

database = mysql.connector.connect(user='invernadmin',
                                   password='password',
                                   host='localhost',
                                   database='invernapro')

cursor = database.cursor()
cursor.execute("Select * FROM plantas;")
res = cursor.fetchall()
desc = cursor.description
y = []
for _ in cursor.description:
    y.append(_[0])
database.close()
# for x in res:
#     for y in x:
#         print (y, end='-')
#     print(" |")

print(res[2][1])
x = [desc[i][0] for i in range(len(desc))]
print(x)
print(y)
