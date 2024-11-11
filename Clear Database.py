from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def delete_all_rows(table_name):
    try:
        response = supabase.table(table_name).delete().neq('id', 0).execute()
        if response.status == 200:
            print(f"All rows deleted from {table_name}")
        else:
            print(f"Failed to delete rows from {table_name}: {response.status}")
    except Exception as e:
        print(f"Error deleting rows from {table_name}: {e}")

tables = ['Estatal (Gobernación)', 'Estatal (Comisionado Residente)', 'Estatal (Partidos)']

for table in tables:
    delete_all_rows(table)