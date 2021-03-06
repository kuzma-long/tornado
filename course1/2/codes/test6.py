#coding=utf-8


from sqlalchemy.engine import create_engine
#1.创建engine对象
conn_url = 'mysql://root:123456@127.0.0.1:3306/tornaod20180830?charset=utf8'
engine = create_engine(conn_url,encoding='utf-8',echo=True)

#2.创建ORM基类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)


#3.引入列和字段类型
from sqlalchemy import Column,ForeignKey
from sqlalchemy.types import Integer,String,Date,DateTime,Float,Text


#4.自定义类创建数据库表
class Clazz(Base):
    __tablename__='t_cls'

    cno = Column(Integer,primary_key=True,autoincrement=True)
    cname = Column(String(length=30),unique=True)


class Student(Base):
    __tablename__='t_student'

    sno = Column(Integer,primary_key=True,autoincrement=True)
    sname = Column(String(length=30),unique=True)
    cno = Column(Integer,ForeignKey(Clazz.cno,ondelete='CASCADE',onupdate='CASCADE'))

    def __repr__(self):
        return u'<Student:%s>'%self.sname


class Course(Base):
    __tablename__ = 't_course'

    courseid = Column(Integer, primary_key=True, autoincrement=True)
    coursename = Column(String(length=30), unique=True)



class SC(Base):
    __tablename__ = 't_sc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sno = Column(Integer,ForeignKey(Student.sno,onupdate='CASCADE',ondelete='CASCADE'))
    courseid = Column(Integer,ForeignKey(Course.courseid,onupdate='CASCADE',ondelete='CASCADE'))




Base.metadata.create_all()