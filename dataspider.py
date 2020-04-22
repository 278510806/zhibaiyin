import requests
from lxml import etree
import time
from enum import Enum


class metal_type(Enum):
    '''
    贵金属类型
    '''
    # 人民币黄金
    RMB_GOLD = "rmb_gold"
    # 人民币白银
    RMB_SIVLER = "rmb_sivler"
    # 人民币铂金
    RMB_PLATINUM = "rmb_platinum"
    # 人民币钯金
    RMB_PORPEZITE = "rmb_porpezite"
    # 美元黄金
    USD_GOLD = "usd_gold"
    # 美元白银
    USD_SILVER = "usd_silver"
    # 美元铂金
    USD_PLATINUM = "usd_platinum"
    # 美元钯金
    USD_PORPEZITE = "usd_porpezite"


def save_data(mtype, tr):
    try:
        bank_buy = tr.xpath(".//td[3]/text()")[0].strip()
        bank_sell = tr.xpath(".//td[4]/text()")[0].strip()
        bank_middle = tr.xpath(".//td[5]/text()")[0].strip()
        bank_Highest = tr.xpath(".//td[6]/text()")[0].strip()
        bank_Lowest = tr.xpath(".//td[7]/text()")[0].strip()
        record_dt = time.strftime("%Y-%m-%d %H:%M:%S")
        file_dt = time.strftime("%Y-%m-%d")
        with open(mtype.value + "_" + file_dt + ".csv", "a", encoding="utf-8") as f:
            f.write(
                bank_buy + "," + bank_sell + "," + bank_middle + "," + bank_Highest + "," + bank_Lowest + "," + record_dt)
            f.write("\n")
    except Exception as e:
        print(e)
    else:
        print(
            "写入文件：" + mtype.value + "_" + file_dt + ".csv " + bank_buy + "，" + bank_sell + "，" + bank_middle + "," + bank_Highest + "," + bank_Lowest + "," + record_dt)

url = "http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}


def get_data():
    resp = requests.get(url, headers=headers)

    html = resp.content.decode()

    root = etree.HTML(html)
    trs = root.xpath("//table[@id='TABLE1']//tr")
    rmb_gold = trs[1]
    rmb_silver = trs[2]
    rmb_platinum = trs[3]
    rmb_porpezite = trs[4]
    dollar_gold = trs[5]
    dollar_silver = trs[6]
    dollar_platinum = trs[7]
    dollar_porpezite = trs[8]
    save_data(metal_type.RMB_GOLD, rmb_gold)
    save_data(metal_type.RMB_SIVLER, rmb_silver)
    save_data(metal_type.RMB_PLATINUM, rmb_platinum)
    save_data(metal_type.RMB_PORPEZITE, rmb_porpezite)
    save_data(metal_type.USD_GOLD, dollar_gold)
    save_data(metal_type.USD_SILVER, dollar_silver)
    save_data(metal_type.USD_PLATINUM, dollar_platinum)
    save_data(metal_type.USD_PORPEZITE, dollar_porpezite)


if __name__ == "__main__":
    while True:
        get_data()
        time.sleep(60)
