import pymysql,time
class lyncmysql:
    """ python3 lync mysql """
    _dbconfig = None
    _cursor = None
    _error_code = ''

    TIMEOUT_DEADLINE = 30 #quit connect if beyond 30s
    TIMEOUT_THREAD = 10 #thread hold of one connect
    TIMEOUT_TOTAL = 0 # total time the connects have waste

    def __init__(self,dbconfig):
        try:
            self._dbconfig = dbconfig
            self.dbconfig_check(dbconfig)
            self._connect = pymysql.connect(host=self._dbconfig['host'],
                                            port=self._dbconfig['port'],
                                            user=self._dbconfig['user'],
                                            passwd=self._dbconfig['passwd'],
                                            db=self._dbconfig['db'],
                                            charset=self._dbconfig['charset'],
                                            connect_timeout=self.TIMEOUT_THREAD
                                            )
            self._cursor = self._connect.cursor()#pymysql.cursors.DictCursor)
        except pymysql.Error as e :
            self._error_code = e.args[0]
            error_msg = '{} -> {} {} {}'.format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),type(e).__name__,e.args[0],e.args[1])
            print(error_msg)
            exit()

    def dbconfig_check(self,dbconfig):
        flag = False
        if type(dbconfig) is not dict:
            print('dbconfig is not dict!')
            flag = True
        else:
            for key in ['host','port','user','passwd','db']:
                if not dbconfig.get(key):
                    print('dbconfig error: do not have {}'.format(key))
                    flag = True
            if not dbconfig.get('charset'):
                self._dbconfig['charset'] = 'utf8'

    def query(self,sql):
        try:
            rst = []
            self._cursor.execute(sql)
            for i in self._cursor.fetchall():
                rst.append(i)
            return rst
            # self._cursor.commit()
        except pymysql.Error as e:
            self._error_code = e.args[0]
            print( e.args[0],e.args[1])

    def dml(self,sql):
        try:
            self._cursor.execute(sql)
            self._connect.commit()
        except pymysql.Error as e :
            print(e)

if __name__ == '__main__':
    dbconfig = {'host': '10.10.3.128',
                'port': 3306,
                'user': 'repl',
                'passwd': '123',
                'db': 'python',
                'charset': 'utf8'}
    db=lyncmysql(dbconfig)

