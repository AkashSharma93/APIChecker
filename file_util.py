import pickle
import api_status

def set_status(api_status):
	with open("api_status.pickle", "wb") as status_file:
		pickle.dump(api_status, status_file)

def get_status():
	try:
	 with open("api_status.pickle", "rb") as status_file:
		 return pickle.load(status_file)
	except:
		return api_status.APIStatus(api_status.FAILED, api_status.FAILED, 0)