
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO



NUMBER = 0

# File Location
file = r'/Users/PETERHAO/Desktop/ga-I572441.pdf'

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
    #print(fp.readline())
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    article = retstr.getvalue()
    retstr.close()
    #print(article)
    fptr = open(Output_Name,'w',encoding = 'utf8')
    fptr.write(article)
    fptr.close()

def more_clear(line):
    """刪去頁碼與標號"""
    if line[0] is '(' or line[1] is '(': #  (2)
        return False
    elif line[0] is '-' and line[1] is ' ': # pages
        return False
    elif line[0] is '\n': # 空行
        return False
    else:
        return True

def text_exeraction():
    locker = False

    ftpr = open(Output_Name,encoding = 'UTF-8')
    p = open(Patent_Name,'w',encoding = 'utf8')
    line = ftpr.readline()

    # 擷取專利範圍
    while line:
        if line.find("圖式簡單說明") is not -1:
            break

        if locker is True:
            if more_clear(line) is True:
                p.writelines(line)
        if line.find("[57]申請專利範圍") is not -1:
            locker = True

        line = ftpr.readline()
    
    ftpr.close()
    p.close()







            
convert_pdf(file)
text_exeraction()
print("Successful.")


