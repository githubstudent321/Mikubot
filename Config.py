import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6081090203:AAEVJrfAbpbhLyhSXa3TO9nHreKqxqBsvOo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLkBuz5JEMT-R2wipvjMJbA9RohUtY6H_Ck9G4JVWN4a4WF5SoGeQ08gEiZ-nVA8TOox2llANxK0GMtUsHhbT9B_ptxDd57Oe3hyXdwqCmmhu5PQOcufsm8whCvO6xpVChVneRg1GPX5L9AwnDEuVV_obQa_yGUYFUhKmIGj8A5Dd0eyBN5wvclKVwOkObxxzucFrH0kYKPBD28T64uq26f0C_TScisr2Oed9h_kAt0C3Uwd_KxXH1df7xQB5mK1_xFDM2-EKyL2-D7l5ZDvXZfPdjjDM7tJSJXufX__dHI9S-Aa2O-M4lXaYMCuv-R07RCEYv8xJ5HT5tZjH20JlFatmfE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mikkumusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5338384454")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
