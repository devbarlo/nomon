from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9572580"))
API_HASH = getenv("API_HASH", "c746d70303fcb2fdc0c1b41e5066f537")
BOT_TOKEN = getenv("BOT_TOKEN", "1801681232:AAHwfkaI5a4tv_su66qTAGk6tjyHUeKCzSA")
STRING_SESSION = getenv("STRING_SESSION","BADExFUoHEBVl7G3s2Ixx0JpqpkLRzhQIt-2femDOICsVAldxpqm222UVyBDZaaoMqe4UlOX6cu8jEm17k6RDNIFdjmmGL70VhmFdSAAbaJkHgNZijtTdte2x_QC-pDFKX5DXC_s2L_A7vyllB8CV3USE0qkvcKeMHHgzSBPGJD485d_PjAT-aX_Usd3RST0sNa1u0FRyBG9hOGKq0X6GaYdurcWUVJG-HO_F7xaGxhBI9GcheoDKIScK8G984L28LkoeREW6xbhgWD-Cns3gzF1Bam7RbdVTK9AT4qsALvVpOG-xJVGsTsQ9wXMc0Ip6HdaZeYDEA8MeHyt11FrsVKGbMkpFAA")
BOT_USERNAME = getenv("BOT_USERNAME", "BARLO0O_bot")
SUPPORT = getenv("SUPPORT", "bar_lo0o")
CHANNEL = getenv("CHANNEL", "cr_source")
START_IMG = int(getenv("START_IMG", "https://telegra.ph/file/671d4aeb68744604215c5.jpg"))
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
