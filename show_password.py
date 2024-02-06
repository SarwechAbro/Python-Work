import subprocess
import time
import sys
arguments = []
for arg in sys.argv[1:]:
    arguments.append(arg)
profile_name = ' '.join(arguments)
command = (f'netsh wlan show profile name="{profile_name}" key=clear')
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, _ = process.communicate()

for char in output.decode():
    print(char, end='', flush=True)
    time.sleep(0.004)  