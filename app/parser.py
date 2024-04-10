import gspread
from app.config import CREDENTIALS

gc = gspread.service_account_from_dict(CREDENTIALS)

sh = gc.open("Bot Data")
worksheet = sh.sheet1
