"""
from os import getenv


API_ID = int(getenv("API_ID", "26797881"))
API_HASH = getenv("API_HASH", "9699262c708c2e45ba18bfce925ed5ed")
BOT_TOKEN = getenv("BOT_TOKEN", "7513124783:AAHNbZKlClU_5xjtLG3BZc6ffmopnwS5h1s")
OWNER_ID = int(getenv("OWNER_ID", "6567162029"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7081036509 7491167754").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://sevmamra01:<db_password>@cluster0.ff29e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002303981738"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002303981738"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

