# API CHECKER

This utility polls a rest end point to check if the API is working as expected.
In case the status changes from OK to FAILED, or vice versa, an email is sent to the recepient notifying him about the change.

**HOW TO RUN**: Export your gmail id and password to the environment variables `smtp_login` and `smtp_password`. Now, execute `api_poller`.

The various files do the following things:

**api_checker**: This is the main file. It is responsible for making a get call to the API. Based on the response, it updates the status of the API, and based on the transition in state, calls the required method to send an email.

**api_status**: This is just a simple object which is used to track the state of the API.

**file_util**: This takes care of getting or setting the state of the API between calls to `api_checker`. The state is stored as a pickle file, which is basically just the serialized `api_status` object.

**mail_util**: This takes care of sending the email to the receipients mentioned in the receipients variable.


**api_poller**: This is just a simple poller that calls the `api_checker` using `os.system`. It makes a system call instead of just calling the `check_api()` method, because this way, we can decide to replace the `api_poller` with more stable utilities in the future, like say, `crontab`.
