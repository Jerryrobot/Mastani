import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "10704655"))
    API_HASH = os.environ.get("API_HASH", "45aa4245259c66ecab638755b406f0a0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6284396856:AAEs4RM3cUOs6qxsfHey4EmVX2I-ZJl2HSo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCiqm0OsOA-mRQmiQzQOalDo9xzbBDo6BEqF8p8E-96cOLKaW8uxCxnBVbKjvUt3M_smRi2Ts8WIfPWisyyazkm6K73Yuqq3jxKTW3Exn0qMgqUsJK29WISzfIArhuPGsEfmpwC9r-7l9s3Zyql1ZwxAnrkgZx7aSdymrrm88j74odNUzzY_nkb04fZMjn_PSM9h50I0WrpGTU6wHNVMV4BugGsm1b5FZPiC7gCo_bC3Ec5lCSZzAjEIysuQXbV5lg3c4GM7cV4BhMB04BHRYgYj9WjlRawfC1aXy84WMfRwVUHDb4AACsRp3dkR0ZBPpden_gHWOjHjapFmhUw0-F9AAAAAHkPKFYA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Nafisa_x_musicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2031036502")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
