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
def log_in(uesr_education_id,uesr_apssword):
    okseid = []
    rokeid = mysqlp(host=host, uesr=uesr, password=password, db=db, exe="""select * from uesrs;""")
    for i in rokeid:
        okseid.append(i['uesr_education_id'])
def DisplayProgramInformation():
    print("此为jmr制作,我的邮箱:3391966290@qq.com")
    print("只有北京市朝阳区陈经纶中学分校小学部的人才能使用")

def QUOB(uesr_education_id):
    ok = []
    exe = """select * from borrowbookslist;"""
    callback = mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe)
    for i in callback:
        if i["a_education_id"] == uesr_education_id or i["b_education_id"] == uesr_education_id:
            ok.append(i)
    return ok
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
    db.set_charset('utf8mb4')    # 添加此行即可运行
    cursor.execute(exe)
    db.commit()
    data = cursor.fetchall()
    return data
    db.close()

    mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)
def hashmd5(stra):
    hasht = hashlib.md5()
    hasht.update(stra.encode("utf-8"))
    return hasht.hexdigest()


#####################main#######################


os.system("cls")
while True:
    try:
        DisplayProgramInformation()
        print("""
        ********************
            1.借书
            2.放书
            3.注册账号
            4.查询未还借书
            5.清空屏幕
        ********************
        """)
        no = input("请输入序号:")
        if no == "1":
            print("暂未开放，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "2":
            print("暂未开放，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "3":
            education_id = int(input("请输入您的教育id:"))
            ypassword = input("请输入您要设定的密码:")
            print("账号正在注册中，请稍等...")
            okeid = []
            rokeid = mysqlp(host=host, uesr=uesr, password=password, db=db, exe="""select uesr_education_id from uesrs;""")
            for i in rokeid:
                okeid.append(i['uesr_education_id'])
            if len(str(education_id)) != 8:
                print("教育id不合法！，正在从新启动程序...")
                time.sleep(2)
                continue
            if education_id in okeid:
                print("教育id以经被注册过了！，正在从新启动程序...")
                time.sleep(2)
                continue
            uesr_password_md5 = hashmd5(ypassword)
            now_date = datetime.datetime.now().date()
            exe = f"""
            insert into uesrs(uesr_education_id,uesr_password_md5,uesr_create_date) values ({education_id},"{uesr_password_md5}",date("{now_date}"));
            """
            mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)
            print("账号注册成功，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "4":
            print("暂未开放，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "5":
            os.system("cls")
            print("清除屏幕成功，正在从新启动程序...")
            time.sleep(2)
            continue
    except:
        print("出现错误，正在从新启动程序...(如果窗口突然消失，说明无法连接服务器/服务器出现错误)")
        time.sleep(1)
        error = str(sys.exc_info()[0]) + "." + str(sys.exc_info()[1]) + "." + str(sys.exc_info()[2])
        mysqlp(host=host, uesr=uesr, password=password, db=db, exe=f"""insert into errors (error_information) values ("{error}");""", UPs=UsingPassword)
        time.sleep(1)
        continue


