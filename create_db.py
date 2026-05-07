import sqlite3
def create_db():
    con= sqlite3.connect(database="rms.db")
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges text, description text )")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text, gender text, dob text, contact text, admission text,course text, state text, city text,pin text, address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text, name text, course text, marks text, full_marks text, per text)")
    con.commit()
    
    #cur.execute("DROP TABLE employee")
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, f_name TEXT, l_name TEXT,contact TEXT,email TEXT,question TEXT,answer TEXT, password TEXT)")
    con.commit()
    #print("old table deleted")
    
    con.close()

create_db()