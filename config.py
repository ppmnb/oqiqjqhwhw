from telethon.sync import TelegramClient

from telethon.sessions import StringSession

import os

APP_ID = os.environ.get("APP_ID", "18922496")

APP_HASH = os.environ.get("APP_HASH", "371d1dc33eccaa19bb0814a27bb98f3c")

BOT_USERNAME = os.environ.get("BOT_USERNAME", "aiibot")

session = os.environ.get("TERMUX")

SESSION = os.environ.get("TERMUX", "1BJWap1sBuzsefozOB5bAwWg-c4tniXzFVd9PZRLYJSUFzRprr1CSYuGGIaxNofMrvZP2Do6mHdqlO94Lnm2LxJiqSX01udnD12O2DAHGN9DhzebSWC_jUsovJ4Kec_qatDdKhRmTvvWJ6PxBbWZ72yfk5zK-d-3HIWKk_dNFcNElWH3HTTmoO-y4047CKKzPCCVcmrcd27-GBTPM-NK0WN_z9DfaB8589PAQtwjZ1EmL-cIjVRh0tyheB4xSdSLTlg6Gkb7XGlXWYswpPiB6Znh3gZ3Y2NBIBm1sQL4Ys5s9YMtDIxz8CPIqJRcpi7T9AR5Ph-EmBQcloRop_m6Jg_CUFsHZS24=")

token = os.environ.get("TOKEN", "5663892372:AAGeOm-sRiIETxstqPYMSgOhWnaDu0ZNSFE")

fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)

bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)

ispay = ['yes']

ispay2 = ['yes']

bot.start()
