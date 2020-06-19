from check.linux_stat import LinuxStat
from utils.linux_base import LinuxBase


class LinuxStat( LinuxBase ):
    def __init__(self, params, conn):
        super().__init__( params )
        self.params = params
        self.conn = conn

    def get_appurl(self):
        command = 'find -name'
        res = super().exec_command( command, self.conn )
        res = res.readlines()
        app_url = {}
        for line in res:
            if line.startswith( 'tomcat' ):
                app_url = line.split()[1]

        return {
            'app_url': app_url
        }


if __name__ == '__main__':
    linux_params = {
        'hostname': '114.116.16.6',
        'port': 22,
        'username': 'root',
        'password': 'tecent.test'
    }
    linux_conn, _ = LinuxBase( linux_params ).connection()

    linuxstat = LinuxStat( linux_params, linux_conn )

    print( linuxstat.get_appurl() )
