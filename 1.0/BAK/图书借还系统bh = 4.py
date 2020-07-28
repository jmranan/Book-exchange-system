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
ver = "1.0"
now_date = datetime.datetime.now().date()
database_code = """
drop database bes;
create database bes;
use bes;
create table BorrowBooksList(id int auto_increment primary key not null,a_education_id int(200) not null,b_education_id int(200) not null,a_borrowbook_one varchar(200),a_borrowbook_two varchar(200),a_borrowbook_three varchar(200),b_borrowbook_one varchar(200),b_borrowbook_two varchar(200),b_borrowbook_three varchar(200),a_PhoneNumber bigint(20) not null,b_PhoneNumber bigint(20) not null,create_date date not null,ok_date date not null)character set utf8;
create table uesrs(uesr_id int auto_increment primary key not null,uesr_education_id int(200) not null,uesr_password_md5 varchar(100) not null,uesr_create_date date not null);
create table NBorrowBooksList(id int auto_increment primary key not null,education_id int(200) not null,borrowbook_one varchar(200),borrowbook_two varchar(200),borrowbook_three varchar(200),PhoneNumber bigint(20) not null,create_date date not null)character set utf8;
create table errors(error_id int auto_increment primary key not null,error_information varchar(200) not null);
create table notice(notice_id int auto_increment primary key not null,notice varchar(200),notice_create_datetime varchar(200),notice_ver varchar(200))character set utf8;

"""
def hashmd5(stra):
    hasht = hashlib.md5()
    hasht.update(stra.encode("utf-8"))
    return hasht.hexdigest()
if len(sys.argv) == 2:
    if sys.argv[1] == "-c" or sys.argv[1] == "/c":
        os.system("cls")
        print("正在查询图书借还系统的数据库信息...")
        time.sleep(1)
        print(f"数据库ip:{host}")
        print(f"数据库用户名:{uesr}")
        if len(sys.argv) >= 3:
            if sys.argv[2] == "-p" or sys.argv[1] == "/p" and hashmd5(sys.argv[3]) == "0db07d05a7845afccd85f42a8c8c153b":   #jiangmuran
                print(f"数据库密码:{password}")
            else:
                print("数据库密码:******")
        else:
            print("数据库密码:******")
        print(f"数据库姓名:{db}")
        os.system("pause")
        quit()
    elif sys.argv[1] == "/?" or sys.argv[1] == "-?":
        pass
    elif sys.argv[1] == "-ver" or sys.argv[1] == "/ver":
        print(f"图书借还系统的当前版本:{ver}")
        os.system("pause")
        quit()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-?" or sys.argv[1] == "/?" and sys.argv[2] == "database":
        print("-e [host] [uesr] [password] [database] [Usingpassword]")
        print(database_code)
        quit()



elif len(sys.argv) == 7:
    if sys.argv[1] == "-e" or sys.argv[1] == "/e":
        del host,uesr,password,db,UsingPassword
        host = sys.argv[2]
        uesr = sys.argv[3]
        password = sys.argv[4]
        db = sys.argv[5]
        if sys.argv[6] == "True":
            UsingPassword = True
        else:
            UsingPassword = False


def log_in(uesr_education_id,uesr_apssword):
    okseid = []
    rokeid = mysqlp(host=host, uesr=uesr, password=password, db=db, exe="""select * from uesrs;""")
    for i in rokeid:
        okseid.append(i['uesr_education_id'])
def DisplayProgramInformation():
    print("此为jmr制作,我的邮箱:3391966290@qq.com")
    # print(f"当前版本:{ver}")
    print("如果你需要注册一个特殊数字账号（如100100），请联系3391966290@qq.com（需额外付费）")

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
            7.查看通知
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
                    pn = int(input("请输入您的联系电话:"))
                    if not len(str(pn)) == 11 or not len(str(pn)) == 6:
                        print("电话号码不合法，正在从新启动程序...")
                        time.sleep(2)
                        continue
                    print("正在放书至未交换书架...")
                    time.sleep(1)
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
                    print("-------------------已经到底了！-------------------------")
                    os.system("pause")
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
        elif no == "7":
            ok = []
            exe = """select * from notice where notice_ver="1.0" or notice_ver="all" """
            callback = mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe)
            print()
            for i in callback:
                y = f"""通知信息： {i["notice"]}         通知时间： {i["notice_create_datetime"]}        """
                print("-" * len(y))
                print(y)
            print("-----------------------------亲，已经到底了！--------------------------------------")
            os.system("pause")
            print("正在从新启动程序...")
            time.sleep(2)
            continue


        else:
            print("序号无效，正在从新启动程序...")
            time.sleep(2)
            continue

    except:
        print("出现错误，正在从新启动程序...(如果窗口突然消失，说明无法连接服务器/服务器出现错误)")
        time.sleep(2)
        error = str(sys.exc_info()[0]) + "." + str(sys.exc_info()[1]) + "." + str(sys.exc_info()[2])
        mysqlp(host=host, uesr=uesr, password=password, db=db,
               exe=f"""insert into errors (error_information) values ("{error}");""", UPs=UsingPassword)
        time.sleep(1)
        continue

