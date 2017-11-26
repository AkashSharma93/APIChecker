# Storing the different statuses as constants here.
OK = "OK"
FAILED = "FAILED"

# Simple object to encapsulate the status.
class APIStatus():
	def __init__(self, api_status, temp_status, status_count):
		self._api_status = api_status
		self._temp_status = temp_status
		self._status_count = status_count

	def get_api_status(self):
		return self._api_status

	def set_api_status(self, api_status):
		self._api_status = api_status;

	def get_temp_status(self):
		return self._temp_status

	def set_temp_status(self, temp_status):
		self._temp_status = temp_status

	def get_status_count(self):
		return self._status_count

	def set_status_count(self, status_count):
		self._status_count = status_count