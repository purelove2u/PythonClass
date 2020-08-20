import pymysql

try:
    db = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '12345',
        db = 'ecommerce',
        charset = 'utf8'
    )
    cursor = db.cursor()
    sql = """
        delete from product where product_code = '215673140'
        """
    if cursor.execute(sql):
        db.commit()
        print('삭제성공')
        print(cursor.rowcount) # sql 쿼리 실행결과
    else:
        db.rollback()
        print('삭제실패')

except Exception as e:
    print(e)
finally:
    db.close()