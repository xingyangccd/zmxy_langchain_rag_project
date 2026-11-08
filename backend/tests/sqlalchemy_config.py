from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 1. 定义MySQL连接字符串（格式：数据库驱动://用户名:密码@主机:端口/数据库名?参数）
# 以pymysql驱动为例
db_url = "mysql+pymysql://root:xy666666@localhost:3306/sqlalchemy_demo?charset=utf8mb4"

# 2. 创建Engine（echo=True表示打印执行的SQL语句，方便调试，生产环境可关闭）
engine = create_engine(db_url, echo=True)
# 3. 创建Session工厂（绑定Engine）
SessionFactory = sessionmaker(bind=engine)
# 4. 创建Base基类（所有模型类必须继承此类）
Base = declarative_base()