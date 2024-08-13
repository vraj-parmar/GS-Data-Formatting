# Google Sheets Data Formatting

This project automates the process of formatting and cleaning data in a Google Sheet using Python. The script connects to a Google Sheet, reformats the data, deduplicates it, and updates the sheet with the cleaned data.

## Features

- **Google Sheets Integration**: Connects to a Google Sheet using the Google Sheets API.
- **Data Formatting**: Reformats date fields and processes data entries.
- **Deduplication**: Removes duplicate entries from the dataset.
- **Sheet Management**: Updates the existing sheet with formatted and cleaned data or creates a new worksheet if it doesn't exist.

## Requirements

- Python 3.7 or higher
- [Pygsheets](https://pygsheets.readthedocs.io/en/latest/) library
- [Pandas](https://pandas.pydata.org/) library
- Google Cloud Platform service account with access to Google Sheets API
- `.env` file with the Google Sheet URL and credentials path

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/vraj-parmar/GS-Data-Formatting.git
    cd GS-Data-Formatting
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the `.env` file**:
   Create a `.env` file in the root directory of the project and add the following:

    ```
    GOOGLE_SHEET_URL="your_google_sheet_url"
    CREDENTIALS_JSON_PATH="config/credentials.json"
    ```

    - Replace `"your_google_sheet_url"` with the actual URL of the Google Sheet you want to format.
    - The `CREDENTIALS_JSON_PATH` should point to the location of your Google service account credentials file.

4. **Place your Google service account credentials** in the `config/` directory.

## Usage

Run the script using Python:

```bash
python main.py
```

The script will:
- Connect to the Google Sheet specified in your `.env` file.
- Reformat and clean the data in the first sheet of the document.
- Create or update a worksheet titled "Formatted_Reg" with the cleaned data.

After the script completes, you can find the cleaned and formatted data in the "Formatted_Reg" sheet within the same Google Sheet document.

## Acknowledgements

- [Pygsheets](https://pygsheets.readthedocs.io/) - For seamless Google Sheets integration.
- [Pandas](https://pandas.pydata.org/) - For powerful data manipulation.
