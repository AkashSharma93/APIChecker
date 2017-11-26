import requests
import file_util
import api_status
import mail_util
import traceback

url = "http://google.com"
timeout_in_sec = 5

def check_api():
	try:
		response = requests.get(url, timeout=timeout_in_sec)
		response_status = response.ok
	except:
		response_status = False

	status = file_util.get_status()
	old_status = status.get_api_status()
	if response_status:
		if status.get_temp_status() == api_status.OK:
			status.set_status_count(status.get_status_count() + 1)
			if status.get_status_count() >= 2: # This may lead to Status transition.
				status.set_api_status(api_status.OK)
		else:	# Temp status has changed.
			status.set_temp_status(api_status.OK)
			status.set_status_count(1)

	else:
		if status.get_temp_status() == api_status.FAILED:
			status.set_status_count(status.get_status_count() + 1)
			if (status.get_status_count() >= 3):	# This may lead to Status transition.
				status.set_api_status(api_status.FAILED)
		else:	# Temp status has changed.
			status.set_temp_status(api_status.FAILED)
			status.set_status_count(1)

	file_util.set_status(status)
	if status.get_api_status() != old_status:	# Status has transitioned.
		mail_util.send_mail(status)

if __name__ == '__main__':
	check_api()