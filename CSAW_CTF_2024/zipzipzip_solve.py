import base64
import os
import zipfile
"""
i = 0
while True:
    # Unzip everything until we get error.
    with zipfile.ZipFile(f"./chunk_{i}.zip", 'r') as f:
        f.extractall()
    i += 1

for i in range(0, 32796):
    os.remove(f"./chunk_{i}.zip")

extracted_data = ""
for i in range(0, 32796):
    with open(f"./chunk_{i}.txt", "r") as f:
        data = f.read()
    extracted_data += data
with open("./0_extracted.txt", "w") as f:
    f.write(extracted_data)
"""
with open("./0_extracted.txt", "r") as f:
    data = f.read()
decoded = base64.b64decode(data)
with open("0_decoded.bin", "wb") as f:
    f.write(decoded)