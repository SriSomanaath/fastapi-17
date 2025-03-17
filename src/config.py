import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")
