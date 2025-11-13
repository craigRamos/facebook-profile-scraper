thonimport sys
from extractors.facebook_parser import parse_facebook_profile
from outputs.exporters import export_to_json

def main():
    if len(sys.argv) < 2:
        print("Usage: python runner.py <facebook_profile_url>")
        sys.exit(1)

    url = sys.argv[1]
    profile_data = parse_facebook_profile(url)
    export_to_json(profile_data)

if __name__ == "__main__":
    main()