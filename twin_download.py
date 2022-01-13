from pprint import pprint
import pandas
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials



def get_pandas_from_google_sheets(spreadsheet_id, CREDENTIALS_FILE='twin_creds.json', output_filename="output.csv"):
    '''This function gets the file from the Google Developer Console and
     the ID of the Google Sheets document (can be taken from its URL)
     It gets data from this table and returns pandas'''

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http = httpAuth)

    # Пример чтения файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:K41',
        majorDimension='ROWS'
    ).execute()

    data_pandas=pandas.DataFrame(values['values'])
    #print(d)
    data_pandas.to_csv(output_filename, index=False, header=False)
    return data_pandas


if __name__ == '__main__':
    get_pandas_from_google_sheets('1h_MA67-SV3SmfM92aT-NS3I4aHZ4bqa4rQZhcVx7Ehk')