###################improt######################
import hashlib
import pymysql
import datetime
import time
import os
import sys
import random


####################def#########################

host = "127.0.0.1"
uesr = "root"
password = "123456"
db = "besanan"
UsingPassword = True
ver = "1.0"
now_date = datetime.datetime.now().date()
database_code = """
drop database besanan;
create database besanan;
use besanan;
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
for ia in range(20):
    x_1 = ""
    x_2 = ""
    x_3 = ""
    x_4 = ""
    x_5 = ""
    re = ["a","A","B","你","暖","哈","123"]
    for i in range(8):
        x_1 = x_1 + str(random.randint(1,9))
    for i in range(10):
        x_2 = x_2 + re[random.randint(0, len(re) - 1)]
        x_3 = x_3 + re[random.randint(0, len(re) - 1)]
        x_4 = x_4 + re[random.randint(0, len(re) - 1)]
    for i in range(11):
        x_5 = x_5 + str(random.randint(1,9))
    x_5 = int(x_5)
    exe = f"""insert into nborrowbookslist(education_id,borrowbook_one,borrowbook_two, borrowbook_three, PhoneNumber, create_date) values (18038030,"{x_2}","{x_3}","{x_4}",{x_5},date("{now_date}"));
    """
    mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe,UPs=UsingPassword)
    print(ia + 1)
for ia in range(int(input())):
    x_1 = ""
    x_2 = ""
    x_3 = ""
    x_4 = ""
    x_5 = ""
    re = ["a","A","B","你","暖","哈","123"]
    for i in range(8):
        x_1 = x_1 + str(random.randint(1,9))
    for i in range(10):
        x_2 = x_2 + re[random.randint(0, len(re) - 1)]
        x_3 = x_3 + re[random.randint(0, len(re) - 1)]
        x_4 = x_4 + re[random.randint(0, len(re) - 1)]
    for i in range(11):
        x_5 = x_5 + str(random.randint(1,9))
    x_5 = int(x_5)
    exe = f"""insert into nborrowbookslist(education_id,borrowbook_one,borrowbook_two, borrowbook_three, PhoneNumber, create_date) values ({x_1},"{x_2}","{x_3}","{x_4}",{x_5},date("{now_date}"));
    """
    mysqlp(host=host, uesr=uesr, password=password, db=db, exe=exe,UPs=UsingPassword)
    print(ia + 1)
