import os
import subprocess
import psutil

print(os.getpid())
print(os.getcwd())
print(os.getgid())
print(os.getuid())

ret = subprocess.getoutput('python3 request_test.py')
print(ret)
print(ret + ' code')
print('main process')

print(os.uname())
print(os.getloadavg())
print(os.cpu_count())

print(psutil.cpu_percent(percpu=True))