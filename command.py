import subprocess
import time


#command = "netsh wlan show profile Sarang  key=clear"
command ="systeminfo"


process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, _ = process.communicate()


for char in output.decode():
    print(char, end='', flush=True)
    time.sleep(0.009)  
