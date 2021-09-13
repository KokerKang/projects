
"""
    writing file
"""

# 파일 안 쓰고 싶은 내용을 변수에 넣기
data = "hello"

# test.txt를 w(write) 쓰기 모드로 열고, 파일 디스크립터를 fp 변수에 담고, 
with open("test.txt", "w") as fp:
    # data 값을 쓰기 위해, write 함수를 호출
    fp.write(data)

# reading file
# test.txt를 r(reading) 읽기 모드로 열고, 파일 디스크립ㅂ터를 fp 변수에 담고,
with open("test.txt", "r") as fp:
    print("======[The result of reading file]======")
    #파일 내용을 읽기 위해, read 함수를 호출
    print(fp.read())


# 라이브러리를 import
import requests

# 이미지가 있는 url 주소
url = "https://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

# 해당 url 로 서버에게 요청
img_response = requests.get(url)

# 요청에 성공,
if img_response.status_code == 200:
    #print(img_response.content)
    
    print("이미지 저장")
    #test.jpg 파일을 wb(writing binary) 바이너리 형식을 쓰는 모드를 열고 fp변수에 저장
    with open("test.jpg", "wb") as fp:
        # write 함수를 호출하여, 이미지에 해당하는 img_response.content를 저장
        fp.write(img_response.content)




