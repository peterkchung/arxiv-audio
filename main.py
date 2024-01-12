import requests
import pdfplumber
from io import BytesIO


def extract_text_from_pdf():
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BytesIO object from the response content
    pdf_file = BytesIO(response.content)

    # Load PDF with pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        # Initialize an empty string to hold the text
        text = ""

        # Loop through each page and extract the text
        for page in pdf.pages:
            text += page.extract_text()

    return text

url = "https://arxiv.org/pdf/2312.00752.pdf"
extracted_text = extract_text_from_pdf(url)




if __name__ == "__main__":
    
    """
    function execute here
    
    """
