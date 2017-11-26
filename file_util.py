import pickle
import api_status

# Serialize the status object in a pickle file.
def set_status(api_status):
	with open("api_status.pickle", "wb") as status_file:
		pickle.dump(api_status, status_file)

# Deserialize the status object from the pickle file and return it.
# In case there is no file, create a new status object with status as FAILED.
def get_status():
	try:
	 with open("api_status.pickle", "rb") as status_file:
		 return pickle.load(status_file)
	except:
		return api_status.APIStatus(api_status.FAILED, api_status.FAILED, 0)