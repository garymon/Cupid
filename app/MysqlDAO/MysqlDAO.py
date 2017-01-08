import uuid, pymysql
from config import *

def DB_connect():
    conn = pymysql.connect(host=MYSQL_URL, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWD, db=MYSQL_DBNAME, charset=MYSQL_CHARSET)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    return conn, curs


def post_select(page_size=None, page_num=None):
    conn, curs = DB_connect()
    if page_size is not None and page_num is not None:
        #select post with limit
        sql = "select * from cupid.post ORDER BY date DESC LIMIT %s, %s"%(page_size * page_num, page_size)
    else:
        #select all posts
        sql = "select * from cupid.post ORDER BY date DESC"

    res = curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    conn.close()
    return rows

def post_insert(post):
    conn, curs = DB_connect()
    post['uuid'] = str(uuid.uuid4())
    #sql = "INSERT INTO cupid.post(date, content,name,uuid) VALUES ('%s', '%s', '%s', '%s')"%(str(post['date']), str(post['content'].encode('utf-8')), str(post['name'].encode('utf-8')), str(post['uuid']))
    sql = "INSERT INTO cupid.post(date, content,name,uuid) VALUES (%s, %s, %s, %s)"
    curs.execute(sql,(str(post['date']), str(post['content'].encode('utf-8')), str(post['name'].encode('utf-8')), str(post['uuid'])))
    #curs.execute(sql)
    curs.fetchall()
    conn.commit()
    conn.close()
    return

def post_update(modifyPost):
    conn, curs = DB_connect()
    sql = "UPDATE cupid.post SET content = %s WHERE uuid = %s"
    curs.execute(sql, (str(modifyPost['content'].encode('utf-8')), str(modifyPost['uuid'])))
    curs.fetchall()
    conn.commit()
    conn.close()
    return

def post_delete(removePost):
    conn, curs = DB_connect()
    sql = "DELETE FROM cupid.post WHERE uuid = %s"
    curs.execute(sql, str(removePost['uuid']))
    curs.fetchall()
    conn.commit()
    conn.close()
    return