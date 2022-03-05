from flask import Flask, render_template, request ,jsonify
import pymysql

app = Flask(__name__)


db = pymysql.connect(host='13.113.77.146', port=3306, user='root', passwd='123456', db='user', charset='utf8mb4')
cursor = db.cursor()


@app.route('/') #test
def db():

    username = input("Enter username:")
    password = input("Enter password:")
    email = input("Enter email:")

    insert_sql = "insert into userdb (username, password, email)VALUES('" + username + "','" + password +  "','" + email + "');"
    print(insert_sql)
    result = cursor.execute(insert_sql)
    # 提交至 SQL
    db.commit()

    return "result"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)

    # 程式結束時釋放資料庫資源
    cursor.close()
    db.close()  # 關閉連線