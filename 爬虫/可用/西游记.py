import requests
from lxml import etree


def downlaod(book_name, dire_url):
    url = "https://www.17k.com" + dire_url
    resp = requests.get(url=url)
    resp.encoding = "gbk2312"
    ep = etree.HTML(resp.text)
    dire_name = ep.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/p/text()')
    for i in dire_name:
        with open("book/" + book_name,"a", encoding="utf-8") as file:
            file.write(i)


def main_spider():
    url = "https://www.17k.com/list/1518510.html"
    resp = requests.get(url=url)
    resp.encoding = "gbk2312"
    resph = resp.text
    ep = etree.HTML(resph)
    dire_name = ep.xpath("/html/body/div[5]/dl/dd/a/span/text()")
    dir1_name = dire_name[1:]
    b = 1
    for i in dir1_name:
        book_name = i.strip().replace(" ", "-")
        dire_url = ep.xpath("/html/body/div[5]/dl/dd/a/@href")
        downlaod(book_name,dire_url[b])
        b += 1


if __name__ == "__main__":
    main_spider()
