"""
此spider是一个很正经的spider(绝非lsp)
"""

import requests
import re
import os
for item in range(0,450,50):
      url = "https://tieba.baidu.com/f?kw=jk&ie=utf-8&pn={}".format(item)
      header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
      }
      dire = os.path.exists("./image")
      if dire == True:
            pass
      else:
            os.mkdir("./image")
      response = requests.get(url=url,headers=header)
      response.encoding = "utf-8"
      response_test = response.text
      re_cm = re.compile(r'<ul class="threadlist_media.*?bpic="(?P<url>.*?)"')

      resp = re_cm.finditer(response_test, re.S)
      for i in resp:
            download_url = i.group("url").strip()
            image_name = download_url.split("/")[5]
            img_request = requests.get(download_url)
            img_request_con = img_request.content
            with open("./image/" + image_name + ".jpg" ,"wb") as file:
                  file.write(img_request_con)