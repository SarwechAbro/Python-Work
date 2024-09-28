import subprocess
import time


while True:
	command = input('Enter Your command: ')
	if command != 'exit':
		process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		output, _ = process.communicate()

	for char in output.decode():
		print(char, end='', flush=True)
		time.sleep(0.004)  
	else:
		exit = "Good bye from Sarwech's terminal if do you want to run again type python command.py in terminal window thank you."
	for char in exit:
		print(char, end='', flush=True)
		time.sleep(0.009) 
	break