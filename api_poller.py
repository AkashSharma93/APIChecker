import time
import os

poll_interval = 10

while True:
	os.system("python api_checker.py")
	time.sleep(10)