# State Ballot Scan Project

## Overview

This project is designed to scan and process state ballots, determine the marked candidates and parties, and store the results in a Supabase database. It also includes functionality to read and display the stored results.

## Project Structure

- `state_ballot_scan.py`: Contains the logic for scanning the ballot, determining marked candidates and parties, and handling user input for ballot corrections.
- `Database Writer.py`: Handles writing the scanned ballot results to the Supabase database.
- `Database Reader.py`: Fetches and displays the count of votes for each candidate and party from the Supabase database.

## Requirements

- Python 3.x
- OpenCV
- Supabase Python Client
- Python Dotenv

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install opencv-python supabase-python python-dotenv
    ```

3. Create a `.env` file in the project root directory and add your Supabase credentials:
    ```
    SUPABASE_URL=<your_supabase_url>
    SUPABASE_KEY=<your_supabase_key>
    ```

## Usage

### Scanning and Writing Ballot Data

1. Run the `Database Writer.py` script to scan a ballot image and write the results to the database:
    ```sh
    python Database Writer.py
    ```

### Reading and Displaying Ballot Data

1. Run the `Database Reader.py` script to fetch and display the count of votes for each candidate and party:
    ```sh
    python Database Reader.py
    ```

## License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for more details.
