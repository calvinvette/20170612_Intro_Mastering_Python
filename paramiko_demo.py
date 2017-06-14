import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.216.50.73",port=22,username="admin",password="password")

stdin, stdout, stderr = ssh.exec_command("ls -la")
for line in iter(stdout.readline, ''):
    print(line.rstrip())
print(type(stdout))
ssh.close()