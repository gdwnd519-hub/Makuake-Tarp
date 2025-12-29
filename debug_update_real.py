
import os
import datetime
import re

file_path = r"..\website\public\double-pole-tarp\index.html"
timestamp = datetime.datetime.now().strftime("%H:%M:%S")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add/Update Debug Timestamp
    if "(Update Check:" in content:
        content = re.sub(r'<span style="font-size:0.5em;color:red;">\(Update Check:.*?\)</span', '', content)
    
    new_content = content.replace("</h1>", f'<span style="font-size:0.5em;color:red;">(Update Check: {timestamp})</span></h1>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully UPDATED {file_path}")

except Exception as e:
    print(f"Error: {e}")
