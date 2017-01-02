
import uuid, pymysql


def DB_connect():
    conn = pymysql.connect(host='toyrds.c0wrmbs8zzag.ap-northeast-2.rds.amazonaws.com', port=3306, user='root',password='rootroot', db='cupid', charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    return conn, curs


def post_select():
    conn, curs = DB_connect()
    sql = "select * from cupid.post ORDER BY date DESC"
    res = curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    conn.close()
    return rows

def post_insert(post):
    conn, curs = DB_connect()
    post['uuid'] = str(uuid.uuid4())
    sql = "INSERT INTO cupid.post(date, content,name,uuid) VALUES (%s, %s, %s, %s)"
    print(str(post['date']))
    print(post['date'])
    curs.execute(sql,(str(post['date']), str(post['content']), str(post['name']), str(post['uuid'])))
    curs.fetchall()
    conn.commit()
    conn.close()
    return


def post_update(modifyPost):
    conn, curs = DB_connect()
    sql = "UPDATE cupid.post SET content = %s WHERE uuid = %s"
    curs.execute(sql, (str(modifyPost['content']), str(modifyPost['uuid'])))
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