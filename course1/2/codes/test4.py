#coding=utf-8


from sqlalchemy.engine import create_engine
#1.创建engine对象
conn_url = 'mysql://root:123456@127.0.0.1:3306/tornaod20180830?charset=utf8'
engine = create_engine(conn_url,encoding='utf-8',echo=True)

#2.创建ORM基类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)


#3.引入列和字段类型
from sqlalchemy import Column
from sqlalchemy.types import Integer,String,Date,DateTime,Float,Text


#4.自定义类创建数据库表

class User(Base):
    __tablename__='t_cuser'

    userid = Column(Integer,primary_key=True,autoincrement=True)
    uname = Column(String(length=20))
    birth = Column(Date)


class Address(Base):
    __tablename__='t_address'

    aid = Column(Integer,primary_key=True,autoincrement=True)
    aname = Column(Text)


from sqlalchemy.orm import sessionmaker
import datetime

def insertUser(uname):
    #创建连接池
    connpool = sessionmaker(bind=engine)

    #获取一个连接
    conn = connpool()

    #创建User对象
    user = User(uname=uname,birth=datetime.datetime.today())

    #插入到t_cuser表中
    conn.add(user)

    #提交事务
    conn.commit()

    #刷新
    conn.refresh(user)

    #断开连接（将连接放回连接池）
    conn.close()

    return user


# insertUser('zhangsan')



def insertMany(users=[]):
    #创建连接池
    connpool = sessionmaker(bind=engine)
    #获取连接
    conn = connpool()
    #一次插入多条记录
    conn.add_all(users)
    #提交事务
    conn.commit()
    #刷新
    [conn.refresh(u) for u in users]
    #断开连接
    conn.close()

    return users

# user1 = User(uname='lisi',birth=datetime.datetime.today())
# user2 = User(uname='wangwu',birth=datetime.datetime.today())
#
#
# userList = [user1,user2]
#
# insertMany(userList)




user3 = User(uname='zhangjie',birth=datetime.datetime.today())
addr = Address(aname='beijingshi')
uaList = [user3,addr]
insertMany(uaList)