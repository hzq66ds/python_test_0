import pymysql as psql


class JdbcMysql:
    def __init__(self, host, user, password, db):
        self.jdbcTemplate = psql.connect(
            host=host,
            user=user,
            password=password,
            db=db, charset='utf8')

    def select(self, qsql):
        try:
            cursor = self.jdbcTemplate.cursor()
            cursor.execute(qsql)
            return cursor.fetchall()
        except BaseException:
            print("查询异常:%s" % qsql)

    def update(self, qsql):
        try:
            cursor = self.jdbcTemplate.cursor()
            cursor.execute(qsql)
        except BaseException:
            print("查询异常:%s" % qsql)

    def __del__(self):
        print("__del__")
        self.jdbcTemplate.close()

    def __delete__(self, instance):
        print("__delete__")
        self.jdbcTemplate.close()






