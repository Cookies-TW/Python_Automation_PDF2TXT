
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO



NUMBER = 0

# File Location
file = r'/Users/PETERHAO/Desktop/ga-I572469.pdf'

# Your output TXT name 
Output_Name="/Users/PETERHAO/Desktop/M0.txt"
Patent_Name="/Users/PETERHAO/Desktop/M1.txt"

def convert_pdf(path, page=1):
    global NUMBER
    
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, pageno=page, laparams=laparams)

    fp = open(path, 'rb')
    print(fp.readline())
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    article = retstr.getvalue().encode('big5')
    retstr.close()
    print(article)
    fptr = open(Output_Name,'w',encoding = 'utf8')
    fptr.write(article)
    fptr.close()

def text_exeraction():
    locker = False

    ftpr = open(Output_Name,encoding = 'UTF-8')
    p = open(Patent_Name,'w',encoding = 'utf8')
    line = ftpr.readline()
    while line:


        if locker is True:
            p.writelines(line)
        line = ftpr.readline()

    ftpr.close()
    p.close()







            
convert_pdf(file)
text_exeraction()


