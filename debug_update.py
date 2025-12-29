
import os
import datetime

file_path = r"..\website\double-pole-tarp\index.html"
timestamp = datetime.datetime.now().strftime("%H:%M:%S")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if we already added a debug span, remove it if so
    if "(Update Check:" in content:
        import re
        content = re.sub(r'<span style="font-size:0.5em;color:red;">\(Update Check:.*?\)</span', '', content)

    # Add the new debug span
    new_content = content.replace("</h1>", f'<span style="font-size:0.5em;color:red;">(Update Check: {timestamp})</span></h1>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully modified {file_path}")

except Exception as e:
    print(f"Error: {e}")
