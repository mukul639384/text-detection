import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img=cv.imread('1.JPG')
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))  # o/p-->raw data/string from image
# print(pytesseract.image_to_boxes(img))   # o/p--->each char with diagonal coordinate

# DETECTING CHAR
# hImg,wImg,_=img.shape
# boxes=pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b=b.split(' ')
#     print(b)
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
#     cv.putText(img,b[0],(x,hImg-y+25),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255))

# DETECTING WORD
# hImg,wImg,_=img.shape
# boxes=pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#             cv.putText(img,b[11],(x,y),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255))

# DETECTING only digits as WORD (by adding config)
# hImg,wImg,_=img.shape
# cong=r'--oem 3 --psm 6 outputbase digits'
# boxes=pytesseract.image_to_data(img,config=cong)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#             cv.putText(img,b[11],(x,y),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255))

# DETECTING CHAR
hImg,wImg,_=img.shape
cong=r'--oem 3 --psm 6 outputbase digits'
boxes=pytesseract.image_to_boxes(img,config=cong)
for b in boxes.splitlines():
    b=b.split(' ')
    print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
    cv.putText(img,b[0],(x,hImg-y+25),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255))

cv.imshow('result',img)
cv.waitKey(0)