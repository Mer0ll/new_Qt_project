import subprocess
import pprint


def getRP():
    return subprocess.check_output('powershell -Executionpolicy ByPass -Command Get-Process').decode(
        encoding='cp866')


a = getRP()

b = a.strip().split('\r\n')
headers = b[1].split()
for i in b[3:]:
    print(i.split())