
import pandas as pd
import openpyxl
import sys

# Set encoding to utf-8 for console output
sys.stdout.reconfigure(encoding='utf-8')

file_path = "c:\\Users\\clean\\OneDrive\\ドキュメント\\ウェブページ LP\\MAKUAKE タープ\\OMP 利益予測＆リターン計算表 のコピー.xlsx"
output_file = "c:\\Users\\clean\\OneDrive\\ドキュメント\\ウェブページ LP\\MAKUAKE タープ\\excel_dump.txt"

try:
    with open(output_file, 'w', encoding='utf-8') as f:
        df = pd.read_excel(file_path, sheet_name=None)
        for sheet_name, sheet_df in df.items():
            f.write(f"\n--- Sheet: {sheet_name} ---\n")
            # Fill NaN with empty string for better readability
            sheet_df = sheet_df.fillna('')
            f.write(sheet_df.to_string())
    print(f"Successfully wrote to {output_file}")
except Exception as e:
    print(f"Error reading excel: {e}")
