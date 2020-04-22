import requests
import time
from lxml import etree
# 1盎司合多少克
oz=28.35
# 计算美元兑人民币汇率
def compute_rate():
    url="https://srh.bankofchina.com/search/whpj/search_cn.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
    }
    data={
    "erectDate":None,
    "nothing": None,
    "pjname": "美元",
    "head": "head_620.js",
    "bottom": "bottom_591.js"
    }
    resp=requests.get(url,params=data,headers=headers)
    #print(resp.content.decode())
    dt=time.strftime("%Y-%m-%d-%H-%M-%S")
    with open(dt+".html","w",encoding="utf-8") as f:
        f.write(resp.content.decode())
    with open(dt+".html","r",encoding="utf-8") as f:
        html=f.read()
        root=etree.HTML(html)
        first_tr=root.xpath("//table//tr[2]/td[2]/text()")[0]
        # 美元兑人民币汇率：1美元=x元人民币
        rate=float(first_tr)/100
        print("美元兑人民币汇率："+str(rate))
        return rate
        #return dollar_per_oz*rate/oz
# 美元/盎司转元/克
def conversion_dollar_per_oz_to_rmb_per_g(dollar_per_oz):
    return dollar_per_oz * compute_rate() / oz
if __name__=="__main__":
    str_dollar_per_oz=input("请输入：")
    dollar_per_oz=float(str_dollar_per_oz)
    result=conversion_dollar_per_oz_to_rmb_per_g(dollar_per_oz)
    print(str_dollar_per_oz+"美元/盎司合"+str(round(result,2))+"元/克")