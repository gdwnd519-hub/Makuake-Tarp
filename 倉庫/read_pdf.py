import re
import sys

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
            
        # Very basic text extraction for unencrypted PDFs
        # This looks for text between parentheses (...) or distinct text streams
        # It's a fallback if no PDF libraries are available
        text_content = []
        
        # Look for text streams in BT (Begin Text) ... ET (End Text) blocks
        # This is not perfect but might catch the main content
        objects = re.findall(b'BT(.*?)ET', content, re.DOTALL)
        
        for obj in objects:
            # Extract text within parentheses
            txt = re.findall(b'\((.*?)\)', obj)
            for t in txt:
                try:
                    # Try to decode common encodings
                    decoded = t.decode('utf-8', errors='ignore')
                    text_content.append(decoded)
                except:
                    pass
        
        # Also try to just find all text-like strings if the above fails to find much
        if len(text_content) < 5:
            print("Standard extraction yielded little text, trying raw string extraction...")
            # specific to this case, maybe we can just dump strings
            strings = re.findall(b'[a-zA-Z0-9\s\.\,\-\:\%\@\u3000-\u30ff\u4e00-\u9faf]+', content)
            text_content = [s.decode('utf-8', errors='ignore') for s in strings if len(s) > 3]

        return "\n".join(text_content)

    except Exception as e:
        return f"Error reading PDF: {str(e)}"

pdf_path = r"c:\Users\clean\OneDrive\ドキュメント\ウェブページ LP\MAKUAKE タープ\デュアルポール防水キャノピーの詳細.pdf"
print(f"Reading: {pdf_path}")
text = extract_text_from_pdf(pdf_path)
print("--- START TEXT CONTENT ---")
print(text)
print("--- END TEXT CONTENT ---")
