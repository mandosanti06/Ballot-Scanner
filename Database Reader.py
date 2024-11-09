from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client
#Login to the database
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

# Fetch the count of submissions with the same name
response = supabase.table('Estatal (Gobernación)').select('name', count='exact').execute()
data = response.data
name_counts = {}
for record in data:
    name = record['name']
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

# Grab the nth key in name_counts
print("The number of votes of each candidate for Gobernor is:")
key_list = list(name_counts.keys())
for i in range(len(key_list)):
    print(key_list[i] + " has " + str(name_counts[key_list[i]]) + " votes")
print("")
print("The number of votes of each candidate for Resident Commissioner is:")
response = supabase.table('Estatal (Comisionado Residente)').select('name', count='exact').execute()
data = response.data
name_counts = {}
for record in data:
    name = record['name']
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
key_list = list(name_counts.keys())
for i in range(len(key_list)):
    print(key_list[i] + " has " + str(name_counts[key_list[i]]) + " votes")
print("")
print("The number of votes of each party is:")
response = supabase.table('Estatal (Partidos)').select('name', count='exact').execute()
data = response.data
name_counts = {}
for record in data:
    name = record['name']
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
key_list = list(name_counts.keys())
for i in range(len(key_list)):
    print(key_list[i] + " has " + str(name_counts[key_list[i]]) + " votes")
# Close the database connection