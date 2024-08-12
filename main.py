import pygsheets
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Get the path to the GS URL and JSON file from environment variables
load_dotenv()

URL = os.getenv("GOOGLE_SHEET_URL")
json_path = os.getenv('CREDENTIALS_JSON_PATH')

# Open the Google Sheet
gc = pygsheets.authorize(service_account_file=json_path)

sheet = gc.open_by_url(URL)

# Access the Sheet1
worksheet = sheet.sheet1

# Get the data from the first 4 columns
data = worksheet.get_all_values(returnas='matrix')

# Extract the header row
header_row = data[0]

# Extract the data rows (excluding the header)
data_rows = data[1:]

# Reformat the data
formatted_data = []
for row in data_rows:
    if any(row):  # Skip rows with all empty values
        submission_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M') if row[0] else ''
        date = datetime.strptime(row[1], '%d-%m-%Y').strftime('%d/%m/%Y') if row[1] else ''
        sid_ = ''
        sabha_centre = row[3] if row[3] else ''
        sids = row[4].replace('\r', '').split('\n') if row[4] else []
        purpose = row[5] if row[5] else ''
        mandal = row[6] if row[6] else ''

        for sid in sids:
            formatted_row = [submission_date, date, sid_, sabha_centre, sid, purpose, mandal]
            formatted_data.append(formatted_row)

# Prepend the header row to the formatted data
formatted_data.insert(0, header_row)

# Create or access the "Formatted_Reg" worksheet
try:
    formatted_worksheet = sheet.worksheet('title', 'Formatted_Reg')
except pygsheets.WorksheetNotFound:
    formatted_worksheet = sheet.add_worksheet('Formatted_Reg')

# Clear the existing data in the "Formatted_Reg" worksheet
formatted_worksheet.clear()

# Update the "Formatted_Reg" worksheet with the reformatted data
formatted_worksheet.update_values('A1', formatted_data)

# Convert the data to a pandas DataFrame for deduplication
df = pd.DataFrame(formatted_data, columns=header_row)

# Remove duplicates based on all columns
df = df.drop_duplicates()

# Remove empty cells (NaN values)
df = df.replace('', pd.NA).dropna()

# Update the "Formatted_Reg" worksheet with the deduplicated and cleaned data
formatted_worksheet.set_dataframe(df, start='A1')
print("DONE")