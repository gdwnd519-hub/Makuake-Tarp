import email
import os
import base64

eml_path = r"c:\Users\clean\OneDrive\ドキュメント\ウェブページ LP\MAKUAKE タープ\メールアドレスの確認.eml"
output_dir = r"c:\Users\clean\OneDrive\ドキュメント\ウェブページ LP\MAKUAKE タープ"

with open(eml_path, 'rb') as f:
    msg = email.message_from_binary_file(f)

for part in msg.walk():
    if part.get_content_maintype() == 'multipart':
        continue
    if part.get('Content-Disposition') is None:
        continue
        
    filename = part.get_filename()
    if filename:
        # Decode filename if necessary (it looked like it was mime encoded in the view_file output)
        from email.header import decode_header
        decoded_header = decode_header(filename)
        filename = ""
        for dh in decoded_header:
            fname, encoding = dh
            if isinstance(fname, bytes):
                filename += fname.decode(encoding or 'utf-8')
            else:
                filename += fname
                
        print(f"Found attachment: {filename}")
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'wb') as f_out:
            f_out.write(part.get_payload(decode=True))
        print(f"Saved to: {filepath}")
