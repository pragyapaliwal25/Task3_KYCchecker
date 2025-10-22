import pytesseract
import cv2
from fuzzywuzzy import fuzz
import re
import streamlit as st
import numpy as np


st.title("🪪 Smart KYC Checker")
st.write("Upload your Aadhar and PAN card images to automatically extract and verify details.")


def extract_text_from_upload(uploaded_file):
    """Extract text using OCR from uploaded image"""
    if uploaded_file is None:
        return ""
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def parse_aadhar(text):
    """Extract Name, DOB, and Aadhar Number"""
    name_match = re.search(r"Name\s*:\s*(.+)", text, re.IGNORECASE)
    dob_match = re.search(r"DOB\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    id_match = re.search(r"(\d{4}\s\d{4}\s\d{4})", text)

    name = name_match.group(1).strip() if name_match else "Not found"
    dob = dob_match.group(1) if dob_match else "Not found"
    aadhar_id = id_match.group(1) if id_match else "Not found"
    return {"Name": name, "DOB": dob, "Aadhar_ID": aadhar_id}

def parse_pan(text):
    """Extract Name and PAN Number"""
    name_match = re.search(r"Name\s*:\s*(.+)", text, re.IGNORECASE)
    pan_match = re.search(r"([A-Z]{5}[0-9]{4}[A-Z])", text)

    name = name_match.group(1).strip() if name_match else "Not found"
    pan_id = pan_match.group(1) if pan_match else "Not found"
    return {"Name": name, "PAN_ID": pan_id}

#I have used streamlit just for little ui

aadhar_file = st.file_uploader("📎 Upload Aadhar Card", type=["png", "jpg", "jpeg"])
pan_file = st.file_uploader("📎 Upload PAN Card", type=["png", "jpg", "jpeg"])

if st.button(" Run KYC Check"):
    if aadhar_file and pan_file:
        
        aadhar_text = extract_text_from_upload(aadhar_file)
        pan_text = extract_text_from_upload(pan_file)

        #Parse info
        aadhar_info = parse_aadhar(aadhar_text)
        pan_info = parse_pan(pan_text)

        #  Fraud check
        name_similarity = fuzz.ratio(aadhar_info["Name"].lower(), pan_info["Name"].lower())

        # Results
        st.success(" Extraction Complete!")

        st.subheader("Aadhar Details")
        st.json(aadhar_info)

        st.subheader("PAN Details")
        st.json(pan_info)

        st.subheader(" Fraud Check")
        st.write(f"**Name similarity:** {name_similarity}%")

        if name_similarity > 85:
            st.success("Names Match — likely same person")
        else:
            st.error("Names do not match! Possible mismatch.")
    else:
        st.warning("Please upload both Aadhar and PAN images first.")


