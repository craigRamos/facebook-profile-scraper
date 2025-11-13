thonimport json

def export_to_json(profile_data):
    with open('output.json', 'w') as file:
        json.dump(profile_data, file, indent=4)
    print("Profile data has been exported to output.json")