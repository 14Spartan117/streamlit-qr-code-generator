#Streamlit app for QR Code generator
#To run, go to command line and run:
# streamlit run this_filename.py
#Must first run pip install streamlit if needed

import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
from pathlib import Path

#Path to the Army logo (same directory as this script)
ARMY_LOGO = Path(__file__).parent / "army_logo.png"

#Add title
st.title('QR Code Generator :rocket:')

#Add App description
with st.expander("App Description"):
    st.write("""
    This app allows you to generate QR Codes for any url or any text string you want to encode.  QR Codes are generated using the [qrcode](https://pypi.org/project/qrcode/) python package.
    
    POC: Brandon Delarosa, brandon.delarosa@nps.edu
    """)

#Add text input
text = st.text_input(label='Enter Text or URL to encode as QR Code')

# Encoding data using qrcode.QRCode for more control
if text:
    #Use high error correction so the QR code still scans with the Army logo overlay
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    #Embed the Army logo in the center of the QR code
    logo = Image.open(ARMY_LOGO).convert("RGBA")
    qr_w, qr_h = qr_img.size
    #Logo takes up ~30% of QR code (max safe size for scanning)
    logo_max = int(qr_w * 0.3)
    logo.thumbnail((logo_max, logo_max), Image.LANCZOS)
    #Paste logo in the center
    pos = ((qr_w - logo.size[0]) // 2, (qr_h - logo.size[1]) // 2)
    qr_img.paste(logo, pos, logo)

    #Save QR code to a BytesIO buffer as PNG
    buf = BytesIO()
    qr_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    #Display the QR Code in the app
    st.write(f'QR Code generated for {text}:')
    st.image(byte_im)

    st.download_button(label='Download QR Code',
                             data=byte_im,
                             file_name='qrcode.png')
