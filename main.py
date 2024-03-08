from getpass import getpass
from database import Database
from mysql.connector import connect
from dotenv import load_dotenv
import os
from main_menu import main_menu


# Load environment variables from .env file
load_dotenv()

# Get database connection credentials from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

# Connect to Database
try:
    db = Database(host=DB_HOST, username=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
except Exception as e:
    print("Something went wrong. Please try again later!") #:

main_menu(db)