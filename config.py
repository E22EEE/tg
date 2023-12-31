import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 26484720))

    API_HASH = os.environ.get("API_HASH", "361cfa5b07e7cef672ecd44c0f4e17cb")
    SESSION = os.environ.get("SESSION", "")

    UBOT = os.environ.get("USER_BOT", "361cfa5b07e7cef672ecd44c0f4e17cb")
    DEVLOO = int(os.environ.get("ID_BOT", 6213845793))
    
