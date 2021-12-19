#spidermusic.py
import time
import xlwt
import csv
import requests
from lxml import etree

#初始化保存列表
list_music = []
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
# 爬取的内容保存在csv文件中
f = open(r"E:\dbspider\doubanmusic.csv", "w+", newline='', encoding="utf-8")
writer = csv.writer(f, dialect='excel')
# csv文件中第一行写入标题
writer.writerow(["song", "singer", "time", "kind", "score", "comments"])


# 定义爬取内容的函数
def music_info(url):
    resp = requests.get(url, headers=headers)
    selector = etree.HTML(resp.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        song = info.xpath('td[2]/div/a/text()')[0].strip()
        singer = info.xpath('td[2]/div/p/text()')[0].split("/")[0]
        times = info.xpath('td[2]/div/p/text()')[0].split("/")[1]
        kind = info.xpath('td[2]/div/p/text()')[0].split("/")[-1]
        score = info.xpath('td[2]/div/div/span[2]/text()')[0].strip()
        comments = info.xpath('td[2]/div/div/span[3]/text()')[0].strip().strip("(").strip(")").strip()
        list_info = [song, singer, times[0:5], kind, score, comments[0:-3]]
        writer.writerow(list_info)
        list_music.append(list_info)
    # 防止请求频繁，故睡眠1秒
    time.sleep(1)


if __name__ == '__main__':
    for i in range(10):
      url = "https://music.douban.com/top250?start={}".format(i*25)
    # 调用函数music_info循环爬取内容
      music_info(url)

    # 关闭csv文件
    f.close()
    # 爬取的内容保存在xls文件中
    header = ["song", "singer", "time", "kind", "score", "comments"]
    # 打开工作簿
    book = xlwt.Workbook(encoding='utf-8')
    # 建立Sheet1工作表
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    i = 1
    for list in list_music:
        j = 0
        for data in list:
            sheet.write(i, j, data)
            j += 1
        i += 1
    # 保存文件
    book.save('doubanmusic.xls')