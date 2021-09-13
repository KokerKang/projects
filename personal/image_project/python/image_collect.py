import requests
import json


def save_image(url, file_name):
    img_response = requests.get(url)

    if img_response.status_code == 200:
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

url = "https://dapi.kakao.com/v2/search/image"
header = {"Authorization" : "KakaoAK a95f015df1177dc4f1bd06f1136400d6"}
data = {"query" : "유재석"}

response = requests.post(url, headers=header, data=data)

if response.status_code != 200:
    print("error because : ", response.json())
else:
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count} th] image_url = ", image_info['image_url'])

        count = count + 1
        file_name = "test_%d.jpg" %(count)
        save_image(image_info['image_url'], file_name)