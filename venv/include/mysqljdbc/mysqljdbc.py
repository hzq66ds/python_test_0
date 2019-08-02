import pymysql as psql


def __getjdbc():
    db = psql.connect(host='rds89uew2533517ity3crw.mysql.rds.aliyuncs.com',
                      user='paipaizhuanpc', password='paiPai100', db='task', charset='utf8')
    return db


def select(qsql):
    db = __getjdbc()
    try:
        cursor = db.cursor()
        cursor.execute(qsql)
        return cursor.fetchall()
    finally:
        db.close()


def update(qsql):
    db = __getjdbc()
    try:
        cursor = db.cursor()
        cursor.execute(qsql)
    finally:
        db.close()


if __name__ == '__main__':
    data = select("SELECT taskid_owner,DATE_FORMAT(start_time,'%y-%M-%d'),count(1) from t_response where taskid_owner='99c916f528a24a7ba282de575ceb28b9' GROUP BY taskid_owner,DATE_FORMAT(start_time,'%y-%M-%d') order by count(1) desc")
    print(data)
