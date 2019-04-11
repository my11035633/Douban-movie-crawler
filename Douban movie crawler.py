from lxml import etree
import requests

#第一步：爬去所需要的html页面
url="https://movie.douban.com/cinema/nowplaying/suzhou/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    "Referer":"https://movie.douban.com/"
}
response=requests.get(url,headers=headers)
text=response.text        #自己帮我们解码，如果出现乱码，则自己response.content.decode("utf-8")

#第二步：调用xpath寻找所需要的数据
html=etree.HTML(text)     #文本需要通过etree变成对象，才可以调用xpath来找标签
ul=html.xpath("//ul[@class='lists']")[0]    #xpath返回的始终是列表：[数据]
lis=ul.xpath("./li")    #.表示当前标签下
positons=[]
for li in lis:
    name=li.xpath("@data-title")[0]     #@取出标签的属性值
    data_socre=li.xpath("@data-score")[0]
    address=li.xpath("@data-region")[0]
    director=li.xpath("@data-director")[0]
    actors=li.xpath("@data-actors")[0]
    image=li.xpath(".//img/@src")[0]     #//表示：全局；  /表示：根标签。 image不属于跟标签所以用//
    list={
        "name":name,
        "data_socre":data_socre,
        "address":address,
        "director":director,
        "actors":actors,
        "image":image
    }
    positons.append(list)
print(positons)

