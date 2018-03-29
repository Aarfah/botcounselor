import mysql.connector
import json
questionMode = 0
cnx = mysql.connector.connect(user='sql12229537',password='fduArMVZ7p',host='sql12.freemysqlhosting.net',database='sql12229537')
userid = 1
query= "Select * from userdata where userid='%s'" % (userid)
cursor = cnx.cursor()
tmp = cursor.execute(query)
row = cursor.fetchone()
if row is None:
	print("New User")
else:
	j = json.loads(str(row[1]))
	j['two'] = "changed"
print("Some text")
str = json.dumps(j, ensure_ascii=False)
query = ("INSERT INTO `userdata`(`userid`,`status`) VALUES ('%d','%s') on DUPLICATE KEY UPDATE status='%s'") % (userid,str,str)
print(query)
cursor.execute(query)
cnx.commit()