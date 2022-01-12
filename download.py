from pprint import pprint
import pandas
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials



def get_pandas_from_google_sheets(spreadsheet_id, CREDENTIALS_FILE='creds.json'):
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
        range='A1:E10',
        majorDimension='COLUMNS'
    ).execute()
    pprint(values)
    print(type(values))

    print(values['values'])
    d=pandas.DataFrame(values['values'])
    print(d)
    return d


if __name__ == '__main__':
    get_pandas_from_google_sheets('10VC6jkJuaYQ03Tq80usAb9Y7EcbVZ7ncpuffXXw8Ono')