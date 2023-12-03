import subprocess
import time


comman = "systeminfo"
command = "netsh wlan show profile Sarang  key=clear"
commands = [command,comman]
colors = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6']
for cmd in commands:
     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
     output, _ = process.communicate()
     color = colors.pop(0) 
     subprocess.run('color ' + color, shell=True)
     colors.append(color)

     for char in output.decode():
        print(char, end='', flush=True)
        time.sleep(0.009)  
