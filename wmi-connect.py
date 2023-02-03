import paramiko

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
try:
    p.connect("192.168.102.35", port=22, username="avocado", password="Avocado@2020")
except Exception as e:
    print(e)
stdin, stdout, stderr = p.exec_command("who am i")
stdout.channel.set_combine_stderr(True)
output = stdout.readlines()
print(output)
print(stderr.readlines())

#print(stdout.read())
#print(stderr.read())
#print(stdin.read())
# opt = "".join(opt)
# print(opt)