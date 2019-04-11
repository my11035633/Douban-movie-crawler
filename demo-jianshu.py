#requests模拟登陆

import requests
url="https://www.jianshu.com/sign_in"
data = {
    "telephone": "18021486042",
    "password": "11035633m"
}
headers={
    "Referer":"https://www.jianshu.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}
session=requests.session()
session.post(url, data=data,headers=headers)
headers2={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    "Referer":"https://www.jianshu.com/u/2ad1b4d95137"
}
response=session.get("https://www.jianshu.com/u/2ad1b4d95137",headers=headers2)
with open("jianshu.html","w",encoding="utf-8") as f:
    f.write(response.text)
