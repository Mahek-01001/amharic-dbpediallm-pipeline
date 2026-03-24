import re

def normalize(text):
    return re.sub(r"\s+", "_", text.strip())