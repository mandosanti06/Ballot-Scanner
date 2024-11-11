from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def fetch_votes(table_name):
    try:
        response = supabase.table(table_name).select('name', count='exact').execute()
        data = response.data
        name_counts = {}
        total_votes = 0
        for record in data:
            name = record['name']
            if name in name_counts:
                name_counts[name] += 1
            else:
                name_counts[name] = 1
            total_votes += 1

        # Calculate percentages
        name_percentages = {name: (count / total_votes) * 100 for name, count in name_counts.items()}
        return name_counts, name_percentages, total_votes
    except Exception as e:
        print(f"Error fetching votes from {table_name}: {e}")
        return {}, {}, 0

@app.route('/')
def index():
    gobernor_votes, gobernor_percentages, total_gobernor_votes = fetch_votes('Estatal (Gobernación)')
    commissioner_votes, commissioner_percentages, total_commissioner_votes = fetch_votes('Estatal (Comisionado Residente)')
    party_votes, party_percentages, total_party_votes = fetch_votes('Estatal (Partidos)')
    total_votes_counted = total_gobernor_votes + total_commissioner_votes + total_party_votes
    return render_template('index.html',
                           gobernor_votes=gobernor_votes,
                           gobernor_percentages=gobernor_percentages,
                           total_gobernor_votes=total_gobernor_votes,
                           commissioner_votes=commissioner_votes,
                           commissioner_percentages=commissioner_percentages,
                           total_commissioner_votes=total_commissioner_votes,
                           party_votes=party_votes,
                           party_percentages=party_percentages,
                           total_party_votes=total_party_votes,
                           total_votes_counted=total_votes_counted)

if __name__ == '__main__':
    app.run(debug=True)