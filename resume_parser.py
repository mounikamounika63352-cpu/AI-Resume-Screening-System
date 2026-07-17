import re

# -------------------------------
# Extract Email
# -------------------------------
def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


# -------------------------------
# Extract Phone
# -------------------------------
def extract_phone(text):
    pattern = r"\+?\d[\d\s\-]{8,}\d"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


# -------------------------------
# Extract Name
# -------------------------------
def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 3 and len(line.split()) <= 4:

            if not any(char.isdigit() for char in line):
                return line.title()

    return "Not Found"