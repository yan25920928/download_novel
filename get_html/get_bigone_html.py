import chardet
import requests


#获取一级页面的网页URL
def get_bigone_html(url):
    res = requests.get(url)
    html_bytes = res.content
    code_style = chardet.detect(html_bytes).get("encoding")
    html_text = html_bytes.decode(code_style)
    return html_text
