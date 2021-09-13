import requests
import json




def save_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as fp:
            fp.write(response.content)


url = "https://dapi.kakao.com/v2/search/image"
data = {
    "query" : "재석"
}

header = {
    "Authorization" : "KakaoAK a95f015df1177dc4f1bd06f1136400d6"
}

response = requests.post(url, headers=header, data=data)

if response.status_code != 200:
    print("Error : ", response.json())

else:
    count = 0
    for image_info in response.json()['documents']:
        count += 1
        print("[%d th url] :" %count, image_info['image_url'])
        file_name = "test_%d.jpg" %count
        print(file_name)
        save_image(image_info['image_url'], file_name)
        if count == 5:
            break