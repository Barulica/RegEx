import re
import json

file_path = ('C:\\Users\\Barulacnik\\Desktop\\Python\\RegEx\\data\\user.json')

try:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)


        search_name = input("Enter your name: ")

        entry_found = None
        for entry in data.get("numbers", []):
            if entry.get("name").lower() == search_name.lower():
                entry_found = entry
                break
        if entry_found:
            phone_number = entry_found.get("phone","")
            phone_number_cleaned = phone_number.replace(" ", "").replace("+", "")
            phone_pattern = r"^38(1|2|5|9)"
            phone_match = re.match(phone_pattern, phone_number_cleaned)

            if phone_match:
                prefix = "38" + phone_match.group(1)
                phone_map = {
                    "381" : "serbia",
                    "382" : "bosnia",
                    "385" : "croatia",
                    "389" : "montenegro"
                }

                country = phone_map.get(prefix, "unknown")
                print(f"Phone Number: {phone_number}, Prefix: {prefix}, Country: {country}")
            else:
                print("No phone number found")

        else:
            print(f"No entry found for {search_name}")

except FileNotFoundError:
    print(f"File in {file_path} not found")
except json.decoder.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

