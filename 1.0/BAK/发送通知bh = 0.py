###################improt######################
import hashlib
import pymysql
import datetime
import time
import os
import sys


####################def#########################

host = "127.0.0.1"
uesr = "pycall"
password = "anan"
db = "bes"
UsingPassword = True
now_date_time = datetime.datetime.now()
def log_in(uesr_education_id,uesr_apssword):
    okseid = []
    rokeid = mysqlp(host=host, uesr=uesr, password=password, db=db, exe="""select * from uesrs;""")
    for i in rokeid:
        okseid.append(i['uesr_education_id'])
def DisplayProgramInformation():
    print("此为jmr制作,我的邮箱:3391966290@qq.com")
    print("如果你需要注册一个特殊数字账号（如100100），请联系3391966290@qq.com（需额外付费）")


def mysqlp(host, uesr, password, db, exe,UPs=True):
    if UPs:
        db = pymysql.connect(host=host,
                             user=uesr,
                             password=password,
                             db=db,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    else:
        db = pymysql.connect(host=host,
                             user=uesr,
                             db=db,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    db.set_charset('utf8mb4')
    cursor.execute(exe)
    db.commit()
    data = cursor.fetchall()
    return data
    db.close()

    mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)


#######################main####################################
try:
    notice = input("请输入您要发送的通知:")
    ver = input("请输入您要发送给那个版本的用户（如1.0，全部填all):")
    print("开始发送")
    mysqlp(host=host,uesr=uesr,password=password,db=db,exe=f"""insert into notice(notice,notice_create_datetime,notice_ver) values("{notice}","{now_date_time}","{ver}");""",UPs=UsingPassword)
    print("发送成功")
    os.system("pause")
except:
    print("出现错误")
    print(sys.exc_info())
    os.system("pause")










