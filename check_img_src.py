
import os

file_path = r"..\website\double-pole-tarp\index.html"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if 'alt="Main Visual"' in line:
                print(f"FOUND LINE: {line.strip()}")
                break
    else:
        print("Line with alt='Main Visual' not found.")
        
except Exception as e:
    print(f"Error: {e}")
