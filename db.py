import pandas as pd
import streamlit as st
import gspread
from datetime import timedelta
from google.oauth2 import service_account
import numpy as np

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Load credentials from Streamlit secrets
service_account_info = st.secrets["gcp_service_account"]
creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=scope)

    # Authorize the credentials with gspread
client = gspread.authorize(creds)

    # Access the Google Sheet using the spreadsheet ID
spreadsheet_id = "19PaTSR26LeiEPzmdCJqS_x3-GjZfaRzKLvsHwQ6mPts"
sheet = client.open_by_key(spreadsheet_id)

def getalldata():
    return sheet


