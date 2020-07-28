import hashlib
import pymysql
import datetime
import time
import os
import random
import sys



host = "127.0.0.1"
uesr = "pycall"
password = "88888888anan"
db = "besanan"
UsingPassword = True
now_date = datetime.datetime.now().date()

def WeChat_payment(money):
    pass


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
def hashmd5(stra):
    hasht = hashlib.md5()
    hasht.update(stra.encode("utf-8"))
    return hasht.hexdigest()




while True:
    try:
        print("最多注册7位数字账号")
        education_id = int(input("请输入您要设定的账号id:"))
        ypassword = input("请输入您要设定的密码:")
        os.system("cls")
        okeid = []
        rokeid = mysqlp(host=host, uesr=uesr, password=password, db=db, exe="""select uesr_education_id from uesrs;""")
        for i in rokeid:
            okeid.append(i['uesr_education_id'])
        if len(str(education_id)) >= 8:
            print("账号id超出限制！，正在关闭程序...")
            time.sleep(2)
            quit()
        if education_id in okeid:
            print("账号id以经被注册过了！，正在关闭程序...")
            time.sleep(2)
            quit()
        md = random.randint(0,20)
        if md == 3:
            print("恭喜你获得随机免单机会!")
        else:
            input(f"您确定要注册账号吗，总计{(140 - (len(str(18)) * 15) * 2) + 0.24 + 10}元(回车支付并开始注册,Ctrl+C取消并结束程序)")
            WeChat_payment((140 - (len(str(18)) * 15) * 2) + 0.24 + 10)
        print("账号正在注册中，请稍等...")
        time.sleep(1)
        uesr_password_md5 = hashmd5(ypassword)
        exe = f"""
        insert into uesrs(uesr_education_id,uesr_password_md5,uesr_create_date) values ({education_id},"{uesr_password_md5}",date("{now_date}"));
        """
        mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)
        print("账号注册成功，正在关闭程序...")
        time.sleep(2)
        quit()
    except:
        print("出现错误，正在从新启动程序...(如果窗口突然消失，说明无法连接服务器/服务器出现错误)")
        time.sleep(1)
        error = str(sys.exc_info()[0]) + "." + str(sys.exc_info()[1]) + "." + str(sys.exc_info()[2])
        mysqlp(host=host, uesr=uesr, password=password, db=db,
               exe=f"""insert into errors (error_information) values ("{error}");""", UPs=UsingPassword)
        time.sleep(1)
        continue
