from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import text

from app.database import engine, SessionLocal


def main():
    # 测试engine 有没有问题
    print("数据库名称：", engine.url.database)
    print("数据库驱动：", engine.url.drivername)

    # 测试session
    with SessionLocal() as session:
        result = session.execute(text("select 1;")).scalar()
        print(result)

    # 通过发射的技术获取数据库中的所有表名
    table_names = inspect(engine).get_table_names()
    print("当前数据表：", table_names)



if __name__ == '__main__':
    main()