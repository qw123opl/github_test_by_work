import pymysql

db_setting= {
    "host" : "localhost",#35.234.31.31
    "port" : 3306,
    "user" : "root",
    "password" : "As29563427!",
    "db" : "test_data",
    "charset" : "utf8" #gbk
}
conn = pymysql.connect(**db_setting)

try:
    with conn.cursor() as cur:
        
        print("連線成功")

        command = f"select * from test_data.charts"
        cur.execute(command)

        data = cur.fetchall()

        print("查詢完成")
        conn.commit()

        print()
        print(data)

except Exception as ex:
    print(ex)