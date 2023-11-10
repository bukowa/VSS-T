# convert from https://themes.vscode.one/ to .json
import json

# open the JSON file
file_path = "vss-t-color-theme.json"
file_path2 = "./VSS-T/VSS-T.json"

with open(file_path, "r") as file:
    data = json.load(file)

# Save the modified data back to the file
print("Saving the file...")
with open(file_path2, "w") as file:
    json.dump({
    "$schema": "vscode://schemas/color-theme",
    "type": "dark",
    "colors": data["colors"],
    "tokenColors": data["tokenColors"],
}, file, indent=2)