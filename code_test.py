import urllib.request

url ='https://openapi.naver.com/v1/search/news.json?query="bts"%start=1&display=100'
client_id = "FHNJ2I7ZTmp1s8EYyIpf"
client_secret = "BoDoQtg7zU"

req = urllib.request.Request(url)  # 네이버서버에 보낼 요청객체를 생성
req.add_header("X-Naver-Client-Id", client_id)  # 위에서 만들어진 요청객체에 client_id를 포함시킴
req.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(req)  # 네이버서버에 요청객체 req를 전달하여 응답을 받아 response에 저장
print(response) # 에러코드출력, 200-정상 호출 및 승인

ret = response.read().decode('utf-8')
print(ret)