from utilities.configurations import *


con = createConnection()
cursor = con.cursor()
cursor.execute("SELECT * FROM CustomerInfo")
# rowOne = cursor.fetchone()
# print(rowOne)
# print(rowOne[3])
rows = cursor.fetchall()
num = 0
for row in rows:
    num = num + row[2]
print("Sum of Book Amounts: ", num)

updateLocationQuery = "UPDATE CustomerInfo SET Location = %s WHERE CourseName = %s"
data = ("Siraha", "Python")
cursor.execute(updateLocationQuery, data)
con.commit()

deleteCourse = "DELETE from CustomerInfo WHERE CourseName = %s AND Location = %s "
course = ('TypeScript', 'Jaynagar')
cursor.execute(deleteCourse, course)
con.commit()

con.close()