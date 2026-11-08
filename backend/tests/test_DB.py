from datetime import datetime

import sqlalchemy
import pymysql
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

print(sqlalchemy.__version__)  # 打印 SQLAlchemy 版本号，如 2.0.49
print(pymysql.__version__)     # 打印 pymysql 版本号，如 2.2.8


# 1. 定义MySQL连接字符串（格式：数据库驱动://用户名:密码@主机:端口/数据库名?参数）
# 以pymysql驱动为例
db_url = "mysql+pymysql://root:xy666666@localhost:3306/sqlalchemy_demo?charset=utf8mb4"

# 2. 创建Engine（echo=True表示打印执行的SQL语句，方便调试，生产环境可关闭）
engine = create_engine(db_url, echo=True)



# 1. 创建Base基类（所有模型类必须继承此类）
Base = declarative_base()


class User(Base):
    # 定义表名（如果不指定，默认用类名小写作为表名）
    __tablename__ = "user"

    # 定义字段：id（主键，自增）
    id = Column(Integer, primary_key=True, autoincrement=True, comment="用户ID")
    # 定义字段：username（用户名，非空，唯一）
    username = Column(String(50), nullable=False, unique=True, comment="用户名")
    # 定义字段：password（密码，非空）
    password = Column(String(100), nullable=False, comment="密码")
    # 定义字段：create_time（创建时间，默认当前时间）
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")

    # 可选：定义__repr__方法，方便打印实例时查看信息
    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, create_time={self.create_time})"
# Base.metadata.create_all(engine)

# 3. 创建Session工厂（绑定Engine）
SessionFactory = sessionmaker(bind=engine)
# # 4. 创建Base基类（所有模型类必须继承此类）
# Base = declarative_base()
# session=SessionFactory()
#
# # 3. 创建User实例（相当于创建一条数据）
# user = User(username="zhangsan", password="123456")
# # 4. 将实例添加到Session（相当于“暂存”数据，未提交到数据库）
# # session.add(user)
# # 5. 提交事务（将暂存的数据提交到数据库，此时才会真正插入数据）
# # session.commit()
#
# users = session.query(User).all()
# for i in users:
#     print(i)
#
# # 6. 执行结束关闭会话
# session.close()

with SessionFactory() as session:
    user_all = session.query(User).all()
    print(user_all)
    print(type(user_all).__name__)
    for user in user_all:
        print(user)




# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     # def __str__(self):
#     #     return self.name+","+str(self.age)
#
#     def __repr__(self):
#         return self.name + "->" + str(self.age)
#
#
#
# user1=User("zhangsan",19)
# # 打印一个对象，就是在调用这个对象的 __str__ 方法，假如没有，就调用这个类的__repr__ 方法
# print(user1)