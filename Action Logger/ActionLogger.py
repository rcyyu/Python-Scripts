import os
import sys
from datetime import datetime

print "Welcome to ActionLogger."
text_file = "log.txt"

# primary function, allows user to access other functions
def menu():
	print "Type w to write in log."
	print "Type r to read log."
	print "Type d to wipe log."
	print "Type e to exit."
	command = raw_input()
	if command == 'w':
		write_to_file(text_file)
	elif command == 'r':
		read_from_file(text_file)
		passive_log(3)
	elif command == 'e':
		passive_log(2)
		sys.exit()
	elif command == 'd':
		open(text_file, 'w').close()
		passive_log(4)
		print "Log wiped successfully."
	else:
		print "Invalid command."
	menu()
# allows user to write in text file
def write_to_file(text_file):
	print "Please enter you text:"
	text = raw_input()
	time = datetime.now()
	with open(text_file, "a") as file:
		file.write("[%s]: %s\n" % (time, text))
		file.close()
	print "Text: %s successfully added" % text
# allows user to read contents of text file
def read_from_file(text_file):
	for line in open(text_file, "r").readlines():
		print line
# passively logs the users actions in text file
def passive_log(command):
	accesstime = datetime.now()
	if command == 1:
		log = "[User Access at %s]\n" % accesstime
	elif command == 2:
		log = "[User Stopped Accessing at %s]\n" % accesstime
	elif command == 3:
		log = "[User Read Log at %s]\n" % accesstime
	elif command == 4:
		log = "[Log wiped successfully at %s]\n" % accesstime
	with open(text_file, "a") as file:
		file.write(log)
		file.close()

passive_log(1)
menu()

