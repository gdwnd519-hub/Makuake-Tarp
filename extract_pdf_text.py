
import sys
import os

try:
    import pypdf
    print(f"Using pypdf version: {pypdf.__version__}")
    def get_text(path):
        reader = pypdf.PdfReader(path)
        print(f"Number of pages: {len(reader.pages)}")
        text = ""
        for i, page in enumerate(reader.pages):
            print(f"--- Page {i+1} ---")
            try:
                page_text = page.extract_text(extraction_mode="layout")
            except:
                page_text = page.extract_text()
            print(page_text)
            text += page_text + "\n"
        return text
except ImportError:
    print("pypdf not found")
    sys.exit(1)

file_path = r"c:\Users\clean\OneDrive\ドキュメント\ウェブページ LP\MAKUAKE タープ\Exclusive_Distribution_Agreement_DoublePoleTarp_JA_B (1).pdf"

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    sys.exit(1)

try:
    content = get_text(file_path)
except Exception as e:
    print(f"Error reading PDF: {e}")
