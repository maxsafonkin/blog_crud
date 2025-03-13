import os

# for local tests
# from dotenv import load_dotenv
# load_dotenv(os.environ["DOTENV_FILE_PATH"])

DB_HOST = os.environ["DB_HOST"]
DB_PORT = int(os.environ["DB_PORT"])
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]
