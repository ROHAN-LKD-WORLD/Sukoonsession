from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("9303922"))
API_HASH = getenv("a17677495aa9ae010b897c2d65146282")

BOT_TOKEN = getenv("6281318666:AAH1JmtLA-QXVU8Kzue3GeYTx13hCSspqds")
OWNER_ID = int(getenv("7385703361"))

MONGO_DB_URI = getenv("mongodb+srv://sukoon:sukoon@cluster0.fldi6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("LINK_KI_DUNIYA", None)
