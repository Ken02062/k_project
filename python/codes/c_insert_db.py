import pymysql

try:
    # 建立Connection物件
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="log_data", charset="utf8")  # 連線資料庫
    cursor = conn.cursor()  # 傳回 Cursor 物件

    # 建立Cursor物件, 進行相關的操作
    with conn.cursor() as cursor:  # with陳述式，當資料庫存取完成後，自動釋放連線
        cursor.execute("SELECT VERSION()")
        print("Database version : %s " % cursor.fetchone())

        SQL = f"INSERT INTO user_log (u_name) VALUES('Ken')"
        cursor.execute(SQL)
        conn.commit()  # 操作結果寫入資料庫

        cursor.close()  # 關閉 Cursor 物件
        conn.close()  # 關閉 Connection 物件
except Exception as ex:
    print(ex)
