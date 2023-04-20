import pyttsx3
import PyPDF2

pdf=open('AudioBook/book.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdf)
n=pdfReader.numPages
print(n)
speaker=pyttsx3.init()
speaker.setProperty('rate',120)
for num in range(0,n):
    page=pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()