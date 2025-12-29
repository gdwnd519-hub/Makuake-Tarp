
import sys

# Set encoding to utf-8 for console output
sys.stdout.reconfigure(encoding='utf-8')

file_path = "c:\\Users\\clean\\OneDrive\\ドキュメント\\ウェブページ LP\\MAKUAKE タープ\\倉庫\\simulation_result.txt"

try:
    with open(file_path, 'r', encoding='utf-16') as f:
        print(f.read())
except Exception as e:
    # Try utf-16le specifically if generic utf-16 fails or try utf-8 just in case
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e2:
        print(f"Error reading file: {e}, {e2}")
