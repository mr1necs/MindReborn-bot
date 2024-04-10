import gspread


gc = gspread.service_account(
    filename='/Users/mr1necs/Documents/GitHub/Testing-work-bot/app/testing-work-bot-8909f6be7ad6.json')
sh = gc.open("Bot Data")