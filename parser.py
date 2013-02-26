#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import logging
import datetime


logging.basicConfig(filename="testlog.log", 
                    format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info('\n'*3 + ' '*5 + '*'*50)
logging.info('-'*50)
logging.info(datetime.datetime.now())
logging.info('-'*50)
logging.info("---Start logging---")

timestamp = int(time.time())
server_number = ''
arg1_fixed = ''
filename = ''

# # The script arguments:
# # Script name
# arg0 = " "
# # Path variable
# arg1 = "/Volumes/01_test_project/2013.02.25/rw/eee/XDCAM 20121009_141429_NOVY4644.mov"
# # Id variable
# arg2 = "449"
# # Stream info
# arg3 = "MPEG IMX 625/50 (50 Mb/s) (1049x576 25.0fps])"
# # Action variable
# arg4 = "Make General Proxy"

args = sys.argv
arg1 = args[1]
arg2 = args[2]
arg3 = args[3]
arg4 = args[4]

# args = [arg0, arg1, arg2, arg3, arg4]


def replace_name(arg):
	global arg1_fixed
	arg1_fixed = "/mnt/nc-prod-" + server_number \
					+ arg[arg.find(server_number)-1:]
	

def get_params(arg):
	global server_number
	global filename
	server_number = arg.split('/')[2][:2]
	filename = arg.split('/')[-1]


def main():
	if len(args)==5:
		logging.info('RECEIVED ARGUMENTS:\n\
		path:\t\t%s\n\
		id:\t\t%s\n\
		stream:\t\t%s\n\
		action:\t\t%s' 
		% (arg1, arg2, arg3, arg4))
		
		if arg3.find('fps') != -1:

			get_params(arg1)
			replace_name(arg1)
			
			logging.info('\
		timestamp:\t%s\n\
		server_number:\t%s\n\
		fixed path:\t%s\n\
		filename:\t%s' 
			% (str(timestamp), server_number, 
				arg1_fixed, filename))
		else:
			logging.error("No field 'fps' in argument 3. Seems like this file isn't video file")
	else:
		logging.error("The number of arguments isn't proper")




if __name__ == '__main__':
	main()
logging.info("---End logging at %s---\n" %datetime.datetime.now())
logging.info('*'*50)