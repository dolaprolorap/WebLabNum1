from dotenv import load_dotenv
import os

load_dotenv()

STATIC_PATH = os.environ.get("STATIC_PATH")

WINDOW_HEIGHT = os.environ.get("WINDOW_HEIGHT")
WINDOW_WIDTH = os.environ.get("WINDOW_WIDTH")

PORT = os.environ.get("PORT")