# BASIC
# Write = json.dump()
# Read = json.load()
# Update = json.update()

# ================= JSON NOTES (PYTHON) =================
import json
import os

FILE = "data.json"

# ---------- BASIC RULES ----------
# json.load(file)   -> file → Python dict/list
# json.dump(data,f) -> Python → file
# json.loads(str)   -> string → Python
# json.dumps(data)  -> Python → string


# ---------- LOAD JSON ----------
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
except json.JSONDecodeError:
    data = {}

print("Loaded:", data)


# ---------- SAVE JSON ----------
with open(FILE, "w") as f:
    json.dump(data, f, indent=4)


# ---------- ADD / UPDATE ----------
# Add new key
data["name"] = "John"

# Update key
data["name"] = "Alice"


# ---------- REMOVE ----------
# Remove key
data.pop("name", None)


# ---------- CHECK ----------
if "name" in data:
    print("Key exists")


# ---------- SAFE ACCESS ----------
print(data.get("name"))

# Nested safe access
# Example: data["gmail"]["email"]
print(data.get("gmail", {}).get("email"))


# ---------- LIST JSON ----------
# Example JSON:
# [
#   {"name":"John"},
#   {"name":"Alice"}
# ]

# Append item
if isinstance(data, list):
    data.append({"name": "Bob"})


# ---------- UPDATE FILE PATTERN ----------
try:
    with open(FILE,"r") as f:
        data = json.load(f)
except:
    data = {}

data["example"] = "value"

with open(FILE,"w") as f:
    json.dump(data,f,indent=4)


# ---------- JSON STRING ----------
json_string = '{"name":"John"}'

dict_data = json.loads(json_string)

print(dict_data)


# ---------- DICT → JSON STRING ----------
new_json_string = json.dumps(data)

print(new_json_string)


# ---------- PRETTY PRINT ----------
print(json.dumps(data, indent=4))


# ---------- TYPE CONVERSION ----------
# JSON -> Python
# object -> dict
# array -> list
# string -> str
# number -> int/float
# true -> True
# false -> False
# null -> None


# ---------- COMMON STRUCTURE ----------
# Example structure:
#
# {
#     "gmail": {
#         "email": "a@gmail.com",
#         "password": "123"
#     }
# }

# Access example:
# data["gmail"]["email"]
# data["gmail"]["password"]


# ---------- BEST PRACTICE TEMPLATE ----------
try:
    with open(FILE,"r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}

# MODIFY DATA HERE
# data["site"] = {"email":"a@gmail.com","password":"123"}

with open(FILE,"w") as f:
    json.dump(data,f,indent=4)


# ================= END NOTES =================