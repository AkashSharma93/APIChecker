import time
import os

poll_interval = 10

while True:
	# os.system, as we may choose to replace this file with crontab or something in the future.
	os.system("python api_checker.py")
	time.sleep(10)