import pymysql

try:
    # mysql 접속
    db = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="12345",
        db="ecommerce",
        charset="utf8",
    )

    # cursor 생성
    cursor = db.cursor()

    # sql 구문 생성
    sql = """
        create table if not exists product(
            product_code varchar(20) not null,
            title varchar(200) not null,
            ori_price int,
            discount_price int,
            discount_percent int,
            delibery varchar(2),
            primary key(product_code));
    """
    # sql 구문 실행
    cursor.execute(sql)

    # sql 실행
    cursor.execute("show tables;")

    # sql 실행결과 가져오기
    rows = cursor.fetchall()

    # 결과 출력하기
    for r in rows:
        print("{}".format(r))

except Exception as e:
    print(e)
finally:
    db.close()
