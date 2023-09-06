from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import login_spreadsheets

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = login_spreadsheets.loginSpreadsheet_id
SAMPLE_RANGE_NAME = login_spreadsheets.loginSampleRangeName


def conectar():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

def read():
    # Conectar com a planilha do google (Sempre executar esse código)
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    #aqui mostra oq eu vou pegar da planilha
    values = result.get('values', [])    
    return values

def write(quantidadeItensLista, listaAtualizacao):

    quantidadeCalculado = quantidadeItensLista ++1
    rangeWrite = f"Página1!A{quantidadeCalculado}"
        
    # Conectar com a planilha do google (Sempre executar esse código)
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    try:
        # Call the Sheets API
        
        result = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rangeWrite, 
                                    valueInputOption="USER_ENTERED", 
                                    body={'values': listaAtualizacao}).execute()

        return result
    
    except HttpError as error:
        print(f"Erro na gravacao do GoogleSheet: {error}")
        return error

#conectar()