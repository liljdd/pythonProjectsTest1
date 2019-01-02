import sys,paramiko,time,pymysql,os,shutil
msg='日期格式：yyyymmdd\n起始时间格式：hh:mm\n均为必填'
print(msg)
date=input('日期格式（yyyymmdd）： ')
b_time=input('开始时间(hh:mm)： ')
e_time=input('结束时间(hh:mm)： ')

if not (len(date) == 8 and len(b_time) == len(e_time) == 5):
    print('时间位数有误')
    time.sleep(3)
    sys.exit(1)


def ssh_server(hostIP,Port,Username,Password,date,b_time,e_time):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostIP, port=Port, username=Username, password=Password)
    except:
        print(hostIP+'无法连接')
        time.sleep(3)
        sys.exit()
    else:
        cmd='''sh /root/lxq/cut_log_time_deploy.sh %s %s %s''' %(date,b_time,e_time)
        #cmd = '''sh /root/lxq/echo.sh %s %s %s''' % (date, b_time, e_time)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result_stdout = stdout.read()
        result = result_stdout.decode()
        ssh.close()
        print(result)

db=pymysql.connect('192.168.1.16','root','Lxq_204389','server_info',port=3306,charset='utf8')
dbc=db.cursor()
sql='''select IP,PORT,USERNE,PASSWD,otowap_log from info where otowap_log!='' '''
#sql=''' select IP,PORT,USERNE,PASSWD,otowap_log from info where IP='123.57.138.212' '''
dbc.execute(sql)
sql_date=dbc.fetchall()
db.close()
#sql_date=dbc.fetchone()
#server=sql_date
#ssh_server(server[0],server[1],server[2],server[3],date,b_time,e_time)
for server in sql_date:
    ssh_server(server[0],server[1],server[2],server[3],date,b_time,e_time)

if not os.path.exists('otowap_logs'):
    os.mkdir('otowap_logs')
else:
    shutil.rmtree('otowap_logs')
    time.sleep(1)
    os.mkdir('otowap_logs')

def scp_server(hostIP,Port,Username,Password,log_file):
    try:
        scp=paramiko.Transport((hostIP,Port))
        scp.connect(username=Username,password=Password)
        sftp=paramiko.SFTPClient.from_transport(scp)
    except Exception as e:
        print(hostIP+'无法连接')
        time.sleep(5)
    else:
        sftp.get('/time_cut_log/'+log_file,'otowap_logs/'+log_file)
        scp.close()

print('下载中，可能占用时间较长')
for server in sql_date:
    scp_server(server[0],server[1],server[2],server[3],server[4])
    print(server[0]+'下载完毕')

print('日志文件在otowap_log下，请查看，enter退出')