from django.http import HttpResponse,JsonResponse
import json
import fitz
import time
from operator import itemgetter
import os

def hello(request):
    return HttpResponse("hello world!")

def pdfToImg(request):
    request.encoding = 'utf-8'
    filePath = request.GET['filePath']
    outPath = request.GET['outPath']
    data = {
        'code': 0,
        'msg': '调用成功',
        'outPath': outPath
    }
    try:
        startTime = time.time()
        imgPath = pdf_to_image('I:\pdf\stest.pdf', outPath)
        endTime = time.time()
        timeSpan =endTime - startTime 
        data["time"] = round(timeSpan, 5)
    except ZeroDivisionError as e:
        data = {
            'code': 500,
            'msg': e
        }
    #json包含中文问题
    return JsonResponse(data,
                        safe=False,
                        json_dumps_params={'ensure_ascii':False})

# 将pdf转换为图片
def pdf_to_image(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        pix = page.getPixmap(alpha=False)          # 默认是720*x尺寸
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        pix.writePNG(imagePath+'/'+'images_%s.jpg' % pg)     #将图片写入指定的文件夹内
    return imagePath
 