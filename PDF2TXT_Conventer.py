
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

NUMBER = 0

# File Location
file = r'C:\Users\M5025.pdf'

# Your output TXT name 
Output_Name=""

def convert_pdf(path, page=1):
    global NUMBER
    
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, pageno=page, laparams=laparams)

    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    article = retstr.getvalue()
    retstr.close()
    
    fptr = open(Output_Name,'w',encoding = 'utf8')
    fptr.write(article)
    fptr.close()




            
convert_pdf(file)


