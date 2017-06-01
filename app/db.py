import utils
import MySQLdb as mysql

class Cursor():
    def __init__(self, config):
        self.config = dict([k[6:], config[k] for k in config if k.startwith('mysql_')])
        if 'port' in self.config:
            self.config['port'] = int(self.config['port'])
        if self.config:
            self._connect_db()
    
    def _connect_db(self):
        self.db = mysql.connect(**self.config)
        self.db.autocommit(True)
        self.cur = self.db.cursor()
        print self.db

    def _close_db(self):
        self.cur.close()
        self.db.close()

    def _execute(self, sql):
        try:
            return self.cur.execute(sql)
        except:
            self._close_db()
            self._connect_db()
            return self.cur.execute(sql)

    def _fetchone(self):
        return self.cur.fetchone()

    def _fetchall(self):
        return self.cur.fetchall()

    def _insert_sql(self, table_name, data):
        fields ,values = [], []
        for k, v in data.items():
            fields.append(k)
            values.append("'%s'" % v)
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, ','.join(fields), ','.join(values)
        utils.write_log('api').info("Insert sql: %s" % sql)
        return sql

    def execute_insert_sql(self, table_name , data):
        


