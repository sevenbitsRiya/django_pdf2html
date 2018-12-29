from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import cloudconvert
from django.http import HttpResponseRedirect
from django.shortcuts import render

from urllib.request import urlopen 
from urllib.error import HTTPError 
from urllib.error import URLError
from bs4 import BeautifulSoup
 

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def pdf_html(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        api = cloudconvert.Api('TrStC9PsjG9GrI7Fqbo1S1wtqYmDU9HE9HZiBUAJYnXEf127aNk9GFmIXII8iqHA')
        #print(name)
        process = api.convert({
            "inputformat": "pdf",
            "outputformat": "html",
            "input": "upload",
            "filename": "riya.pdf",
            "file": open('/home/sevenbits/pro/project/myproject/media/'+name, 'rb')
        })
        process.wait()
        process.download()
        tags = []
        try:
            html = open('/home/sevenbits/pro/project/myproject/riya.html')
        except HTTPError as e:
            print(e)
        except URLError:
            print("Server down or incorrect domain")
        else:
            res = BeautifulSoup(html.read(), "html5lib")
            for tag in res.find_all('div', {"id":"pf1"}):
                DAA = tag.find('div',{'class':'t m0 x4 h3 y9 ff1 fs0 fc0 sc0 ls1 ws0'}).find('span',{'class':'ls0'}).get_text()
                wm = tag.find('div',{'class':'c x1 yf w2 h4'}).find('span', {'class':'ls0'}).get_text()
                context = {DAA:'DAA',wm:'wm'}
                print(context)
                return render(request, 'pdf_html/iframe.html', context)  
                
    return render(request, 'pdf_html/iframe.html')  

 