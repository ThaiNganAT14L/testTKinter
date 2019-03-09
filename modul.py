import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db = 'xep_gach_game', autocommit=True)
sqldata = conn.cursor()

def checkID (user):
    sql = "SELECT ID FROM account WHERE User= " + "'" + user +"'"
    sqldata.execute (sql)
    for row in sqldata:
        for i in row:
            return i

def checkPass (user , Pass):
    sql = "SELECT Pass FROM account WHERE User= " + "'" + user +"'"  
    sqldata.execute (sql)
    for row in sqldata:
        if (Pass in row):
            return 1
    return 0        

def checkHistory(id):
    sql = "SELECT History1,History2,History3 FROM information WHERE ID=" + str(id)  
    sqldata.execute (sql)
    for row in sqldata:
        return row

def checkUser (user):
    sql = "SELECT User FROM account "    
    sqldata.execute (sql)
    for row in sqldata:
        if (user in row):
            return 1
    return 0

def creatUser ( user , Pass):
    #tìm Max ID    
    sql1 = "SELECT MAX(ID) FROM account"
    sqldata.execute (sql1)
    for row in sqldata:
        for i in row:
            maxID = i
    # Tạo User mới
    sql2 = "INSERT INTO account (ID, User, Pass) VALUES (%s, %s, %s)" 
    sqldata.execute (sql2, (maxID+1, user, Pass))     
# conn.close()