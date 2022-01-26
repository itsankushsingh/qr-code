from django.shortcuts import render
from django.http import HttpResponse

from pyqrcode import *
import png
data = None


def testing(request):
    global data
    if request.method == 'POST':
        data = request.POST.get('data')
        img = create(data)
        img.png("static/image/qrcode.png", scale=12)
        img.svg("static/image/qrcode.svg", scale=8)
    else:
        pass
    return render(request, 'index.html', {'data': data})
