from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import cloudconvert
from django.http import HttpResponseRedirect
from urllib.error import HTTPError 
from urllib.error import URLError
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from bs4 import SoupStrainer
import csv
from django.shortcuts import render_to_response


def pdf_html(request):
    try:
        html = open('/home/sevenbits/pro/project/myproject/riya.html')     
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        if request.method == 'POST':
            uploaded_file = request.FILES['myfile']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            url = fs.url(name)
            uploaded_file_url = fs.url(name)
            api = cloudconvert.Api('TrStC9PsjG9GrI7Fqbo1S1wtqYmDU9HE9HZiBUAJYnXEf127aNk9GFmIXII8iqHA')
            process = api.convert({
                "inputformat": "pdf",
                "outputformat": "html",
                "input": "upload",
                "filename": "riya.pdf",
                "file": open('/home/sevenbits/pro/project/myproject/media/'+name, 'rb')
            })
            process.wait()
            process.download()
            html = open('/home/sevenbits/pro/project/myproject/riya.html')   
            context = {}
            tag = []
            only_div_tags = SoupStrainer("div") 
            #res = BeautifulSoup(html, "html.parser", parse_only=only_div_tags).prettify()
            res = BeautifulSoup(html.read(), "html5lib")
            tag = res.find_all('div', {"id":"pf1"})
            header = res.find('div', {'class': "c x1 y1 w2 h2"})
            name = res.find('div', {'class':"t m0 x2 h5 y1b ff1 fs1 fc0 sc0 ls0 ws0"})
            hemoglobin = res.find('div', {'class': 't m0 x12 h9 y22 ff2 fs3 fc0 sc0 ls0 ws0'})
            hemoglobin_cnt = res.find('div', {'class': 't m0 x13 h9 y23 ff2 fs3 fc0 sc0 ls0 ws0'})
            pcv = res.find('div', {'class': 't m0 x12 h9 y24 ff2 fs3 fc0 sc0 ls0 ws0'}).get_text()
            pcv_cnt = res.find('div', {'class': 't m0 x13 h9 y25 ff2 fs3 fc0 sc0 ls0 ws0'}).get_text()
            print(pcv)
            #para2 = res.find_all('div',{'class':'c x4 y8 w4 h6'})
            
            #print(para2)
            #DAA = tag.find('div',{'class':'c x1 y1 w2 h2'}).get_text()
                #DAA = tag.find('div',{'class':'t m0 x4 h3 y9 ff1 fs0 fc0 sc0 ls1 ws0'}).find('span',{'class':'ls0'}).get_text()
                #wm = tag.find('div',{'class':'c x1 yf w2 h4'}).find('span', {'class':'ls0'}).get_text()
            #tagg = tag.prettify(formatter="html")print(tag)
            
            fp = open('/home/sevenbits/pro/project/myproject/media/res.html', 'w')
            uploaded_file_url1 = "/media/res.html"
            header1 = ''.join(map(str,header))
            tag1 = ''.join(map(str, name))
            hemoglobin1 = ''.join(map(str,hemoglobin)) 
            hemoglobin2 = ''.join(map(str,hemoglobin_cnt)) 
            #pcv1 = ''.join(map(str,pcv)) 
            #pcv2 = ''.join(map(str,pcv_cnt)) 
            
           # para_2 = ''.join(map(str, para2)) 
           # context = {'header1':header1,'tag1':tag1,'para1':para1}   
            
            html = tag1
            html += "\n"
            html += hemoglobin1
            html += hemoglobin2
            #html += pcv
            #html += pcv_cnt
            
            #html += para_2
            fp.write(html)
            #with open('riyacsv.csv','w') as csvfile:
                #fielnames = []


            fp.close()
            return render(request,'pdf_html/iframe.html',{
                'uploaded_file_url': uploaded_file_url,
                'uploaded_file_url1': uploaded_file_url1,
            })
              
    return render(request, 'pdf_html/iframe.html')            
    
