import pefile
import PyPDF2
import zipfile
import os
import csv
from PIL import Image
from io import BytesIO
import json
from docx import Document
import openpyxl
from pptx import Presentation
from bs4 import BeautifulSoup
import sqlite3

# PE File 
def analyze_pe(file_path):
    try:
        pe = pefile.PE(file_path)
        imported_libraries = []
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            imported_libraries.append(entry.dll.decode())  # Decode from bytes to string
        return imported_libraries
    except Exception as e:
        print(f"An error occurred while analyzing PE file: {e}")
        return None

# PDF 
def analyze_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            metadata = reader.metadata
            return metadata
    except Exception as e:
        print(f"An error occurred while analyzing the PDF: {e}")
        return None

# ZIP File 
def analyze_zip(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_info = zip_ref.infolist()
            files = [info.filename for info in zip_info]
            return files
    except Exception as e:
        print(f"An error occurred while analyzing the ZIP file: {e}")
        return None

# Text File 
def analyze_txt(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content[:500]  # Return first 500 characters of content
    except Exception as e:
        print(f"An error occurred while analyzing the text file: {e}")
        return None

# Image (simple check for format)
def analyze_image(file_path):
    try:
        with Image.open(file_path) as img:
            img_format = img.format
            img_size = img.size
            return {"format": img_format, "size": img_size}
    except Exception as e:
        print(f"An error occurred while analyzing the image: {e}")
        return None

# CSV File 
def analyze_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            rows = list(csvreader)
            return {"rows_count": len(rows), "columns_count": len(rows[0]) if rows else 0}
    except Exception as e:
        print(f"An error occurred while analyzing the CSV file: {e}")
        return None

# Microsoft Word 
def analyze_word(file_path):
    try:
        doc = Document(file_path)
        paragraphs = [para.text for para in doc.paragraphs]
        return {"paragraph_count": len(paragraphs), "sample_text": paragraphs[:3]}  # Sample first 3 paragraphs
    except Exception as e:
        print(f"An error occurred while analyzing the Word file: {e}")
        return None

# Microsoft Excel 
def analyze_excel(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        rows = list(sheet.iter_rows(values_only=True))
        return {"rows_count": len(rows), "columns_count": len(rows[0]) if rows else 0}
    except Exception as e:
        print(f"An error occurred while analyzing the Excel file: {e}")
        return None

# Microsoft PowerPoint 
def analyze_ppt(file_path):
    try:
        ppt = Presentation(file_path)
        slide_count = len(ppt.slides)
        return {"slide_count": slide_count}
    except Exception as e:
        print(f"An error occurred while analyzing the PowerPoint file: {e}")
        return None

# JSON File 
def analyze_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return {"keys_count": len(data), "sample_data": str(data)[:100]}  # Sample first 100 chars
    except Exception as e:
        print(f"An error occurred while analyzing the JSON file: {e}")
        return None

# HTML File 
def analyze_html(file_path):
    try:
        with open(file_path, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            return {"title": title, "meta_description": soup.find('meta', attrs={'name': 'description'})}
    except Exception as e:
        print(f"An error occurred while analyzing the HTML file: {e}")
        return None

# SQLite Database 
def analyze_sqlite(file_path):
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return {"table_count": len(tables), "tables": [table[0] for table in tables]}
    except Exception as e:
        print(f"An error occurred while analyzing the SQLite database: {e}")
        return None

# Main File  Function
def analyze_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.exe' or file_extension == '.dll':
        return analyze_pe(file_path)
    elif file_extension == '.pdf':
        return analyze_pdf(file_path)
    elif file_extension == '.zip':
        return analyze_zip(file_path)
    elif file_extension == '.txt':
        return analyze_txt(file_path)
    elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        return analyze_image(file_path)
    elif file_extension == '.csv':
        return analyze_csv(file_path)
    elif file_extension == '.docx':
        return analyze_word(file_path)
    elif file_extension == '.xlsx':
        return analyze_excel(file_path)
    elif file_extension == '.pptx':
        return analyze_ppt(file_path)
    elif file_extension == '.json':
        return analyze_json(file_path)
    elif file_extension in ['.html', '.htm']:
        return analyze_html(file_path)
    elif file_extension in ['.sqlite', '.db']:
        return analyze_sqlite(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return None

# Example usage
file_path = input("Enter the full path to the file: ")
file_info = analyze_file(file_path)

if file_info:
    print("File Information:")
    if isinstance(file_info, dict):
        for key, value in file_info.items():
            print(f"{key}: {value}")
    elif isinstance(file_info, list):
        print("Files in ZIP Archive:")
        for file in file_info:
            print(file)
else:
    print("No information found or error occurred.")
