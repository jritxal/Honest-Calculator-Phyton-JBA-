raw = input()
processed = raw.replace(",", "")
processed = processed.replace(".", "")
processed = processed.replace("!", "")
processed = processed.replace("?", "")
print(processed.lower())
