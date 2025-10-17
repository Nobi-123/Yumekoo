import os

class config:

    # ==================== Client ====================
    API_ID = int(os.getenv("API_ID", 22657083))
    API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7489206821:AAGkkjz2rCQmZN33PUR9sKwhr-PI1fNp64U")
    BOT_NAME = "𝐑 𝐀 𝐅 𝐈 𝐍"
    BOT_USERNAME = "RafinGroupBot"
    BOT_ID = 7489206821
    WORKERS = 30
    MAX_MESSAGE_CACHE_SIZE = 100
    MAX_CONCURRENT_TRANSMISSIONS = 10

    # ==================== Git ====================
    GIT_USERNAME = "Nobi-123"
    GIT_URL_WITH_TOKEN = "https://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@github.com/Nobi-123/Yumeko.git" 

    # ==================== Info ====================
    BOT_VERSION = "x"
    OWNER_ID = int(os.getenv("OWNER_ID", 8076443359))
    OWNER_USERNAME = "SemxyCarders"
    SUPPORT_CHAT = -1003180602440
    SUPPORT_CHAT_USERNAME = "TNCmeetup"
    SUPPORT_CHAT_LINK = "https://t.me/TNCmeetup"
    LOG_CHANNEL = -1003180602440
    ERROR_LOG_CHANNEL = -1003180602440
    DOWNLOAD_LOCATION = "./downloads"
    COMMAND_PREFIXES = ["/" , "!" , "." , "#" , "$" , "%" , "&" , "?"] 
    CMD_STARTERS = "/.!&#%$"
    STATS_IMG_URL = "https://files.catbox.moe/d69tm0.jpg"
    START_IMG_URL = "https://files.catbox.moe/wybrme.jpg"
    HELP_IMG_URL = "https://files.catbox.moe/j3tdbi.jpg"
    ALIVE_IMG_URL = "https://files.catbox.moe/w4t9cj.jpg"

    # ==================== Database ====================
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://ahad0181888:ahad0181888@cluster0.f9casz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = "Frieren"

    # ==================== APIs ====================
    ARQ_API_KEY = "RLWCED-WZASYO-AWOLTB-ITBWTP-ARQ"
    ARQ_API_URL = "arq.hamker.dev"
    CRICKET_API_URL = "https://sugoi-api.vercel.app/cricket"
    FOOTBALL_API_URL = "https://sugoi-api.vercel.app/football"
    BINGSEARCH_URL = "https://sugoi-api.vercel.app/search"
    NEWS_URL = "https://sugoi-api.vercel.app/news?keyword={}"
    shayri_api_url = "https://hindi-quotes.vercel.app/random"
    BASE_URL = "https://api.waifu.pics"
    Movie_Api = "5d3274c3bb08b4276482436c8444abc0"
    Movie_RAC = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDMyNzRjM2JiMDhiNDI3NjQ4MjQzNmM4NDQ0YWJjMCIsIm5iZiI6MTczMzIyMjgxMy42OTQwMDAyLCJzdWIiOiI2NzRlZTE5ZDJjZTRjZTdkZDYwOTU2YjAiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.aXfQw0_CRrKl2iSJd9tFE1TVbWWVYNgysWkUVlwzyRg"
    Pokedex = "https://sugoi-api.vercel.app/pokemon?name={name_or_id}"
    OPENAI_KEY = "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"
    LYRICS_GENIUS_TOKEN = "D5BK03zvcTNIfunVRptHavsYv5XfFgKknHXjad-wxi65PgEz_mGgdZnxZlnSpKXZ"

    # ==================== Music API & Caching ====================
    API_URL = os.getenv("API_URL", "https://api.thequickearn.xyz")        # Audio
    VIDEO_API_URL = os.getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")  # Video
    API_KEY = os.getenv("API_KEY", "Your_api_key")                        # API Key
    CACHE_PATH = os.getenv("CACHE_PATH", "./cache")                       # Temp audio/video storage
    CACHE_EXPIRY = int(os.getenv("CACHE_EXPIRY", 60))                     # Seconds to keep file
    CLEANUP_AFTER = int(os.getenv("CLEANUP_AFTER", 30))                   # Extra cleanup delay