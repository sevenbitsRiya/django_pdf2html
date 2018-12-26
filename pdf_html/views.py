from django.shortcuts import render
#import PyPDF2 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
#import unirest
# Create your views here.

def pdf_html(request):
    #pdfFileObj = open('static/pdf/Medical-Report-Free-Download-PDF-Template.pdf', 'rb') 
    #pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    #pageObj = pdfReader.getPage(0) 
    #page = pdfReader.numPages
    #data = pageObj.extractText()
    #pdfFileObj.close() 
    return render(request,'pdf_html/iframe.html')
'''
def pdf_html(request):
    # These code snippets use an open-source library. http://unirest.io/python
    response = unirest.post("https://netservice-convert-pdf-to-html-v1.p.mashape.com/api/documents/pdf2html.json",
    headers={
        "X-Mashape-Key": "ppGHqaZtQVmshmv5RrWBPke1CtL5p18g43jjsnLKOjB6sr4C6N",
        "X-BlackboxApiId": "3",
        "X-BlackboxApiToken": "Mashape"
    },
    params={
        "document": open("static/pdf/Medical-Report-Free-Download-PDF-Template.pdf", mode="r"),
        "dpi": 144,
        "embedCSS": true,
        "embedFont": true,
        "embedImage": true,
        "embedJavascript": true,
        "enableOutline": false,
        "zoom": 1.0
    }
    )
    return render(request,'pdf_html/iframe.html')'''