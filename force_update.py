
import os
import datetime
import re

file_path = r"..\website\double-pole-tarp\index.html"
timestamp = datetime.datetime.now().strftime("%H:%M:%S")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Force image update to hero_new.png
    # Replace any img src that looks like D01.png or main_visual.* with hero_new.png
    new_content = re.sub(r'src="/double-pole-tarp/images/.*?\.(png|jpg).*?"', 'src="/double-pole-tarp/images/hero_new.png"', content)
    
    # 2. Add/Update Debug Timestamp
    if "(Update Check:" in new_content:
        new_content = re.sub(r'<span style="font-size:0.5em;color:red;">\(Update Check:.*?\)</span', '', new_content)
    
    new_content = new_content.replace("</h1>", f'<span style="font-size:0.5em;color:red;">(Update Check: {timestamp})</span></h1>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully UPDATED {file_path}")

except Exception as e:
    print(f"Error: {e}")
