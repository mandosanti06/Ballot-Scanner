import random
import os
import subprocess
from dotenv import load_dotenv
from state_ballot_scan import state_ballot
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# List of all the images
l = ['Alianza.png', 'Dalmau.png', 'Dalmau and Pablo Jose.png', 'Dalmau and Pablo Jose (cross).png', 'Dalmau and Pablo Jose (cross - bad vote).png', 'Javier Jimenez and Irma.png', 'Party Error.png', 'PIP.png', 'PNP.png', 'PPD.png', 'Proyecto Dignidad.png', 'Proyecto Dignidad and Write In.png', 'Victoria Ciudadana.png', 'Write In.png']

# Function to run the script and handle the prompt
def run_script():
    process = subprocess.Popen(['python3', 'test_voting.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            if 'There are fewer votes than expected. Do you want to change or vote? (change/vote):' in output:
                process.stdin.write('vote\n')
                process.stdin.flush()

# Loop to insert data
for _ in range(10000):
    random_image = random.choice(l)

    data_dict = state_ballot(f'State Ballot Tests/{random_image}')

    # Automatically input a vote if required
    if 'Empty Ballot' in random_image:
        data_dict['Gobernor'].append('Default Gobernor')
        data_dict['Resident Commissioner'].append('Default Commissioner')
        data_dict['Party'].append('Default Party')

    # Insert Gobernor data
    for gobernor in data_dict['Gobernor']:
        supabase.table("Estatal (Gobernación)").insert({"name": gobernor}).execute()

    # Insert Resident Commissioner data
    for commissioner in data_dict['Resident Commissioner']:
        supabase.table("Estatal (Comisionado Residente)").insert({"name": commissioner}).execute()

    # Insert Party data
    for party in data_dict['Party']:
        supabase.table("Estatal (Partidos)").insert({"name": party}).execute()
    print(_)

# Run the script and handle the prompt
run_script()