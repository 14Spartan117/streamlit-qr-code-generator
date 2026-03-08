# U.S. Army QR Code Generator

A Streamlit web app that generates QR codes with the U.S. Army logo embedded in the center. Enter any URL or text, and the app produces a scannable, branded QR code ready to download.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)

## Features

- **Branded QR Codes** — Every QR code includes the U.S. Army star logo in the center
- **High Error Correction** — Uses QR error correction level H (30%), ensuring codes scan reliably even with the logo overlay
- **Instant Download** — One-click download of the generated QR code as a PNG
- **Simple Interface** — Just type a URL or text and the QR code is generated instantly

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
# Clone the repo
git clone https://github.com/14Spartan117/streamlit-qr-code-generator.git
cd streamlit-qr-code-generator

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run streamlit_QR_app.py
```

The app will open in your browser at `http://localhost:8501`.

## How It Works

1. User enters a URL or text string
2. The app generates a QR code using the `qrcode` library with error correction level H
3. The U.S. Army logo is resized to 30% of the QR code and pasted in the center
4. The final image is displayed in-app and available for download as PNG

## Project Structure

```
├── streamlit_QR_app.py   # Main Streamlit application
├── army_logo.png         # U.S. Army logo image
├── requirements.txt      # Python dependencies
└── README.md
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web app framework |
| `qrcode` | QR code generation |
| `Pillow` | Image processing and logo overlay |

## Author

**Brandon Delarosa** — brandon.delarosa@nps.edu
