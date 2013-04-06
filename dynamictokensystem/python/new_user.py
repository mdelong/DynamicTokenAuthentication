
import uuid
import sqlite3
import sys

def create_user(username):
    token_seed = uuid.uuid4()
    #add username, token_seed to database
    try:
        conn = sqlite3.connect('test.db')
        curs = conn.cursor()
        curs.execute("create table if not exists Users(uid text primary key, token text, count double);")
        
        curs.execute("select * from Users;")
    
        print curs.fetchall()
        print str(token_seed)
        query = "insert into Users values('%s', '%s', %d);" % (username, str(token_seed), 0)
        curs.execute(query)
        conn.commit()
    
    except sqlite3.Error, e:
        print e

    finally:
        if conn:
            conn.close()

def increment_count(username):
    try:
        conn = sqlite3.connect('test.db')
        curs = conn.cursor()

        curs.execute("select count from Users where uid='%s';" % username)
        
        val = curs.fetchall()[0][0] + 1
        print val
    
        curs.execute("update Users set count=%d where uid='%s';" % (val, username))
        conn.commit()
    
        # then generate new token based on namespace (seed + count or possibly new uid), and name (username) uuid.uuid3(namespace, name)
        """ Now we need to figure out how to generate RSA keypair from this UID"""
    
    except sqlite3.Error, e:
        print e
    
    finally:
        if conn:
            conn.close()

def test():
    print uuid.uuid4()
    print uuid.uuid5(uuid.NAMESPACE_DNS, 'sdj')

if __name__ == '__main__':
    test()
    create_user("mdelong")
    create_user("jmoreno")
    increment_count("mdelong")
