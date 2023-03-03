import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20862508"))
    API_HASH = os.environ.get("API_HASH", "b0ed9dc92caed3e21da662b97b23a4b0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5973659336:AAHVBqHcEC9MeiSjS2YHduB6jyhF0AUrN3g-ZJl2HSo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJcBuwtFJ94wMcYYhOQk4BCVvonspI3qJP9tTHZy8tKE2DMtnw7l1RDYyuyw4W89GT5NtwHQMObR1ddsegS5FO_P0bAq3kGefQqWA_Fg6O-yqyUfsso1I9c8FXbWSYebqhtHuTa6FcOGGt6isYJ4LWQxXca5aqHCYGTqe3LwIA7Q3R24zyghiSLrm_Dgs_hx8Ht2aPpPff-Fw32_Hi4NRHm_EeNW1Gz-gZdns7qIgYQNHseMyFFT1U-LmGSImjCyMiecUnEWVyyNQg2-QI3IqCvYy-5LQWh0r_gL1o9ocg3LNkoNZdyTezd1Bs2vwjrIZqoYzMdrYGvQHVvCmly1iXixQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Xnzzgetsuzobot")
    SUPPORT = os.environ.get("SUPPORT", "-1001874507743") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "-1001780086074") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5454639216")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
