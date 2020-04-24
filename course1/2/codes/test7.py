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




#插入多表操作
def insertMany(cname,sname,coursenames=[]):
    #创建连接池对象
    from sqlalchemy.orm import sessionmaker
    connpool = sessionmaker()

    #获取连接
    conn = connpool()

    #1.插入班级表数据
    clsList = conn.query(Clazz.cno).filter(Clazz.cname==cname).all()

    if clsList:
        cno = clsList[0].cno
    else:
        cls = Clazz(cname=cname)
        conn.add(cls)
        conn.commit()
        conn.refresh(cls)
        cno = cls.cno



    #2.插入学生表数据
    stuList = conn.query(Student.sno).filter(Student.sname == sname).all()

    if stuList:
        sno = stuList[0].sno
    else:
        stu = Student(sname=sname,cno=cno)
        conn.add(stu)
        conn.commit()
        conn.refresh(stu)
        sno = stu.sno



    #3.插入课程表数据
    courseid_list = []
    for cn in coursenames:
        courseList = conn.query(Course.courseid).filter(Course.coursename==cn).all()

        if courseList:
            courseid_list.append(courseid_list[0].courseid)
        else:
            course = Course(coursename=cn)
            conn.add(course)
            conn.commit()
            conn.refresh(course)
            courseid_list.append(course.courseid)



    #4.插入中间表数据
    for cid in courseid_list:
        sc = SC(sno=sno,courseid=cid)
        conn.add(sc)
        conn.commit()
        conn.refresh(sc)



    #断开连接
    conn.close()


insertMany('Python207','zhangsan',['Python','HTML5'])
