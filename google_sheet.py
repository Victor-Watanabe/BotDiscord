import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "18kaJLF0OBLkMNS9fKx4Q_HPYQZ37So91-NXr7WURL2c"
SAMPLE_RANGE_NAME = "WorkSheet!C2:C"

other_status = [["Ausente"]]
new_status = [["Na Comunidade"]]
old_status = ['Na Comunidade']

def string_sublist(sublist):
      return ' '.join(map(str, sublist))

def main(email, username):

  creds = None
  
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])
    user_data = [[username]]
    
    # Mapear cada sublista para uma string usando map
    string_list = list(map(string_sublist, values))
     
    if values:
        if email in string_list:
          position = string_list.index(email) + 2
          SAMPLE_RANGE_NAME_WRITE_STATUS = "WorkSheet!G{}".format(position)
          result_status = (
              sheet.values()
              .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_WRITE_STATUS)
              .execute()
          )
          values_status = result_status.get("values", [])
          status_list = list(map(string_sublist, values_status)) 
          if old_status == status_list:
            return False
          else:
            status = (
              sheet.values()
              .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_WRITE_STATUS, valueInputOption = "USER_ENTERED", body={"values": new_status}).execute()
          )
            SAMPLE_RANGE_NAME_WRITE_USERNAME = "WorkSheet!H{}".format(position)
            user_api = (
              sheet.values()
              .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_WRITE_USERNAME, valueInputOption = "USER_ENTERED", body={"values": user_data}).execute()
          )
            return True
        else:
            return False
    else:
        print("Nenhum dado retornado.")
  except HttpError as err:
    print(err)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "18kaJLF0OBLkMNS9fKx4Q_HPYQZ37So91-NXr7WURL2c"
SAMPLE_RANGE_USERNAME = "WorkSheet!H2:H"

def secondary (name):

  creds = None
  
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_USERNAME)
        .execute()
    )
    values = result.get("values")
      
    # Mapear cada sublista para uma string usando map
    string_list = list(map(string_sublist, values))
   
    if values:
        if name in string_list:
            position = string_list.index(name) + 2
            SAMPLE_RANGE_NAME_WRITE_STATUS = "WorkSheet!G{}".format(position)
            status = (
              sheet.values()
              .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_WRITE_STATUS, valueInputOption = "USER_ENTERED", body={"values": other_status}).execute()
          )
        else:
            pass
    else:
        print("Nenhum dado retornado.")
  except HttpError as err:
    print(err)




if __name__ == "__main__":
  main()
