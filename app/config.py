from PIL import Image
from pypdf import PdfReader
from pdfminer.high_level import extract_text
import pytesseract
import os
from docx import Document

path = input("Add Resume: ")

def pdfscan(path):
    def extract_pypdf():
        readPDF = PdfReader(path)
        text = []
        for page in readPDF.pages:
            page_text = page.extract_text() or ""
            text.append(page_text)
            return "\n".join(text)
    def extract_pdfminer():
        return extract_text(path) or ""
    # return extract_pdfminer()
    # return extractPypdf()
    def merge_texts(t1, t2):
        if len(t2.strip()) > len(t1.strip()):
            return t2
        elif len(t1.strip()) > 0:
            return t1
        else:
            return t2
    txt_pypdf = extract_pypdf()
    txt_pdfminer = extract_pdfminer()
    txt_combined = merge_texts(txt_pypdf, txt_pdfminer)
    print("---------------PDF EXtracted Text-----------------")     
    return txt_combined
# scanTxt = pdfscan(path)
# print(pdfscan(path))

def docscan(path):
    doc = Document(path)
    print("---------------Doc EXtracted Text-----------------")
    for para in doc.paragraphs:
        print(para.text)
        # return para.text
    return ""
# extract_doc = 
# print(docscan(path))

def imgscan(path):
    img = Image.open(path)
    txt_img = pytesseract.image_to_string(img, lang="eng")
    print("---------------Image EXtracted Text-----------------")
    return txt_img
# pytesseract.image_to_string(r"C:\Users\utkar\OneDrive\Documents\Project\ResuIQ\ResuIQ\data\samples\Priya_Desai_Resume.jpg")
# print(imgscan(path))
# import os
# filepath = input("Enter the file Path: ")
ext = os.path.splitext(path)[1].lower()
# print("Extension: ",ext)

if ext in ['.jpeg', '.jpg', '.png']:
    print(imgscan(path))
elif ext == '.pdf':
    print(pdfscan(path))
elif ext in ['.doc','.docx']:
    print(docscan(path))
else:
    print("not working")