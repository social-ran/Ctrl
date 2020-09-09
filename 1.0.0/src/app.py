import asyncio
import os
from walkoff_app_sdk.app_base import AppBase

class Ctrler(AppBase):
    __version__ = "1.0.0"
    app_name = "ctrler"  # this needs to match "name" in api.yaml
    def __init__(self, redis, logger, console_logger=None):
        super().__init__(redis, logger, console_logger)

    async def contrl(self,cmd, ip,servetype, frequency , start_time="2018-08-11 13:41:11", end_time="2018-08-11 13:41:41",
                        log_path="/var/log/appsimulation/traffic_gen.log" ,vpntype='no' , vpnserveip='no', vpnipaddr='no',):
        if cmd!='start' and cmd != 'stop':
            return "cmd error!!"
        serveset=['arpServer','arpClient','dnsServer','dnsClient','ftpServer','ftpClient', 'httpServer','httpClient','ircServer','ircClient','mailServer','mailClient','ntpServer','ntpClient','rtpServer','rtpClient','sshServer','sshClient','telnetServer','telnetClient','tftpServer','tftpClient']
        if servetype not in serveset:
            return "serveType error!!"
        if frequency<1 or frequency>100000:
            return  "frequency error!!"

        fp = open('post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('receiver')#####!!!!!
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"FREQUENCY":"')
        fp.write(str(frequency))#1-100000
        if vpntype!='no':
            fp.write('",\n"VPNTYPE":"')
            fp.write(vpntype)
            fp.write('",\n"VPNSERVERIP":"')
            fp.write(vpnserveip)
            fp.write('",\n"VPNIPADDR":"')
            fp.write(vpnipaddr)
        fp.write('\n}\n}\n')
        os.system('sshpass -p 123456 scp post_info.json 10.245.142.21:/home/config')
        os.system('rm -r post_info.json')
        return "ctrler OK!!"


if __name__ == "__main__":
    asyncio.run(Ctrler.run(), debug=True)
