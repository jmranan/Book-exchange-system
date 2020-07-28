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
now_date = datetime.datetime.now().date()
def log_in(uesr_education_id,uesr_apssword):
    okseid = []
    rokeid = mysqlp(host=host, uesr=uesr, password=password, db=db, exe="""select * from uesrs;""")
    for i in rokeid:
        okseid.append(i['uesr_education_id'])
def DisplayProgramInformation():
    print("此为jmr制作,我的邮箱:3391966290@qq.com")
    print("如果你需要注册一个特殊数字账号（如100100），请运行万能账号生成器（需额外付费）")

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

def temp_1(all_uesrs_id, all_password_md5, uesr_education_id_input):
    for a, b in enumerate(all_uesrs_id):
        if b == uesr_education_id_input:
            return all_password_md5[a]
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
            6.登录测试
        ********************
        """)
        no = input("请输入序号:")
        if no == "1":
            print("暂未开放，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "2":
            print("正在登录...")
            exe = """select * from uesrs;"""
            uesrs = mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe, UPs=UsingPassword)
            all_uesrs_id = []
            all_password_md5 = []
            for i in uesrs:
                all_uesrs_id.append(i['uesr_education_id'])
                all_password_md5.append(i['uesr_password_md5'])
            uesr_education_id_input = int(input("请输入你的教育id:"))
            if uesr_education_id_input in all_uesrs_id:
                uesr_password_input = input("请输入密码:")
                os.system("cls")
                if temp_1(all_uesrs_id, all_password_md5, uesr_education_id_input) == hashmd5(uesr_password_input):
                    br1 = input("请输入您要放的第一本书:")
                    br2 = input("请输入您要放的第二本书:")
                    br3 = input("请输入您要放的第三本书:")
                    pn = input("请输入您的联系电话:")
                    print("正在放书至未交换书架...")
                    exe = f"""insert into nborrowbookslist(education_id,borrowbook_one,borrowbook_two, borrowbook_three, PhoneNumber, create_date) values ({uesr_education_id_input},"{br1}","{br2}","{br3}",{pn},date("{now_date}"));
                    """
                    mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe)

                    print("放书成功，正在从新启动程序...")
                    time.sleep(2)
                    continue
                else:
                    print("密码错误，正在从新启动程序...（如果忘记密码，请联系3391966290@qq.com)")
                    time.sleep(2)
                    continue
            else:
                print("找不到这个教育id,正在从新启动程序...")
                time.sleep(2)
                continue
        elif no == "3":
            education_id = int(input("请输入您的教育id:"))
            ypassword = input("请输入您要设定的密码:")
            os.system("cls")
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
            exe = f"""
            insert into uesrs(uesr_education_id,uesr_password_md5,uesr_create_date) values ({education_id},"{uesr_password_md5}",date("{now_date}"));
            """
            mysqlp(host=host,uesr=uesr,password=password,db=db,exe=exe,UPs=UsingPassword)
            print("账号注册成功，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "4":
            print("正在登录...")
            exe = """select * from uesrs;"""
            uesrs = mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe, UPs=UsingPassword)
            all_uesrs_id = []
            all_password_md5 = []
            for i in uesrs:
                all_uesrs_id.append(i['uesr_education_id'])
                all_password_md5.append(i['uesr_password_md5'])
            uesr_education_id_input = int(input("请输入你的教育id:"))
            if uesr_education_id_input in all_uesrs_id:
                uesr_password_input = input("请输入密码:")
                os.system("cls")
                if temp_1(all_uesrs_id, all_password_md5, uesr_education_id_input) == hashmd5(uesr_password_input):
                    for rd in QUOB(uesr_education_id_input):
                        if rd["ok_date"].year >= now_date.year:
                            mysqlp(host=host, uesr=uesr, password=password, db=db,
                                   exe=f"""delete from borrowbookslist where id={rd["id"]}""", UPS=UsingPassword)
                        elif rd["ok_date"].month >= now_date.month:
                            mysqlp(host=host, uesr=uesr, password=password, db=db,
                                   exe=f"""delete from borrowbookslist where id={rd["id"]}""", UPS=UsingPassword)
                        elif rd["ok_date"].day >= now_date.day:
                            mysqlp(host=host, uesr=uesr, password=password, db=db,
                                   exe=f"""delete from borrowbookslist where id={rd["id"]}""", UPS=UsingPassword)

                    for p in QUOB(uesr_education_id_input):
                        print(p)
                    print("--------------------------------------------")
                    print("查询成功，正在从新启动程序...")
                    time.sleep(2)
                    continue

                else:
                    print("密码错误，正在从新启动程序...（如果忘记密码，请联系3391966290@qq.com)")
                    time.sleep(2)
                    continue
            else:
                print("找不到这个教育id,正在从新启动程序...")
                time.sleep(2)
                continue
        elif no == "5":
            os.system("cls")
            print("清除屏幕成功，正在从新启动程序...")
            time.sleep(2)
            continue
        elif no == "6":
            print("正在登录...")
            exe = """select * from uesrs;"""
            uesrs = mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe, UPs=UsingPassword)
            all_uesrs_id = []
            all_password_md5 = []
            for i in uesrs:
                all_uesrs_id.append(i['uesr_education_id'])
                all_password_md5.append(i['uesr_password_md5'])
            uesr_education_id_input = int(input("请输入你的教育id:"))
            if uesr_education_id_input in all_uesrs_id:
                uesr_password_input = input("请输入密码:")
                os.system("cls")
                if temp_1(all_uesrs_id, all_password_md5, uesr_education_id_input) == hashmd5(uesr_password_input):
                    print("登录成功，正在从新启动程序...")
                    time.sleep(2)
                    continue
                else:
                    print("密码错误，正在从新启动程序...（如果忘记密码，请联系3391966290@qq.com)")
                    time.sleep(2)
                    continue
            else:
                print("找不到这个教育id,正在从新启动程序...")
                time.sleep(2)
                continue
        else:
            print("序号无效，正在从新启动程序...")
            time.sleep(2)
            continue
    except:
        print("出现错误，正在从新启动程序...(如果窗口突然消失，说明无法连接服务器/服务器出现错误)")
        time.sleep(1)
        error = str(sys.exc_info()[0]) + "." + str(sys.exc_info()[1]) + "." + str(sys.exc_info()[2])
        mysqlp(host=host, uesr=uesr, password=password, db=db,
               exe=f"""insert into errors (error_information) values ("{error}");""", UPs=UsingPassword)
        time.sleep(1)
        continue

