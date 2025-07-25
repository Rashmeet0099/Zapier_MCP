"""import os
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_to_zapier_mcp(name, email, dob):
    client = openai.OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input=f"Add a new user registration to the Google Sheet:\n"
              f"Name: {name}, Email: {email}, DOB: {dob}",
        tool_choice="required",
        tools=[{
            "type": "mcp",
            "server_label": "zapier",
            "server_url": "https://mcp.zapier.com/api/mcp/mcp",
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {os.getenv('ZAPIER_BEARER_TOKEN')}",
            },
        }],
    )
    return response

def fetch_all_registrations_from_sheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("MCP").worksheet("Sheet1")  # Match spreadsheet and worksheet names
        data = sheet.get_all_records()
        return data

    except Exception as e:
        return f"❌ Error reading Google Sheet: {str(e)}"     """
        
