# -*- coding: utf-8 -*-
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#pdf转img
#https://github.com/pymupdf/PyMuPDF
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 
import fitz
from operator import itemgetter
import os
 
 
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
 