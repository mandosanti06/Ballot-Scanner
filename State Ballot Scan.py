import cv2

file=input("Enter the name of the file: ")
# Load the test image
image_path = f'State Ballot Tests/{file}'
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)

# Define coordinates for checkboxes
checkboxes = {
    "Partido Nuevo Progresista": (497, 334, 114, 84),
    "Partido Popular Democrático": (1058, 334, 114, 84),
    "Movimiento Victoria Ciudadana": (1619, 334, 114, 84),
    "Partido Independentista Puertorriqueño": (2180, 334, 114, 84),
    "Proyecto Dignidad": (2742, 335, 113, 83),
    "Jennifer González": (355, 636, 77, 52),
    "William Villafañe": (355, 817, 77, 52),
    "Jesús Manuel Ortiz": (917, 636, 77, 52),
    "Pablo José Hernández Rivera": (917, 817, 77, 52),
    "Javier Córdova Iturregui": (1479, 636, 76, 52),
    "Ana Irma Rivera Lassén": (1479, 817, 76, 52),
    "Juan Dalmau": (2041, 636, 76, 51),
    "Roberto Karlo Velázquez Correa": (2040, 818, 75, 50),
    "Javier Jiménez Pérez": (2603, 636, 76, 51),
    "Viviana Ramírez Morales": (2603, 817, 76, 51),
    "Write-in Gobernador": (3165, 636, 76, 51),
    "Write-in Comisionado Residente": (3165, 817, 76, 51)
}


# Separate candidates into two groups
gobernor_candidates = [
    "Jennifer González", "Jesús Manuel Ortiz", "Javier Córdova Iturregui",
    "Juan Dalmau", "Javier Jiménez Pérez", "Write-in Gobernador"
]
resident_commissioner = [
    "William Villafañe", "Pablo José Hernández Rivera", "Ana Irma Rivera Lassén",
    "Roberto Karlo Velázquez Correa", "Viviana Ramírez Morales", "Write-in Comisionado Residente"
]
parties = ["Partido Nuevo Progresista", "Partido Popular Democrático", "Movimiento Victoria Ciudadana", "Partido Independentista Puertorriqueño", "Proyecto Dignidad"]

# Set detection threshold
threshold = 500
results = {}

# Check each checkbox area
for candidate, (x, y, w, h) in checkboxes.items():
    # Extract region of interest
    roi = adaptive_thresh[y:y+h, x:x+w]

    # Count non-zero pixels in the ROI
    non_zero_count = cv2.countNonZero(roi)

    # Determine if checkbox is marked
    if non_zero_count > threshold:
        results[candidate] = "Marked"
    else:
        results[candidate] = "Not marked"

# Check results for each group
gobernor_marked = [candidate for candidate in gobernor_candidates if results.get(candidate) == "Marked"]
resident_commissioner_marked = [candidate for candidate in resident_commissioner if results.get(candidate) == "Marked"]
party_marked = [candidate for candidate in results if "Partido" in candidate and results.get(candidate) == "Marked"]

# Parties
if "Party Nuevo Progresista" in party_marked:
    if gobernor_marked == []:
        gobernor_marked.append("Jennifer González")
    if resident_commissioner_marked == []:
        resident_commissioner_marked.append("William Villafañe")
elif "Partido Popular Democrático" in party_marked:
    if gobernor_marked == []:
        gobernor_marked.append("Jesús Manuel Ortiz")
    if resident_commissioner_marked == []:
        resident_commissioner_marked.append("Pablo José Hernández Rivera")
elif "Movimiento Victoria Ciudadana" in party_marked:
    if gobernor_marked == []:
        gobernor_marked.append("Javier Córdova Iturregui")
    if resident_commissioner_marked == []:
        resident_commissioner_marked.append("Ana Irma Rivera Lassén")
elif "Partido Independentista Puertorriqueño" in party_marked:
    if gobernor_marked == []:
        gobernor_marked.append("Juan Dalmau")
    if resident_commissioner_marked == []:
        resident_commissioner_marked.append("Roberto Karlo Velázquez Correa")
elif "Proyecto Dignidad" in party_marked:
    if gobernor_marked == []:
        gobernor_marked.append("Javier Jiménez Pérez")
    if resident_commissioner_marked == []:
        resident_commissioner_marked.append("Viviana Ramírez Morales")

# Determine the ballot status
if len(gobernor_marked) > 1:
    action = input("More than one Gobernor candidate marked. Do you want to vote or correct the ballot? (vote/correct): ")
    if action.lower() == "vote":
        if len(resident_commissioner_marked) == 0:
            action = input("There are fewer votes than expected. Do you want to change or vote? (change/vote): ")
            if action.lower() == "vote":
                print("Ballot accepted")
                print("Selected Gobernor candidates:", gobernor_marked)
                print("Selected Resident Commissioner candidates:", resident_commissioner_marked)
                print("Selected party candidates:", party_marked)
            elif action.lower() == "change":
                print("Ballot returned for change.")
            else:
                print("Invalid input. Ballot returned.")
        else:
            print("Ballot accepted")
            print("Selected Gobernor candidates:", gobernor_marked)
            print("Selected Resident Commissioner candidates:", resident_commissioner_marked)
            print("Selected party candidates:", party_marked)
    elif action.lower() == "correct":
        print("Ballot returned for correction.")
    else:
        print("Invalid input. Ballot returned.")
elif len(resident_commissioner_marked) > 1:
    action = input("More than one Resident Commissioner candidate marked. Do you want to vote or correct the ballot? (vote/correct): ")
    if action.lower() == "vote":
        if len(gobernor_marked) == 0:
            action = input("There are fewer votes than expected. Do you want to change or vote? (change/vote): ")
            if action.lower() == "vote":
                print("Ballot accepted")
                print("Selected Gobernor candidates:", gobernor_marked)
                print("Selected Resident Commissioner candidates:", resident_commissioner_marked)
                print("Selected party candidates:", party_marked)
            elif action.lower() == "change":
                print("Ballot returned for change.")
            else:
                print("Invalid input. Ballot returned.")
        else:
            print("Ballot accepted")
            print("Selected Gobernor candidates:", gobernor_marked)
            print("Selected Resident Commissioner candidates:", resident_commissioner_marked)
            print("Selected party candidates:", party_marked)
    elif action.lower() == "correct":
        print("Ballot returned for correction.")
    else:
        print("Invalid input. Ballot returned.")
else:
    if len(gobernor_marked) == 0 or len(resident_commissioner_marked) == 0:
        action = input("There are fewer votes than expected. Do you want to change or vote? (change/vote): ")
        if action.lower() == "vote":
            print("Ballot accepted")
            print("Selected Gobernor candidates:", gobernor_marked)
            print("Selected Resident Commissioner candidates:", resident_commissioner_marked)
            print("Selected party candidates:", party_marked)
        elif action.lower() == "change":
            print("Ballot returned for change.")
        else:
            print("Invalid input. Ballot returned.")
    else:
        print("Ballot accepted")
        print("Selected Gobernor candidates:", gobernor_marked)
        print("Selected Resident Commissioner candidates:", resident_commissioner_marked)
        print("Selected party candidates:", party_marked)
