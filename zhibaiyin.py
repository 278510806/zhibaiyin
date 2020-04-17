import requests
import time
from lxml import etree
# url="https://srh.bankofchina.com/search/whpj/search_cn.jsp"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
# }
# data={
# "erectDate":None,
# "nothing": None,
# "pjname": "美元",
# "head": "head_620.js",
# "bottom": "bottom_591.js"
# }
# resp=requests.get(url,params=data,headers=headers)
# #print(resp.content.decode())
# dt=time.strftime("%Y-%m-%d-%H-%M-%S")
# with open(dt+".html","w",encoding="utf-8") as f:
#     f.write(resp.content.decode())
# time.sleep(3)
with open("2020-04-15-15-08-52.html","r",encoding="utf-8") as f:
    html=f.read()
    root=etree.HTML(html)
    first_tr=root.xpath("//table//tr[2]/td[2]/text()")[0]
    print(float(first_tr)/100)