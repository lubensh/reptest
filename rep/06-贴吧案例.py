from urllib.request import urlopen,Request
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent":UserAgent().chrome
    }
    request = Request(url,headers=headers)
    response = urlopen(request)
    print(response.read().decode())
    return response.read()

def save_html(filename, html_bytes):

    with open(filename,"wb") as f:
        f.write(html_bytes)
        f.close()

def main():
    content = input("请输入要下载的内容：")
    num = input("请输入要下载多少页：")
    base_url = "http://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args={
            "pn":pn * 50,
            "kw":content
        }
        filename = "第" + str(pn + 1) + "页.html"
        args = urlencode(args)
        print("正在下载" + filename)
        html_byte = get_html(base_url.format(args))
        save_html(filename,html_byte)

if __name__ == "__main__":
    main()