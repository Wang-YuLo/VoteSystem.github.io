import json
import cv2
import pytesseract

def verified(id,name,img,key):
    with open("data.json", 'r') as f:
        data = json.load(f)

    img = cv2.imread(img)
    y = img.shape[0]
    x = img.shape[1]
    y = y//10*6
    x = x//3*2
    img = img[y:, x:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)[1]
    img = cv2.medianBlur(img, 3)
    id = id.upper()
    if '605' in id:
        text = pytesseract.image_to_string(img, lang='eng')
        text = text.split('\n')
        for ele in text:
            if '605' in ele:
                cardId = ele.replace(" ", "")
                break
        if cardId != id:
            return False
        else:
            if id in data['data'].keys():
                return False
            else:
                data['data'][str(id)]={"name" : name , "password" : key}
                with open('data.json','w',encoding='utF8') as f:
                        json.dump(data,f,indent=4)
                return True
    else:
        return False


    
