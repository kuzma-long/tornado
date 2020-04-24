#coding=utf-8


import torndb


def insertUser(uname,pwd):
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')
    #执行插入操作
    rowid = conn.insert('insert into t_auser values(null,"%s","%s",now())'%(uname,pwd))

    print rowid

    #断开连接
    conn.close()

# insertUser('lisi','123')



def insertMany(args=[]):
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'insert into t_auser values(null,%s,%s,now())'

    #执行插入操作
    rowid = conn.insertmany(sql,args)

    print rowid

    #断开连接
    conn.close()


# insertMany([('zhangjie','123'),('xiena','123')])



def queryAll():
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'select * from t_auser'

    #执行插入操作
    rowList = conn.query(sql)

    print rowList

    #断开连接
    conn.close()


# queryAll()



def queryUser(uname,pwd):
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'select * from t_auser where uname="%s" and pwd="%s"'%(uname,pwd)

    #执行插入操作
    rowList = conn.query(sql)

    print rowList

    #断开连接
    conn.close()



# queryUser('zhangsan','123')


def likeQuery(key):
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'select * from t_auser where uname like "%%{uname}%%"'.format(uname=key)

    print sql

    #执行插入操作
    rowList = conn.query(sql)

    print rowList

    #断开连接
    conn.close()


# likeQuery('n')


def order_by_userid(param):
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    #排序方式变量
    rule = 'ASC'
    columnname = param

    if param.startswith('-'):
        rule = 'DESC'
        columnname = param[1:]



    sql = 'select * from t_auser order by %s %s'%(columnname,rule)

    print sql

    # 执行插入操作
    rowList = conn.query(sql)

    print rowList

    # 断开连接
    conn.close()


# order_by_userid('-userid')
# order_by_userid('userid')



def page_user(num,size=2):
    # 建立数据库的连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'select * from t_auser limit %s,%s'%(((num-1)*size),size)

    rowList = conn.query(sql)


    print rowList


    #断开连接
    conn.close()


# page_user(2)



#更新操作
def updateUser(uname):
    #建立连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'update t_auser set uname="%s" where userid=1'%uname

    rowcount = conn.update(sql)

    print rowcount

    conn.close()

# updateUser('zhangsan123')


def deleteUser(uname):
    # 建立连接
    conn = torndb.Connection(host='127.0.0.1', database='tornaod20180830', user='root', password='123456')

    sql = 'delete from t_auser where uname="%s"'%uname

    rowid = conn.execute(sql)

    print rowid

    conn.close()


# deleteUser('zhangsan123')