import requests
import json

#이미지 파일 저장 function

def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    
    if img_response.status_code == 200:    
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

#이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {"Authorization" : "KakaoAK a95f015df1177dc4f1bd06f1136400d6"}
data = {"query" : "손흥민"}

#이미지 검색요청

response = requests.post(url, headers=headers, data= data)

# requests fail
if response.status_code != 200:
    print("error! because", response.json())
else:
    count = 0
    for image_info in response.json()['documents']:
        print("[%dth] image_url) = " %count, image_info['image_url'])
        file_name = "test_%d.jpg" %(count)
        count = count + 1
        save_image(image_info['image_url'], file_name)

