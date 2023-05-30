import PyPDF2
import re

pdf_url = 'https://arxiv.org/pdf/hep-lat/9211031v1.pdf'

# If the PDF is accessible online
# pdf_file = PyPDF2.PdfReader(pdf_url, 'rb')

# If the PDF is stored locally
 pdf_file = PyPDF2.PdfReader(open('../data/9211031.pdf', 'rb'))
