import mysql.connector
from datetime import datetime
import json
class MysqlWriterPipeline(object):
    def open_spider(self, spider):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ml",
            )
        self.cursor = self.mydb.cursor()
    def close_spider(self, spider):
        print('close spider')
        self.mydb.commit()
    def process_item(self, item, spider):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO crawl_data (domain, title, url, content, created_at) VALUES (%s, %s, %s, %s, %s)"
        val = (item['domain'], item['title'], item['url'], item['content'], now)
        if 'tags' in item:
            tagsstr = json.dumps(item['tags'])
            sql = "INSERT INTO crawl_data (domain, title, url, content, data, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (item['domain'], item['title'], item['url'], item['content'], tagsstr, now)
        self.cursor.execute(sql, val)
        return item
