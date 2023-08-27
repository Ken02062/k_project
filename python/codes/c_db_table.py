import pymysql

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)

    # 建立Cursor物件, 進行相關的操作
    with conn.cursor() as cursor:  # with陳述式，當資料庫存取完成後，自動釋放連線
        cursor.execute("SELECT VERSION()")
        print("Database version : %s " % cursor.fetchone())

        # 建立資料庫
        SQL = "CREATE DATABASE IF NOT EXISTS log_data DEFAULT CHARSET=utf8 DEFAULT COLLATE=utf8_unicode_ci"
        cursor.execute(SQL)
        conn.commit()
        print("Database established!")

        cursor.close()  # 關閉 Cursor 物件
        conn.close()  # 關閉 Connection 物件

        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="log_data", charset="utf8")  # 連線資料庫
        cursor = conn.cursor()  # 傳回 Cursor 物件

        SQL = '''CREATE TABLE IF NOT EXISTS user_log(
        id INT(5) PRIMARY KEY AUTO_INCREMENT,
        u_name VARCHAR(100),
        create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
        ENGINE=InnoDB
        DEFAULT  CHARSET=utf8'''

        cursor.execute(SQL)
        conn.commit()  # 操作結果寫入資料庫
        print("Table established!")
        cursor.close()  # 關閉 Cursor 物件
        conn.close()  # 關閉 Connection 物件
except Exception as ex:
    print(ex)
