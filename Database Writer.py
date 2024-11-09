from dotenv import load_dotenv
load_dotenv()
from state_ballot_scan import state_ballot

import os

from supabase import create_client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Dictionary to be inserted
data_dict = state_ballot('State Ballot Tests/Write In.png')

# Insert Gobernor data
for gobernor in data_dict['Gobernor']:
    supabase.table("Estatal (Gobernación)").insert({"name": gobernor}).execute()

# Insert Resident Commissioner data
for commissioner in data_dict['Resident Commissioner']:
    supabase.table("Estatal (Comisionado Residente)").insert({"name": commissioner}).execute()

# Insert Party data
for party in data_dict['Party']:
    supabase.table("Estatal (Partidos)").insert({"name": party}).execute()