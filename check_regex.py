import json
import re


def validate_seva_names(file_path):
    """
    Validate that all 'Name' values in the JSON file match the pSEVA\d+ regex pattern.

    Args:
        file_path (str): Path to the index.json file

    Returns:
        bool: True if all names match the pattern, False otherwise
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        # Regex pattern to match pSEVA followed by one or more digits
        pattern = re.compile(r"^pSEVA\d+.*$")

        # Check each entry's Name against the pattern
        for entry in data:
            name = entry.get("Name", "")
            if name and not pattern.match(name):
                print(f"Invalid name found: {name}")
                return False

        return True

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {file_path}")
        return False


# Example usage
if __name__ == "__main__":
    result = validate_seva_names("index.json")
    print("All SEVA names are valid" if result else "Some SEVA names are invalid")
