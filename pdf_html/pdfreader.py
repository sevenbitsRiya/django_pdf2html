import cloudconvert
api = cloudconvert.Api('lU1MyU6xnPCeiF0qfW0da-buD3d1QS7dMkurLXdG4Q5pS6nJeiZHx-zzCoA1B-NOpdad-hMz4zgZjbwj8Sgf-Q')
 
process = api.convert({
    "inputformat": "pdf",
    "outputformat": "html",
    "input": "upload",
    "timeout": 10,
    "save": true,
    "file": open('inputfile.pdf', 'rb')
})
process.wait()
process.download()