import paramiko
from getpass import getpass
host = '127.0.0.1'
user = 'phil'
port = 22
password = 'pythoncode'

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    # WarningPolicy, AutoAddPolicy, RejectPolicy
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        '192.168.40.38',
        username='nikhil.dahake',
        password= getpass('Enter pass:')
    )
    stdin, stdout, stderr = client.exec_command('ls')
except Exception as err:
    print(f'Error is : {err}')




