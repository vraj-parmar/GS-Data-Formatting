from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the path to the JSON file from environment variables
json_path = os.getenv('CREDENTIALS_JSON_PATH')
print(json_path)