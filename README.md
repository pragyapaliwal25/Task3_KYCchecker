# 🪪 Smart KYC Checker

### 👩‍💻 Developed by: Pragya Paliwal

---

## 📘 About the Project
**Smart KYC Checker** is an AI-powered verification tool that automates KYC validation.  
It extracts essential details from **Aadhar** and **PAN** card images using OCR and performs a **fraud check** by comparing the names on both documents.  
The system is built using **Python**, **OpenCV**, **Tesseract**, and **Streamlit** for an interactive web-based interface.

---

## ⚙️ Features
- 🧠 Optical Character Recognition (OCR) for reading document text  
- 📄 Auto-parsing of Aadhar & PAN details  
- 🔍 Fuzzy name matching to detect fraud or mismatched documents  
- 💻 Streamlit interface for image uploads and results  
- ⚡ Lightweight and easy to use

---

### 🧠 Tech Stack
- **Language:** Python  
- **Libraries:** `pytesseract`, `opencv-python`, `streamlit`, `re`  
- **Interface:** Streamlit  
- **IDE Used:** VS Code  

---

### 🧩 How It Works
1. **Upload Documents:** The user uploads images of PAN or Aadhar cards.  
2. **Preprocessing:** The images are converted to grayscale and cleaned to improve text extraction.  
3. **Text Extraction:** OCR reads text from the image using Tesseract.  
4. **Validation:** Extracted data is matched against PAN/Aadhar formats using regex.  
5. **Output:** The system displays whether the document is valid or needs correction.

---

### 🚀 Run the Project Locally
1. Clone the repository  
   ```bash
   git clone https://github.com/pragyapaliwal25/Task3_KYCchecker.git
   cd Task3_KYCchecker
   
2. Create a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   ```bash
   pip install -r requirements.txt   

4. Run the Streamlit app
   ```bash
   streamlit run kyc_checker.py

---

📊 Sample Output

Document Type | File Name             | Result
---------------|----------------------|---------
Aadhar         | sample-aadhar.png    | ✅ Valid Aadhar detected
PAN            | sample-pan-card.jpg  | ✅ Valid PAN detected
Random Image   | random-text.png      | ⚠️ Invalid document

💡 Timestamped logs and success messages are displayed in the Streamlit app.

---

🔮 Future Scope

1.Add support for more document types (Passport, Voter ID, etc.).

2.Deploy online using Streamlit Cloud or Render.

3.Improve OCR accuracy using AI/ML models.

4.Add database support for saving verification logs.

---

🧑‍💻 Author

Pragya Paliwal

📍 Student Project – Automated KYC Verification using Python

