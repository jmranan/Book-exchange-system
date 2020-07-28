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
password = "88888888anan"
db = "besanan"
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
def temp_log_in(all_uesrs_id,all_password_md5,uesr_education_id_input):
        for a,b in enumerate(all_uesrs_id):
            if b == uesr_education_id_input:
                return all_password_md5[a]
def log_in(id,passwordu):
    print("正在登录...")
    exe = """select * from uesrs;"""
    uesrs = mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)
    all_uesrs_id = []
    all_password_md5 = []
    for i in uesrs:
        all_uesrs_id.append(i['uesr_education_id'])
        all_password_md5.append(i['uesr_password_md5'])
    uesr_education_id_input = int(input("请输入你的教育id:"))
    if uesr_education_id_input in all_uesrs_id:
        uesr_password_input = input("请输入密码:")
        if temp_log_in(all_uesrs_id,all_password_md5,uesr_education_id_input) == uesr_password_input:
            for p in range(QUOB(uesr_education_id_input)):
                print(p)
    else:
        print("找不到这个教育id,正在从新启动程序...")
        time.sleep(2)


###########################################################################################
def temp_log_in(all_uesrs_id, all_password_md5, uesr_education_id_input):
    for a, b in enumerate(all_uesrs_id):
        if a == uesr_education_id_input:
            return all_password_md5[b]
while True:
    print("正在登录...")
    exe = """select * from uesrs;"""
    uesrs = mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)
    all_uesrs_id = []
    all_password_md5 = []
    for i in uesrs:
        all_uesrs_id.append(i['uesr_education_id'])
        all_password_md5.append(i['uesr_password_md5'])
    uesr_education_id_input = int(input("请输入你的教育id:"))
    if uesr_education_id_input in all_uesrs_id:
        uesr_password_input = input("请输入密码:")
        os.system("cls")
        if temp_log_in(all_uesrs_id,all_password_md5,uesr_education_id_input) == hashmd5(uesr_password_input):
            print("ok")
        else:
            print("密码错误，正在从新启动程序...（如果忘记密码，请联系3391966290@qq.com)")
            time.sleep(2)
            continue
    else:
        print("找不到这个教育id,正在从新启动程序...")
        time.sleep(2)
        continue